#!/usr/bin/env bash
# Setup script: installs pre-commit and creates the git pre-commit hook
# so that .pre-commit-config.yaml runs automatically on every git commit.
#
# Usage: ./setup-pre-commit.sh

set -e

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$REPO_ROOT"

# Must be inside a git repo
if ! git rev-parse --git-dir > /dev/null 2>&1; then
  echo "Error: Not a git repository. Run this from the project root."
  exit 1
fi

# Prefer pre-commit from the project venv (avoids pyenv/version conflicts)
VENV_PRE_COMMIT="$REPO_ROOT/.venv/bin/pre-commit"
if [[ -x "$VENV_PRE_COMMIT" ]]; then
  PRE_COMMIT="$VENV_PRE_COMMIT"
  echo "Using pre-commit from .venv"
elif [[ -d "$REPO_ROOT/.venv" ]]; then
  echo "Installing pre-commit into .venv..."
  "$REPO_ROOT/.venv/bin/pip" install pre-commit
  PRE_COMMIT="$VENV_PRE_COMMIT"
elif command -v pre-commit > /dev/null 2>&1; then
  PRE_COMMIT="pre-commit"
  echo "pre-commit is already installed (from PATH)."
else
  echo "Installing pre-commit..."
  pip install pre-commit
  PRE_COMMIT="pre-commit"
fi

# Create the pre-commit hook (writes .git/hooks/pre-commit)
echo "Installing pre-commit hook from .pre-commit-config.yaml..."
"$PRE_COMMIT" install

echo "Done. The pre-commit hook is installed."
echo "On each 'git commit', pre-commit will run the hooks in .pre-commit-config.yaml."
echo ""
echo "To run hooks manually:  pre-commit run --all-files"
echo "To run a single hook:   pre-commit run pytest-coverage --all-files"
