# Hybrid Data-Driven Automation Framework

A modular Python-based automation framework designed for flexible web testing. This project leverages **Selenium WebDriver** to execute test cases using data dynamically retrieved from three different sources: MySQL databases, Excel files, and direct terminal input.

## 🚀 Framework Architecture

The framework is built with a decoupled architecture, separating data acquisition from test execution logic to ensure modularity and scalability.

### Core Components

* **Controller (`Input_box.py`):** The central entry point. It uses a `match-case` menu to route execution based on the user's chosen data source.
* **Database Engine (`Database_1.py`):** Manages connectivity to MySQL using `mysql-connector-python` to fetch test parameters dynamically.
* **Excel Engine (`Read_Excel.py`):** Utilizes `openpyxl` to parse `.xlsx` files and map data to specific test cases based on column headers.
* **Manual Engine (`User_Input.py`):** Provides a fallback module for ad-hoc or exploratory testing via manual terminal input.

---

## 🛠️ Technical Stack

| Component | Technology |
| --- | --- |
| **Language** | Python 3.x |
| **Automation** | Selenium WebDriver |
| **Database** | MySQL |
| **Libraries** | `mysql-connector-python`, `openpyxl`, `selenium` |

---

## 📋 Key Features

* **Multi-Source Data Handling:** Seamlessly switch between SQL, Excel, and console input without modifying the core test scripts.
* **Dynamic Web Interaction:** Automatically targets [the-internet.herokuapp.com](https://the-internet.herokuapp.com/inputs) to validate numeric input fields.
* **Robust Error Handling:** Includes `try-except` blocks to manage database connection errors and invalid user inputs.
* **Synchronization:** Implements implicit waits to ensure reliable element location during page loads.

---

## ⚙️ Setup and Configuration

### 1. Database Setup

* Execute the `Data_Base.sql` script in your MySQL environment to create the `data_1` database and the `input` table.
* Update the connection parameters (host, user, password) in `Database_1.py` to match your local MySQL configuration.

### 2. File Paths

* **Excel:** Ensure your test data is populated in `Data.xlsx` and the file path in `Read_Excel.py` is correct.
* **Driver:** Update the `Service` path in all Python files to point to your local `chromedriver.exe` location.

### 3. Install Dependencies

Run the following command to install the required libraries:

```bash
pip install selenium mysql-connector-python openpyxl

```

---

## 📂 Project Structure

```text
Hybrid_Data_Driven_Framework/
├── Database_1.py       # SQL Data Retrieval Logic
├── Data_Base.sql       # Database Schema Script
├── Input_box.py        # Main Controller (Execution Entry)
├── Read_Excel.py       # Excel Data Retrieval Logic
├── User_Input.py       # Manual Data Input Logic
└── Data.xlsx           # Sample Test Data

```

## 🔍 How to Run

1. Navigate to the project directory.
2. Run the controller script:
```bash
python Input_box.py

```
