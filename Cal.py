import pytest
import os
import sys


def run_tests():
    # Get the directory where this script (Cal.py) is located
    base_dir = os.path.dirname(os.path.abspath(__file__))
    test_dir = os.path.join(base_dir, "Calculator")

    print(f"Starting Automation Suite in: {test_dir}")

    # Ensure the report is saved in the same directory as the script
    report_path = os.path.join(base_dir, "report.html")

    pytest.main([
        "-v",
        "-s",
        "-rf",
        "--tb=short",  # <--- Add this for cleaner error summaries
        test_dir,
        f"--html={report_path}",
        "--self-contained-html"
    ])


if __name__ == "__main__":
    run_tests()