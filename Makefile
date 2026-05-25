.PHONY: install serve build clean

install:
	bundle install

serve: install
	bundle exec jekyll serve --livereload

build: install
	bundle exec jekyll build

clean:
	bundle exec jekyll clean
