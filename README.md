# Pytest-Selenium Web Automation Frameworks

Welcome to the central repository for my Selenium-based automation frameworks. This project serves as a comprehensive portfolio demonstrating various design patterns in Python-based web testing, ranging from Hybrid Data-Driven models to Page Object Model (POM) architectures.

## 📂 Project Portfolio

Each directory below contains a specialized framework designed for specific automation challenges.

| Project Name | Framework Type | Key Technologies | Link |
| --- | --- | --- | --- |

| **Hybrid Data-Driven** | Hybrid Framework | Selenium, Excel, MySQL | [View Project](https://github.com/Kunaljoshi12/Pytest-Selenium-Web-Framework/tree/main/Hybrid_Data_Driven_Framework) |
| **PyCalc-AutoFrame** | Page Object Model (POM) | Pytest, Selenium, MySQL | [View Project](https://github.com/Kunaljoshi12/Pytest-Selenium-Web-Framework/tree/main/PyCalc-AutoFrame) |
---

## 🏗️ Core Architecture Overview

Most projects in this repository follow a standardized automation lifecycle to ensure reliability and maintainability:

1. **Configuration:** Global fixtures and WebDriver settings managed via `conftest.py`.
2. **Data Layer:** Externalized test data using SQL databases or Excel spreadsheets.
3. **Page Objects:** UI elements and interactions isolated into dedicated classes.
4. **Reporting:** Detailed HTML reports generated after every execution.

---

## 🛠️ Global Requirements

To run any of the projects within this repository, ensure you have the following installed:

* **Python:** 3.10 or higher
* **Browser Driver:** [ChromeDriver](https://www.google.com/search?q=https://googlechromelabs.github.io/chrome-for-testing/) (matching your local Chrome version)
* **Key Libraries:**
```bash
pip install selenium pytest pytest-html mysql-connector-python openpyxl
```
---
## 📝 Author
**Kunal Joshi** [GitHub Profile](https://www.google.com/search?q=https://github.com/Kunaljoshi12)
---
