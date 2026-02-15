from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pages.add_remove_page import AddRemovePage
from config import CHROME_DRIVER_PATH

def run_automation():
    count = int(input("How many elements to cycle? "))

    # Setup
    service = Service(CHROME_DRIVER_PATH)
    driver = webdriver.Chrome(service=service)
    page = AddRemovePage(driver)

    try:
        page.open()
        driver.maximize_window()

        for i in range(count):
            page.add_element()
            print(f"Added iteration {i + 1}")

            page.remove_element()
            print(f"Removed iteration {i + 1}")

        # Verification step
        remaining = page.get_delete_button_count()
        print(f"Final check: {remaining} elements left on page.")

    except Exception as e:
        print(f"Automation failed: {e}")
    finally:
        driver.quit()


if __name__ == "__main__":
    run_automation()