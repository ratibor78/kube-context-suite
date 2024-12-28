#!/bin/bash

# Install package
pip install -e .

# Add prompt command to bashrc if not already present
PROMPT_CMD='PROMPT_COMMAND="kube-prompt; \${PROMPT_COMMAND}"'
if ! grep -q "$PROMPT_CMD" ~/.bashrc; then
    echo "$PROMPT_CMD" >> ~/.bashrc
    source ~/.bashrc
fi

echo "Installation complete! Please restart your terminal or run 'source ~/.bashrc'"