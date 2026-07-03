# 🧮 Advanced Calculator Application

A Python command-line calculator application demonstrating object-oriented programming, software design patterns, configuration management, logging, persistent storage, and automated testing.

---

# 📖 1. Project Description

This project is an advanced calculator application built in Python. It supports multiple mathematical operations while demonstrating software engineering principles including the Factory, Strategy, Observer, and Memento design patterns.

The calculator includes persistent calculation history using CSV files, undo/redo functionality, configuration through environment variables, colored terminal output using Colorama, logging, and automated testing with GitHub Actions.

---

# ⚙️ 2. Installation

## Clone the Repository

```bash
git clone https://github.com/TechyMel/midtermproject.git
cd midtermproject
```

---

## Create a Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Mac/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## Install Required Packages

```bash
pip install -r requirements.txt
```

Verify installation:

```bash
pip list
```

---

# 🔧 3. Configuration Setup

This project uses **python-dotenv** to load optional configuration settings from a `.env` file.

Create a `.env` file in the project root or copy the provided `.env.example` file.

Example:

```bash
cp .env.example .env
```

The application supports the following environment variables:

| Variable | Description | Default |
|----------|-------------|---------|
| `CALCULATOR_BASE_DIR` | Base project directory | Project Root |
| `CALCULATOR_LOG_DIR` | Directory for log files | `logs/` |
| `CALCULATOR_HISTORY_DIR` | Directory for history files | `history/` |
| `CALCULATOR_HISTORY_FILE` | CSV history file | `history/calculator_history.csv` |
| `CALCULATOR_LOG_FILE` | Log file location | `logs/calculator.log` |
| `CALCULATOR_MAX_HISTORY_SIZE` | Maximum history entries | `1000` |
| `CALCULATOR_AUTO_SAVE` | Automatically save history | `true` |
| `CALCULATOR_PRECISION` | Decimal precision | `10` |
| `CALCULATOR_MAX_INPUT_VALUE` | Maximum input value | `1e999` |
| `CALCULATOR_DEFAULT_ENCODING` | File encoding | `utf-8` |

If no `.env` file is provided, the application automatically uses these default values.

---

# 🚀 4. Running the Calculator

Start the calculator with:

```bash
python main.py
```

You should see:

```
Calculator started. Type 'help' for commands.
```

---

# ⌨️ 5. Available Commands

```
help
add
subtract
multiply
divide
power
root
modulus
intdiv
percentage
absdiff
history
undo
redo
save
load
clear
exit
```

---

# ➕ Example Usage

Addition

```text
Enter command: add

First number: 5
Second number: 10

Result: 15
```

Power

```text
Enter command: power

First number: 2
Second number: 8

Result: 256
```

History

```text
Enter command: history
```

Undo

```text
Enter command: undo
```

Save History

```text
Enter command: save
```

---

# 🧪 6. Running Tests

Run all unit tests

```bash
python -m pytest
```

Generate a coverage report

```bash
python -m pytest --cov=app --cov-report=term-missing --cov-report=html
```

Current Results

- ✅ 123 Unit Tests Passing
- ✅ 90% Code Coverage

---

# 🔄 7. GitHub Actions (CI/CD)

This project uses GitHub Actions to automatically:

- Install project dependencies
- Run all unit tests
- Measure code coverage
- Verify successful builds on every push to GitHub

Workflow location:

```
.github/workflows/tests.yml
```

---

# 🏗️ 8. Design Patterns Used

### Factory Pattern

Creates calculator operations dynamically without modifying the calculator itself.

### Strategy Pattern

Allows the calculator to switch between different mathematical operations at runtime.

### Observer Pattern

Automatically logs calculations and saves history whenever calculations are performed.

### Memento Pattern

Stores calculator history to support Undo and Redo functionality.

---

# 📁 9. Project Structure

```
midtermproject/
│
├── app/
│   ├── calculator.py
│   ├── calculator_repl.py
│   ├── calculation.py
│   ├── calculator_config.py
│   ├── calculator_memento.py
│   ├── operations.py
│   ├── history.py
│   ├── exceptions.py
│   └── input_validators.py
│
├── tests/
│
├── logs/
│
├── history/
│
├── requirements.txt
├── pytest.ini
├── main.py
└── README.md
```

---

# 📊 10. Features

- Addition
- Subtraction
- Multiplication
- Division
- Power
- Root
- Modulus
- Integer Division
- Percentage
- Absolute Difference
- Calculation History
- Save History
- Load History
- Undo / Redo
- Colored Terminal Output (Colorama)
- Logging
- CSV History Storage
- Environment Configuration
- Automated Testing
- GitHub Actions CI/CD

---

# 📝 11. Logging

Application logs are automatically written to the **logs/** directory.

Calculation history is stored inside the **history/** directory as CSV files.

---

# 🔥 Useful Commands Cheat Sheet

| Action | Command |
|------------------------------|--------------------------------|
| Create Virtual Environment | `python -m venv venv` |
| Activate Virtual Environment (Windows) | `venv\Scripts\activate` |
| Activate Virtual Environment (Linux/Mac) | `source venv/bin/activate` |
| Install Dependencies | `pip install -r requirements.txt` |
| Run Calculator | `python main.py` |
| Run Tests | `python -m pytest` |
| Run Coverage | `python -m pytest --cov=app --cov-report=html` |
| Git Add | `git add .` |
| Commit | `git commit -m "message"` |
| Push | `git push origin main` |

---

# 📋 Requirements

- Python 3.12+
- Git
- Virtual Environment
- pip

---

# 📚 Technologies Used

- Python
- Pandas
- Pytest
- Pytest-Cov
- Colorama
- Git
- GitHub Actions

---

# 👩‍💻 Author

**Melvina Temu**

Business Information Systems Student

New Jersey Institute of Technology