from sublist_sort import *
import json

def import_data():
    with open("tests.json", "r") as f:
        return json.load(f)

def test_main():
    data = import_data()

    # Go through each test case
    for item in data:
        # Try executing case
        try:
            sorted = main(item["input"])
            if not item["expectedFail"]:
                assert(sorted == item["output"])
            else:
                assert False, f"Fail - data not sorted correctly. Got {sorted}, expected {item["output"]}"
        except Exception as e:
            if item["expectedFail"]:
                assert True
            else:
                assert False, f"Fail - encountered an error {e}. Expected {item["output"]}"