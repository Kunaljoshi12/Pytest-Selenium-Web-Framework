import pytest
from DBUtils import fetch_test_cases
from CalculatorPage import CalculatorPage


@pytest.mark.parametrize("n1, n2", fetch_test_cases())
def test_addition(driver, n1, n2):
    calc = CalculatorPage(driver)
    calc.open()
    calc.enter_numbers(n1, n2)
    calc.click_add()

    # 1. Calculate the raw result
    res = round(float(n1) + float(n2), 2)

    # 2. Logic: If it's a whole number (like 378.0), make it "378"
    #    If it's a decimal (like 15.5), keep it "15.5"
    expected = str(int(res) if res % 1 == 0 else res)

    assert calc.get_result_value() == expected