# 🧮 Advanced Calculator Application

An advanced Python command-line calculator demonstrating object-oriented programming, software design patterns, configuration management, logging, automated testing, and continuous integration.

---

# 📖 1. Project Description

This project is an advanced calculator application built in Python using object-oriented programming principles and several software design patterns. The calculator supports basic and advanced mathematical operations, maintains calculation history, provides undo/redo functionality, automatically saves history, logs calculator activity, and includes automated testing through GitHub Actions.

This project demonstrates:

- Factory Pattern
- Strategy Pattern
- Observer Pattern
- Memento Pattern
- Environment Configuration
- Logging
- Continuous Integration
- Unit Testing
- Code Coverage

---

# ⚙️ 2. Installation

## Clone the Repository

```bash
git clone https://github.com/TechyMel/midterm-project.git
cd midterm-project
```

---

## Create a Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

Verify installation:

```bash
pip list
```

---

# 🔧 3. Configuration Setup

This project supports configuration using **python-dotenv**.

Copy the example configuration file:

```bash
cp .env.example .env
```

The following environment variables are supported:

```env
CALCULATOR_BASE_DIR=.
CALCULATOR_MAX_HISTORY_SIZE=1000
CALCULATOR_AUTO_SAVE=true
CALCULATOR_PRECISION=10
CALCULATOR_MAX_INPUT_VALUE=1e999
CALCULATOR_DEFAULT_ENCODING=utf-8
CALCULATOR_LOG_DIR=logs
CALCULATOR_HISTORY_DIR=history
CALCULATOR_HISTORY_FILE=history/calculator_history.csv
CALCULATOR_LOG_FILE=logs/calculator.log
```

If no `.env` file exists, the calculator automatically uses the default configuration values.

---

# 🚀 4. Running the Application

Run the calculator:

```bash
python main.py
```

You should see:

```text
Calculator started. Type 'help' for commands.
```

---

# ⌨️ 5. Calculator Commands

Supported commands:

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

Result: 15 (in green)
```

Power

```text
Enter command: power

First number: 2
Second number: 8

Result: 256
```

View History

```text
Enter command: history
```

Undo

```text
Enter command: undo
```

Redo

```text
Enter command: redo
```

Save History

```text
Enter command: save
```

Load History

```text
Enter command: load
```

---

# 🎨 Terminal Features

The calculator uses **Colorama** to improve readability.

- 🔵 Welcome messages
- 🟢 Successful calculations
- 🟡 Exit messages
- 🔴 Error messages

---

# 🏗️ 6. Design Patterns

## Factory Pattern

Creates operation objects dynamically without modifying the calculator.

## Strategy Pattern

Allows the calculator to switch between mathematical operations during runtime.

## Observer Pattern

Automatically logs calculations and saves history whenever a calculation is performed.

## Memento Pattern

Stores calculator history, enabling Undo and Redo functionality.

---

# 📝 7. Logging

The application uses a centralized **logger.py** module to configure application logging.

Logs are automatically written to:

```
logs/calculator.log
```

Calculation history is stored in:

```
history/calculator_history.csv
```

---

# 🧪 8. Testing

Run all tests:

```bash
python -m pytest
```

Generate coverage report:

```bash
python -m pytest --cov=app --cov-report=term-missing --cov-report=html
```

Current Results:

- ✅ 123 Unit Tests Passing
- ✅ 90% Code Coverage

Coverage reports are generated inside:

```
htmlcov/
```

---

# 🔄 9. Continuous Integration (GitHub Actions)

This project uses GitHub Actions for Continuous Integration.

Every push or pull request automatically:

- Installs project dependencies
- Runs all unit tests
- Checks code coverage
- Verifies successful builds

Workflow location:

```
.github/workflows/tests.yml
```

---

# 📁 10. Project Structure

```
midterm-project/
│
├── app/
│   ├── __init__.py
│   ├── calculation.py
│   ├── calculator.py
│   ├── calculator_config.py
│   ├── calculator_memento.py
│   ├── calculator_repl.py
│   ├── exceptions.py
│   ├── history.py
│   ├── input_validators.py
│   ├── logger.py
│   └── operations.py
│
├── history/
├── htmlcov/
├── logs/
├── tests/
│
├── .env.example
├── .github/
├── LICENSE
├── main.py
├── pytest.ini
├── requirements.txt
└── README.md
```

---

# 📊 11. Features

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
- Undo
- Redo
- Save History
- Load History
- Clear History
- Automatic History Saving
- Calculation Logging
- Colored Terminal Output
- Environment Configuration
- CSV History Storage
- Unit Testing
- GitHub Actions CI/CD

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
| Generate Coverage | `python -m pytest --cov=app --cov-report=html` |
| Git Add | `git add .` |
| Commit | `git commit -m "message"` |
| Push | `git push origin main` |

---

# 📋 Requirements

- Python 3.12+
- Git
- Virtual Environment
- pandas
- python-dotenv
- pytest
- pytest-cov
- Colorama

---

# 📚 Technologies Used

- Python
- Pandas
- Pytest
- Pytest-Cov
- Colorama
- python-dotenv
- Git
- GitHub Actions

---

# 👩‍💻 Author

**Melvina Temu**

Business Information Systems Student

New Jersey Institute of Technology