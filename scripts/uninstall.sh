#!/bin/bash

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${YELLOW}Starting uninstallation of kube-context-suite...${NC}"

# Function to remove PROMPT_COMMAND from bashrc
remove_from_bashrc() {
    # Remove the prompt command from .bashrc
    echo -e "${YELLOW}Removing prompt configuration from .bashrc...${NC}"
    if [ -f ~/.bashrc ]; then
        # Create a backup of .bashrc
        cp ~/.bashrc ~/.bashrc.backup.$(date +%Y%m%d_%H%M%S)
        echo -e "${GREEN}Created backup of .bashrc${NC}"
        
        # Remove the PROMPT_COMMAND line
        sed -i '/PROMPT_COMMAND="kube-prompt/d' ~/.bashrc
        echo -e "${GREEN}Removed prompt configuration from .bashrc${NC}"
    else
        echo -e "${YELLOW}No .bashrc file found${NC}"
    fi
}

# Function to uninstall the package
uninstall_package() {
    echo -e "${YELLOW}Uninstalling kube-context-suite package...${NC}"
    if pip uninstall -y kube-context-suite; then
        echo -e "${GREEN}Successfully uninstalled kube-context-suite package${NC}"
    else
        echo -e "${RED}Failed to uninstall package${NC}"
        return 1
    fi
}

# Main uninstallation process
echo -e "${YELLOW}Checking for existing installation...${NC}"

# Check if the package is installed
if pip show kube-context-suite > /dev/null 2>&1; then
    # Remove from bashrc first
    remove_from_bashrc
    
    # Then uninstall the package
    uninstall_package
    
    echo -e "${GREEN}Uninstallation completed successfully!${NC}"
    echo -e "${YELLOW}Note: Please restart your terminal or run 'source ~/.bashrc' to apply changes${NC}"
else
    echo -e "${YELLOW}Package kube-context-suite is not installed${NC}"
    
    # Still try to remove from bashrc if exists
    remove_from_bashrc
    
    echo -e "${GREEN}Cleanup completed${NC}"
fi

# Final cleanup check
if which ksw >/dev/null 2>&1; then
    echo -e "${RED}Warning: 'ksw' command is still available in: $(which ksw)${NC}"
    echo -e "${YELLOW}You may need to manually remove it or check your PATH${NC}"
fi

if which kube-prompt >/dev/null 2>&1; then
    echo -e "${RED}Warning: 'kube-prompt' command is still available in: $(which kube-prompt)${NC}"
    echo -e "${YELLOW}You may need to manually remove it or check your PATH${NC}"
fi

exit 0