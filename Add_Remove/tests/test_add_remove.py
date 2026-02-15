# tests/test_add_remove.py
import pytest
from pages.add_remove_page import AddRemovePage


def test_add_remove_elements_cycle(driver):
    page = AddRemovePage(driver)
    page.open()

    iterations = 3
    for i in range(iterations):
        page.add_element()
        page.remove_element()

    remaining = page.get_delete_button_count()
    assert remaining == 0, f"Failure: Expected 0 elements, but found {remaining}"


# NEW TEST: Add multiple elements
def test_add_multiple_elements(driver):
    page = AddRemovePage(driver)
    page.open()

    # Add 5 elements
    for _ in range(5):
        page.add_element()

    count = page.get_delete_button_count()
    assert count == 5, f"Expected 5 elements, found {count}"


# NEW TEST: Remove all elements
def test_remove_all_elements(driver):
    page = AddRemovePage(driver)
    page.open()

    # Add 3 elements
    for _ in range(3):
        page.add_element()

    # Remove all
    while page.get_delete_button_count() > 0:
        page.remove_element()

    assert page.get_delete_button_count() == 0