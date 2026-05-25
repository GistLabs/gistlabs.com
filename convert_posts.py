#!/usr/bin/env python3
import re
import os
import subprocess
import sys

def html_to_markdown(html_content):
    """Convert HTML to Markdown preserving EXACT original text"""
    content = html_content
    
    # Convert blockquotes - need to handle nested <p> tags
    def blockquote_replace(m):
        text = m.group(1).strip()
        text = re.sub(r'<p>(.*?)</p>', r'\1\n', text, flags=re.DOTALL)
        lines = [line.strip() for line in text.split('\n') if line.strip()]
        return '\n' + '\n'.join('> ' + line for line in lines) + '\n\n'
    content = re.sub(r'<blockquote>(.*?)</blockquote>', blockquote_replace, content, flags=re.DOTALL)
    
    # Convert lists
    content = re.sub(r'<ul[^>]*>\s*', '\n', content)
    content = re.sub(r'</ul>\s*', '\n', content)
    content = re.sub(r'<ol[^>]*>\s*', '\n', content)
    content = re.sub(r'</ol>\s*', '\n', content)
    content = re.sub(r'<li>(.*?)</li>', r'- \1', content, flags=re.DOTALL)
    
    # Convert paragraphs
    content = re.sub(r'<p[^>]*>(.*?)</p>', r'\1\n\n', content, flags=re.DOTALL)
    
    # Convert line breaks
    content = re.sub(r'<br\s*/?>', '\n', content)
    
    # Convert links - preserve exact href
    content = re.sub(r'<a\s+href="([^"]+)"[^>]*>(.*?)</a>', r'[\2](\1)', content)
    
    # Convert emphasis
    content = re.sub(r'<em>(.*?)</em>', r'*\1*', content)
    content = re.sub(r'<i>(.*?)</i>', r'*\1*', content)
    content = re.sub(r'<strong>(.*?)</strong>', r'**\1**', content)
    content = re.sub(r'<b>(.*?)</b>', r'**\1**', content)
    
    # Convert code
    content = re.sub(r'<code>(.*?)</code>', r'`\1`', content)
    
    # Convert headings
    content = re.sub(r'<h([1-6])[^>]*>(.*?)</h\1>', lambda m: '#' * int(m.group(1)) + ' ' + m.group(2) + '\n\n', content)
    
    # Convert images
    content = re.sub(r'<img[^>]+src="([^"]+)"[^>]*/?>', r'![](\1)', content)
    
    # Handle HTML entities
    content = content.replace('&#8217;', "'")
    content = content.replace('&#8220;', '"')
    content = content.replace('&#8221;', '"')
    content = content.replace('&#8230;', '...')
    content = content.replace('&nbsp;', ' ')
    content = content.replace('&amp;', '&')
    content = content.replace('&lt;', '<')
    content = content.replace('&gt;', '>')
    content = content.replace('&#038;', '&')
    
    # Clean up extra whitespace
    content = re.sub(r'\n{3,}', '\n\n', content)
    content = re.sub(r'[ \t]+\n', '\n', content)
    content = content.strip()
    
    return content

def extract_title(html):
    """Extract title from HTML"""
    match = re.search(r'<h1[^>]*class="[^"]*entry-title[^"]*"[^>]*>(.*?)</h1>', html, re.DOTALL)
    if match:
        title = match.group(1).strip()
        # Clean HTML entities
        title = title.replace('&#8217;', "'")
        title = title.replace('&#8220;', '"')
        title = title.replace('&#8221;', '"')
        title = title.replace('&#8230;', '...')
        title = title.replace('&amp;', '&')
        return title
    return ""

def extract_content(html):
    """Extract entry-content from HTML"""
    match = re.search(r'<div class="entry-content clear"[^>]*>(.*?)</div><!-- \.entry-content \.clear -->', html, re.DOTALL)
    if match:
        return match.group(1)
    return ""

def extract_images(content):
    """Extract all image URLs from content"""
    images = re.findall(r'<img[^>]+src="([^"]+)"', content)
    return images

