#!/bin/bash
# Initializes rbenv and serves the Jekyll site locally.
# Run from the website directory: bash serve.sh

export PATH="$HOME/.rbenv/bin:$PATH"
eval "$(rbenv init - bash)"

echo "Ruby: $(ruby --version)"
echo "Starting Jekyll at http://localhost:4000 ..."
echo "(Press Ctrl+C to stop)"
echo ""

bundle exec jekyll serve --livereload
