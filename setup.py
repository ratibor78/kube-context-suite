from setuptools import setup, find_packages

setup(
    name="kube-context-suite",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "pyyaml>=5.1",
    ],
    entry_points={
        'console_scripts': [
            'ksw=kube_context_suite.switcher:switch_context',
            'kube-prompt=kube_context_suite.prompt:main',
        ],
    },
    author="Nizhegolenko Oleksii",
    author_email="your.email@example.com",
    description="Kubernetes Context Management Suite",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/kube-context-suite",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)