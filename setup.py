from setuptools import setup, find_packages
from os import path

# read the contents of your README file
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="kube-context-suite",
    version="0.1.0",
    author="Nizhegolenko Oleksii",
    author_email="ratibor78@gmail.com",
    description="A lightweight suite of tools for managing and displaying Kubernetes contexts",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ratibor78/kube-context-suite",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Topic :: System :: Systems Administration",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Operating System :: POSIX :: Linux",
        "Environment :: Console",
    ],
    keywords="kubernetes, k8s, context, kubectl, devops, terminal, cli",
    package_dir={"": "src"},
    python_requires=">=3.6",
    install_requires=[
        "pyyaml>=5.1",
        "setuptools>=42",
        "wheel>=0.37.0",
    ],
    entry_points={
        "console_scripts": [
            "ksw=kube_context_suite.switcher:switch_context",
            "kube-prompt=kube_context_suite.prompt:main",
        ],
    },
    project_urls={
        "Bug Reports": "https://github.com/ratibor78/kube-context-suite/issues",
        "Source": "https://github.com/ratibor78/kube-context-suite",
    },
    include_package_data=True,
    zip_safe=False,
)