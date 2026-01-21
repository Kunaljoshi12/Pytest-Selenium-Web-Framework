from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


def User_input():
    try:
        # 1. Take user input and convert to float
        s = float(input("Enter number: "))

        # 2. Setup Selenium
        ser_obj = Service(r"C:\Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
        driver = webdriver.Chrome(service=ser_obj)
        driver.get("https://the-internet.herokuapp.com/inputs")
        driver.maximize_window()
        driver.implicitly_wait(5)

        # 3. Validation and Interaction
        # Since 's' is already a float from line 7, we know it's a number
        driver.find_element(By.XPATH, "//input[@type='number']").send_keys(str(s))

        print(f"Successfully entered: {s}")
        input("Press Enter to close browser...")
        driver.quit()

    except ValueError:
        print("Error: Please enter a valid numeric value.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# To run the function:
if __name__ == "__main__":
    User_input()