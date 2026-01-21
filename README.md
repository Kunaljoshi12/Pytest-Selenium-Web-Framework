# Selenium Python Automation Framework

This repository contains a hands-on implementation of **Python with Selenium for web automation testing**, covering both **core concepts and practical automation scenarios** typically used in professional QA environments.

---

## 🚀 Featured Projects

### 1. Hybrid Data-Driven Framework
**[Click here to view the Mini-Project: Hybrid Data-Driven Framework](./Hybrid_Data_Driven_Framework)**

This demonstrates a professional-grade framework that bridges the gap between Python automation and external data systems:
* **Multi-Source Data**: Retrieves test data from **Excel (.xlsx)** and **MySQL Databases**.
* **Controller Logic**: Centralized execution via `Input_box.py`.
* **Database Integration**: Real-time SQL queries for dynamic test data.

### 2. PyCalc-AutoFrame: Advanced Data-Driven Selenium Framework
**[Click here to view the Mini-Project: PyCalc-AutoFrame](./PyCalc-AutoFrame)**

#### 📌 Project Overview
PyCalc-AutoFrame is a professional-grade automation testing framework designed to validate web-based financial calculation logic. Built with **Python** and **Selenium**, it demonstrates industry-aligned QA standards by integrating a **MySQL database** for real-time test data management and **PyTest** for professional reporting.



#### 🚀 Key Technical Features
* **PyTest Integration**: Utilizes **Fixtures** for session-based browser management and **Parameterization** to run 80+ test scenarios dynamically.
* **Page Object Model (POM)**: Implements a clean separation between UI locators and test logic through a centralized `CalculatorPage` class.
* **Data-Driven Testing (DDT)**: Integrated with **MySQL** via `DBUtils` to fetch test data directly from the database.
* **Robust Synchronization**: Employs **Explicit Waits** (`WebDriverWait`) to handle dynamic UI states and edge cases like "Divide by Zero".
* **Professional Reporting**: Generates comprehensive **HTML and PDF reports** providing detailed pass/fail metrics for stakeholders.

#### 🛠️ Tech Stack
* **Language**: Python 3.13+
* **Automation**: Selenium WebDriver
* **Framework**: PyTest with HTML Reporting
* **Database**: MySQL
* **Reporting**: PyTest-HTML & Chrome PDF Print

#### 📁 Project Structure
The framework is organized into logical layers to ensure scalability and ease of maintenance:

```text
PyCalc-AutoFrame/
│
├── Cal.py                     # Main Runner (Entry Point to trigger PyTest)
├── conftest.py                # Global PyTest Fixtures (Driver setup & Teardown)
├── DBUtils.py                 # MySQL Database Utility (Connection & Data Fetching)
├── requirements.txt           # Project dependencies (Selenium, PyTest, etc.)
├── report.html                # Generated execution report (HTML version)
├── Automation_Report.pdf      # Generated execution report (PDF version)
│
├── Calculator/                # Test Layer Package
│   ├── test_addition.py       # Addition logic test suite
│   ├── test_subtraction.py    # Subtraction logic test suite
│   ├── test_multiplication.py # Multiplication logic test suite
│   └── test_division.py       # Division logic with error message validation
│
├── CalculatorPage.py          # Page Object Layer (Locators & UI Interactions)
│
└── WebApp/                    # Application Under Test (AUT)
    └── Calculator.html        # Local Web Calculator application

```
🔹 Project Focus
This repository emphasizes professional automation practices rather than isolated demo scripts. The implementation reflects industry-aligned QA automation standards.

🔹 Purpose
The purpose of this repository is to help recruiters and hiring managers evaluate proficiency in Python Selenium automation, organized code structure, and real-world data handling.

📌 Keywords
Selenium Python WebDriver QA Test Automation PyTest SQL Excel Automation Hybrid Framework Page Object Model Data-Driven Testing

