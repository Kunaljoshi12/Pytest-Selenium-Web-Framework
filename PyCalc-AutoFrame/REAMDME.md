# PyCalc-AutoFrame

**PyCalc-AutoFrame** is a professional-grade, hybrid data-driven automation framework built with Python and Selenium. Unlike basic automation scripts, this framework is designed to validate a web-based calculator application using real-world QA practices, including the Page Object Model (POM) and external database integration.

## 🌟 Project Overview

The core philosophy of this framework is to **scale test coverage without modifying code**. By decoupling test data from the test logic, new scenarios can be added simply by updating the connected MySQL database.

## 🚀 Key Features

* **Modular Architecture (POM):** Utilizes `CalculatorPage.py` to isolate UI locators and interactions from test scripts, ensuring high maintainability.
* **Hybrid Data-Driven Testing:** Test parameters (, ) are dynamically injected from a MySQL database via `DBUtils.py`.
* **Comprehensive Test Coverage:** Automated suites for Addition, Subtraction, Multiplication, and Division.
* **Automated HTML Reporting:** Generates a detailed `report.html` featuring execution summaries, timestamps, and pass/fail statuses.
* **Edge Case Logic:** Intelligent handling for floating-point rounding and safety checks for division-by-zero scenarios.

---

## 🛠️ Technical Stack

| Component | Technology |
| --- | --- |
| **Language** | Python 3.13+ |
| **Automation Tool** | Selenium WebDriver |
| **Testing Framework** | Pytest |
| **Database** | MySQL |
| **Frontend** | HTML, CSS, JavaScript |

---

## 📂 Project Structure

```text
PyCalc-AutoFrame/
├── Calculator/             # Pytest test scripts (DB-driven)
│   ├── test_addition.py
│   ├── test_subtraction.py
│   ├── test_multiplication.py
│   └── test_division.py    # Includes zero-check logic
├── WebApp/                 # The Application Under Test (AUT)
│   └── Calculator.html     # JS-based web calculator
├── Data/                   # Database resources
│   └── Data_set.sql        # SQL script to initialize test data
├── CalculatorPage.py       # Page Object Model (Locators & Actions)
├── conftest.py             # Pytest fixtures (Driver setup/teardown)
├── DBUtils.py              # MySQL utility layer
├── Cal.py                  # Main execution entry point
└── report.html             # Auto-generated execution report

```

---

## ⚙️ Execution Flow

1. **Initialization:** `Cal.py` triggers the run; `conftest.py` sets up the Chrome WebDriver environment.
2. **Data Retrieval:** `DBUtils.py` queries the MySQL database to fetch test datasets.
3. **UI Interaction:** The test scripts execute actions on the WebApp through the `CalculatorPage` class.
4. **Verification:** UI results are captured and compared against dynamically calculated expected values.
5. **Finalization:** Pytest compiles the results into a self-contained HTML report.

---

## 🔧 Setup & Usage

### 1. Database Configuration

Run the `Data_set.sql` script in your MySQL instance. Update the connection credentials within `DBUtils.py` to match your local environment.

### 2. Installation

```bash
pip install selenium pytest pytest-html mysql-connector-python

```

### 3. Running Tests

To execute the entire suite and generate a report:

```bash
python Cal.py

```
