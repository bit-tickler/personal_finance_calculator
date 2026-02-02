# Personal Finance Calculator
Author: Michael Shields

## About
A text-based command line application that allows the user to enter their finances and view a budget summary. This project was complete for **Beng Software Engineering - Computer Science Fundamentals (COM4302)**

## Prerequisites.

Before setting up the project, ensure you have the following installed:

- Git: For cloning the repository. Install via your package manager (e.g., `sudo apt install git` on Debian/Ubuntu) or download from [git-scm.com](git-scm.com).
- Python 3.11 or higher: Download and install from python.org. Verify with `python3 --version`.
- pip: Included with Python 3.11+. Verify with `pip3 --version`. If missing, install `via sudo apt install python3-pip` (on Debian/Ubuntu) or follow [Python docs](https://docs.python.org/3/).

## Cloning the Repository
Clone the project from GitHub:
```bash
git clone https://github.com/bit-tickler/personal_finance_calculator.git
```

Change directory into the cloned project:
```bash
cd personal-finance-calculator
```

## Installation
This project requires Python 3.11 or higher and has dependencies listed in pyproject.toml.

Using Poetry (Recommended)
Poetry manages dependencies and virtual environments automatically.

1. Install pipx if you haven't already (on Debian/Ubuntu-based systems):
```bash
sudo apt update
sudo apt install pipx
```
(For other systems, refer to the [pipx documentation](https://pipx.pypa.io/stable/installation/)

2. Install Poetry using pipx:
```bash
pipx install poetry
```
3. Ensure pipx binaries are in your PATH (run this and restart your terminal if needed):
```bash
pipx ensurepath
```
4. Install the project dependencies:
```bash
poetry install
```

## Running the Application
To run the application:
If using Poetry (runs in the virtual environment):
```bash
poetry run python3 main.py
```

