#!/bin/bash
# Sources this file to activate rbenv in your current shell session.
# Usage: source ruby-env.sh  (note: must use 'source', not 'bash')

export PATH="$HOME/.rbenv/bin:$PATH"
eval "$(rbenv init - bash)"

echo "Ruby environment ready: $(ruby --version)"
echo "You can now run: bundle exec jekyll serve"
