# one-time setup
## with timeout
git config --global credential.helper 'cache --timeout=3600'
## no timeout
git config --global credential.helper cache
