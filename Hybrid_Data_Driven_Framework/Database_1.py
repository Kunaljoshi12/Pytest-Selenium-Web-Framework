import mysql.connector
from mysql.connector import Error
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


def Read_Database(search_id=123):  # Set a default ID here
    test_id_variable = None
    try:
        con = mysql.connector.connect(
            host="localhost",
            port=3306,
            user="root",
            password="Pass@1234kj",
            database="data_1"
        )

        if con.is_connected():
            cursor = con.cursor()
            query = "SELECT id FROM input WHERE id = %s"
            cursor.execute(query, (search_id,))
            row = cursor.fetchone()

            if row:
                test_id_variable = row[0]
            else:
                print(f"Test Data Error: ID {search_id} not found.")

            cursor.close()
            con.close()
    except Error as e:
        print("Database connection error:", e)
        return None

    if test_id_variable is not None:
        print(f"Retrieved ID {test_id_variable} - Starting Selenium...")
        try:
            ser_obj = Service(r"C:\Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
            driver = webdriver.Chrome(service=ser_obj)
            driver.get("https://the-internet.herokuapp.com/inputs")
            driver.maximize_window()
            driver.implicitly_wait(5)

            if isinstance(test_id_variable, (int, float)):
                driver.find_element(By.XPATH, "//input[@type='number']").send_keys(str(test_id_variable))

            input("Press Enter to close the browser...")
            driver.quit()
            return test_id_variable

        except Exception as e:
            print("Selenium Error:", e)
            return None
    return None