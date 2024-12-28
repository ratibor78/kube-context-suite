#!/usr/bin/env python3

"""
KSW - Console K8s Cluster Context Printer and Navigator
            Nizhegolenko Oleksii - 2024
                    MIT License
"""

import os
import yaml

def get_current_context():
    """
    Retrieve the current Kubernetes context from the kubeconfig file.
    """
    # Get the kubeconfig path from the environment or use the default
    config_path = os.getenv("KUBECONFIG", os.path.expanduser("~/.kube/config"))

    try:
        # Open and parse the kubeconfig file
        with open(config_path, "r") as f:
            config = yaml.safe_load(f)

        # Get the current context
        current_context = config.get("current-context", "No Context Found")
        return current_context

    except FileNotFoundError:
        return "Kubeconfig file not found"
    except yaml.YAMLError:
        return "Error parsing kubeconfig file"
    except Exception as e:
        return f"Unexpected error: {e}"


def display_context(context):
    """
    Display the current context with styled output.
    """
    K8S_SYMBOL = "\u2638"  # Kubernetes symbol
    CYAN = "\033[36m"
    BOLD = "\033[1m"
    RESET = "\033[0m"

    # Stylish output
    print(f"\n{CYAN}{BOLD}{K8S_SYMBOL} K8s Context: {RESET} {context}\n")


if __name__ == "__main__":
    current_context = get_current_context()
    display_context(current_context)