def download_image(url, dest_dir):
    """Download an image and return the local filename"""
    if not url.startswith('http'):
        return None
    
    filename = os.path.basename(url.split('?')[0])  # Remove query params
    dest_path = os.path.join(dest_dir, filename)
    
    # Skip if already downloaded
    if os.path.exists(dest_path):
        return filename
    
    try:
        result = subprocess.run(['curl', '-L', '-o', dest_path, url], check=True, capture_output=True)
        return filename
    except:
        return None

def process_blog_post(html_file, date, title):
    """Process a single blog post HTML file"""
    
    with open(html_file, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Extract title from HTML if not provided
    html_title = extract_title(html)
    if not title:
        title = html_title
    
    # Extract content
    content_html = extract_content(html)
    if not content_html:
        print(f"Could not extract content from {html_file}")
        return None
    
    # Extract images
    images = extract_images(content_html)
    
    # Download images to assets folder
    assets_dir = './assets'
    os.makedirs(assets_dir, exist_ok=True)
    
    image_map = {}
    for img_url in images:
        local_name = download_image(img_url, assets_dir)
        if local_name:
            image_map[img_url] = local_name
    
    # Convert content to markdown
    markdown_content = html_to_markdown(content_html)
    
    # Replace image URLs with Jekyll relative_url format
    for old_url, new_name in image_map.items():
        markdown_content = markdown_content.replace(old_url, f"{{{{ '/assets/{new_name}' | relative_url }}}}")
    
    # Create frontmatter
    # Extract slug from date and title
    year, month = date.split('-')[:2]
    slug = title.lower()
    slug = re.sub(r'[^a-z0-9\s-]', '', slug)
    slug = re.sub(r'\s+', '-', slug)
    slug = slug.strip('-')
    
    permalink = f"/{year}/{month}/{slug}/"
    
    frontmatter = f"""---
layout: post
title: "{title}"
date: {date}
author: John Heintz
categories: posts
permalink: {permalink}
---
"""
    
    # Create Jekyll markdown file
    filename = f"{date}-{slug}.markdown"
    filepath = os.path.join('./_posts', filename)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(frontmatter)
        f.write('\n')
        f.write(markdown_content)
    
    return filename

# Posts to process with their dates and titles
posts_to_process = [
    ('big-data.html', '2012-08-01', 'Big Data, Little Tests'),
    ('ignore-hours.html', '2012-08-15', 'Ignore hours, focus on collaboration'),
    ('mechanize.html', '2012-09-01', 'Announcing mechanize for java'),
    ('rules-collab.html', '2013-01-15', 'Rules for Fast Collaboration'),
    ('spoon.html', '2013-04-01', 'Spoon Framework'),
    ('scrum-master.html', '2013-04-10', 'The Role of the Scrum Master'),
    ('visualizing-work.html', '2013-04-20', 'Visualizing Work'),
    ('mechanics-agile.html', '2013-09-01', 'Mechanics Agile'),
    ('video-devops.html', '2013-09-10', 'Video Business Impact DevOps'),
    ('video-motivation.html', '2013-09-15', 'Video Motivation for Agile'),
    ('video-planning.html', '2013-09-20', 'Video Sequential and Collaborative Planning'),
    ('user-story.html', '2013-11-01', 'The User Story'),
    ('keynote-india.html', '2014-01-15', 'Keynote at the Lean India Summit 2013 Work Visualization'),
]

# Process all files
blog_dir = '/tmp/blog_posts'
results = []

for html_file, date, title in posts_to_process:
    filepath = os.path.join(blog_dir, html_file)
    if os.path.exists(filepath):
        result = process_blog_post(filepath, date, title)
        if result:
            results.append(result)
            print(f"✓ Created {result}")
        else:
            print(f"✗ Failed to process {html_file}")
    else:
        print(f"✗ File not found: {filepath}")

print(f"\n{len(results)} blog posts converted successfully")
