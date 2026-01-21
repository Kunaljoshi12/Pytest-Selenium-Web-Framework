import pytest
from DBUtils import fetch_test_cases
from CalculatorPage import CalculatorPage


@pytest.mark.parametrize("n1, n2", fetch_test_cases())
def test_division(driver, n1, n2):
    if n2 == 0:
        pytest.skip("Skipping division by zero")

    calc = CalculatorPage(driver)
    calc.open()
    calc.enter_numbers(n1, n2)
    calc.click_divide()

    # Logic to match JavaScript's number formatting (removes .0 from whole numbers)
    res = round(n1 / n2, 2)
    expected = str(int(res) if res % 1 == 0 else res)

    assert calc.get_result_value() == expected