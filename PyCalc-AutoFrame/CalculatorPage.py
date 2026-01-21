from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = r"C:\Python_Projects\PyCalc-AutoFrame\WebApp\Calculator.html"
        self.n1_field = (By.ID, "num1")
        self.n2_field = (By.ID, "num2")
        self.btn_add = (By.XPATH, "//button[text()='+']")
        self.btn_sub = (By.XPATH, "//button[text()='−']")  # Check if this is '-' or '−'
        self.btn_mul = (By.XPATH, "//button[text()='×']")
        self.btn_div = (By.XPATH, "//button[text()='÷']")
        self.result_text = (By.ID, "current-result")
        # Initialize the wait once to use everywhere
        self.wait = WebDriverWait(self.driver, 10)

    def open(self):
        self.driver.get(self.url)

    def enter_numbers(self, n1, n2):
        el1 = self.wait.until(EC.element_to_be_clickable(self.n1_field))
        el1.clear()
        el1.send_keys(str(n1))

        el2 = self.wait.until(EC.element_to_be_clickable(self.n2_field))
        el2.clear()
        el2.send_keys(str(n2))

    def click_add(self):
        self.wait.until(EC.element_to_be_clickable(self.btn_add)).click()

    def click_subtract(self):
        self.wait.until(EC.element_to_be_clickable(self.btn_sub)).click()

    # ADD THESE TWO METHODS:
    def click_multiply(self):
        self.wait.until(EC.element_to_be_clickable(self.btn_mul)).click()

    def click_divide(self):
        self.wait.until(EC.element_to_be_clickable(self.btn_div)).click()

    def get_result_value(self):
        # Wait until the result element actually has text in it
        element = self.wait.until(EC.visibility_of_element_located(self.result_text))
        full_text = element.text

        if "=" in full_text:
            return full_text.split("=")[1].strip()
        return full_text