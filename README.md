# 🚀 Kube Context Suite

A lightweight suite of tools designed to streamline Kubernetes context management in your terminal. This suite includes an interactive context switcher and a prompt integration that constantly displays your current context.

![Kube Context Suite Demo](screenshots/demo.gif)

## ✨ Features

- **Interactive Context Switcher (ksw)**
  - Beautiful TUI interface for switching between contexts
  - Quick navigation with arrow keys
  - Visual indicators for active context
  - Easy exit with 'q'

- **Context Prompt Integration**
  - Shows current Kubernetes context in your terminal prompt
  - Color-coded for better visibility
  - Kubernetes wheel symbol (⎈) indicator
  - Updates automatically after each command

## 🛠️ Prerequisites

- Python 3.6 or higher
- kubectl installed and configured
- Valid kubeconfig file

## 📦 Installation

### Manual Installation
```bash
# Clone the repository
git clone https://github.com/ratibor78/kube-context-suite
cd kube-context-suite

# Install the package
pip install -e .

# Or use the installation script
./scripts/install.sh
```

## 🚀 Quick Start

### Context Switcher
```bash
# Launch the interactive context switcher
ksw
```

### Prompt Integration
Add the following line to your `~/.bashrc` or `~/.bash_profile`:
```bash
PROMPT_COMMAND="kube-prompt; $PROMPT_COMMAND"
```

Then, source your profile:
```bash
source ~/.bashrc  # or source ~/.bash_profile
```

## 🎮 Usage

### Context Switcher (ksw)
- Launch with `ksw` command
- Use ↑/↓ arrows to navigate between contexts
- Press Enter to select a context
- Press 'q' to exit without changes

### Prompt Display
Once configured, your prompt will automatically show:
- Current Kubernetes context
- Kubernetes wheel symbol (⎈)
- Color-coded output for better visibility

Example prompt:
```
⎈ K8s Context: production-cluster
username@hostname:~$
```

## ⚙️ Configuration

The suite uses your existing kubeconfig file, typically located at:
- Default path: `~/.kube/config`
- Custom path: Set via `KUBECONFIG` environment variable

## 📦 Uninstall 

Just run script `./scripts/uninstall.sh` this will remove scripts from your configs

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Created by Nizhegolenko Oleksii
- Inspired by the need for simpler Kubernetes context management
- Thanks to all contributors who help improve this project

## 🐛 Troubleshooting

### Common Issues

1. **Context not showing in prompt**
   - Ensure `PROMPT_COMMAND` is correctly set in your `.bashrc`
   - Try restarting your terminal

2. **ksw command not found**
   - Verify the installation with `pip list | grep kube-context-suite`
   - Check if `~/.local/bin` are in your `PATH` if nope add `export PATH="$HOME/.local/bin:$PATH"` to the end of your `~/.bashrc` file
   
3. **Kubeconfig errors**
   - Verify your kubeconfig file exists and is valid
   - Check permissions on your kubeconfig file

### Getting Help

If you encounter any issues:
1. Check the [Issues](https://github.com/ratibor78/kube-context-suite/issues) page
2. Search for existing problems
3. Create a new issue with:
   - Your OS version
   - Python version (`python --version`)
   - Installation method used
   - Error message or unexpected behavior

## 🔄 Version History

- 0.1.0
  - Initial release
  - Interactive context switcher
  - Prompt integration
  - Basic documentation

## 📫 Contact

Nizhegolenko Oleksii
- GitHub: [@ratibor78](https://github.com/ratibor78)
- Email: ratibor78@gmail.com

---

Made with ❤️ for the Kubernetes community