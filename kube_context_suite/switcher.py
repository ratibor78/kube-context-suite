#!/usr/bin/env python3

"""
KSW - Console K8s Cluster Context Printer and Switcher
            Nizhegolenko Oleksii - 2024
                    MIT License
"""

import os
import yaml
import shutil
import curses
import subprocess


def check_kubectl():
    """
    Check if kubectl is installed and available in PATH.
    """
    if not shutil.which("kubectl"):
        print("Error: 'kubectl' is not installed or not in PATH.")
        exit(1)


def load_kubeconfig():
    """
    Load the Kubernetes configuration file.
    Returns the loaded configuration or an error message.
    """
    config_path = os.getenv("KUBECONFIG", os.path.expanduser("~/.kube/config"))

    try:
        with open(config_path, "r") as f:
            return yaml.safe_load(f)
    except FileNotFoundError:
        return {"error": "Kubeconfig file not found"}
    except yaml.YAMLError:
        return {"error": "Error parsing kubeconfig file"}
    except Exception as e:
        return {"error": f"Unexpected error: {e}"}


def get_current_context():
    """
    Retrieve the current Kubernetes context from the kubeconfig.
    """
    config = load_kubeconfig()
    if "error" in config:
        print(config["error"])
        exit(1)

    return config.get("current-context", "No Context Found")


def list_contexts():
    """
    Retrieve a list of all available Kubernetes contexts.
    
    Returns:
        List[str]: List of context names
    """
    config = load_kubeconfig()
    if "error" in config:
        print(config["error"])
        return []

    contexts = config.get("contexts", [])
    return [context["name"] for context in contexts if "name" in context]


def interactive_menu(stdscr, contexts, current_context):
    """
    Render an interactive menu for Kubernetes context selection.

    Parameters:
        stdscr: The curses screen object.
        contexts: List of Kubernetes contexts.
        current_context: The currently active Kubernetes context.

    Returns:
        The selected context as a string or None if the user exits without selection.
    """
    try:
        curses.curs_set(0)  # Hide cursor
        stdscr.clear()
        selected_row = 0

        while True:
            stdscr.clear()
            height, width = stdscr.getmaxyx()

            # Title and instructions
            title = f"K8s Context Switcher - {len(contexts)} contexts available"
            instructions = "Use UP/DOWN arrows to select, ENTER to confirm, Q to exit"
            stdscr.addstr(0, width // 2 - len(title) // 2, title, curses.color_pair(1))
            stdscr.addstr(1, width // 2 - len(instructions) // 2, instructions, curses.color_pair(1))
            stdscr.addstr(2, 0, "-" * width, curses.color_pair(1))  # Horizontal line

            # Render contexts
            for idx, context in enumerate(contexts, 1):  # Start numbering from 1
                y = 4 + (idx - 1) * 2  # Space out rows
                x = width // 2 - len(context) // 2 - 4

                if idx - 1 == selected_row:
                    stdscr.attron(curses.color_pair(2))  # Highlighted row
                    marker = "\u279C "  # Arrow symbol
                else:
                    stdscr.attron(curses.color_pair(1))
                    marker = "  "

                active_mark = "\u2713" if context == current_context else " "
                stdscr.addstr(y, x, f"{marker}{idx}. {context} [{active_mark}]")
                stdscr.attroff(curses.color_pair(2))

            stdscr.refresh()

            # Handle key inputs
            key = stdscr.getch()
            if key == curses.KEY_UP and selected_row > 0:
                selected_row -= 1
            elif key == curses.KEY_DOWN and selected_row < len(contexts) - 1:
                selected_row += 1
            elif key == ord("\n"):  # Enter key
                return contexts[selected_row]
            elif key in (ord("q"), ord("Q")):  # Exit on Q or q
                return None

    except Exception as e:
        # Gracefully handle any exceptions
        stdscr.clear()
        stdscr.addstr(0, 0, f"An error occurred: {str(e)}", curses.color_pair(1))
        stdscr.refresh()
        stdscr.getch()
        return None


def switch_context():
    """
    Main function to list contexts and handle interactive menu.
    """
    try:
        check_kubectl()

        # Retrieve contexts and the current context
        contexts = list_contexts()
        if not contexts:
            print("No Kubernetes contexts found. Exiting.")
            return

        current_context = get_current_context()

        # Initialize curses for the interactive menu
        curses.wrapper(lambda stdscr: interactive_run(stdscr, contexts, current_context))

    except FileNotFoundError:
        print("Error: 'kubectl' is not installed or not in PATH.")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")


def interactive_run(stdscr, contexts, current_context):
    """
    Run the interactive menu and switch context if a new context is selected.

    Parameters:
        stdscr: The curses screen object.
        contexts: List of Kubernetes contexts.
        current_context: The currently active Kubernetes context.
    """
    # Setup colors
    curses.start_color()
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)  # Normal text
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_CYAN)   # Highlighted text

    # Show interactive menu
    selected_context = interactive_menu(stdscr, contexts, current_context)

    # Check if the user exited without selection
    if selected_context is None:
        return

    # Try to switch Kubernetes context
    try:
        subprocess.check_call(["kubectl", "config", "use-context", selected_context])
        print(f"Successfully switched to context: {selected_context}")
    except subprocess.CalledProcessError:
        print("Error: Failed to switch context.")
    except Exception as e:
        print(f"Unexpected error: {str(e)}")


if __name__ == '__main__':
    switch_context()
