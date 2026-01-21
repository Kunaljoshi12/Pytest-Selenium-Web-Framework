import pytest
from DBUtils import fetch_test_cases
from CalculatorPage import CalculatorPage


@pytest.mark.parametrize("n1, n2", fetch_test_cases())
def test_subtraction(driver, n1, n2):
    calc = CalculatorPage(driver)
    calc.open()
    calc.enter_numbers(n1, n2)
    calc.click_subtract()

    # Apply the same logic as addition
    res = round(float(n1) - float(n2), 2)
    expected = str(int(res) if res % 1 == 0 else res)

    assert calc.get_result_value() == expected