Hybrid Data-Driven Automation Framework
This repository contains a Hybrid Data-Driven Framework designed for automated web testing using Python and Selenium WebDriver. The framework demonstrates the ability to drive test execution by retrieving data from three distinct sources: MySQL Databases, Excel Spreadsheets, and Manual User Input.

🚀 Framework Architecture
The project is structured to separate data retrieval logic from the main execution controller, ensuring modularity and scalability.

Core Components
Controller (Input_box.py): Acts as the main entry point, allowing the user to select the data source via a match-case menu.

Database Engine (Database_1.py & .sql): Manages connectivity to MySQL using mysql.connector to fetch test parameters dynamically from a relational database.

Excel Engine (Read_Excel.py): Utilizes openpyxl to parse .xlsx files, locating specific data by column headers (e.g., "ID").

Manual Engine (User_Input.py): Provides a fallback for ad-hoc testing where data is entered directly via the terminal.

🛠️ Technical Stack
Language: Python

Automation Tool: Selenium WebDriver

Database: MySQL

Libraries:

mysql-connector-python (Database connectivity)

openpyxl (Excel manipulation)

selenium (Web browser automation)

📋 Features
Multi-Source Data Handling: Seamlessly switch between SQL, Excel, and console input for test data.

Robust Error Handling: Includes try-except blocks to manage database connection errors and invalid user inputs.

Dynamic Element Interaction: Automatically launches Chrome and interacts with numeric input fields on a live test site (the-internet.herokuapp.com).

Synchronization: Implements implicit waits to ensure reliable element location during page loads.

⚙️ Setup and Configuration
Database Setup: Execute the Data_Base.sql script in your MySQL environment to create the data_1 database and the input table.

Driver Configuration: Update the Service path in all Python files to point to your local chromedriver.exe location.

Excel Path: Ensure the file path in Read_Excel.py points to your Data.xlsx file.

Database Credentials: Update the connection parameters in Database_1.py (host, user, password) to match your local setup.
