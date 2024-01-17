import allure
import unittest
import json
import csv
import os
import datetime
import allure


class TestRegression(unittest.TestCase):
    def setUp(self):
        # Loaded data from files
        self.soft_assertions = {}
        self.v1_data = {}
        self.v2_data = []
        script_directory = os.path.dirname(os.path.abspath(__file__))
        v1_directory = os.path.join(script_directory, 'v3')
        fds_v1 = sorted(os.listdir(v1_directory))

        # Loaded V1 data
        for failic_v1 in fds_v1:
            with open(os.path.join(v1_directory, failic_v1), 'r') as file:
                file_data = json.load(file)
                identifier = os.path.splitext(failic_v1)[0]
                self.v1_data[identifier] = file_data

        # Loaded V2 data
        v2_directory = os.path.join(script_directory, 'v4')
        fds_v2 = sorted(os.listdir(v2_directory))
        for failic_v2 in fds_v2:
            with open(os.path.join(v2_directory, failic_v2), 'r') as file:
                self.v2_data.append(list(csv.reader(file)))

    def soft_assert(self, identifier, condition, message):
        """Added a soft assertion."""
        if identifier not in self.soft_assertions:
            self.soft_assertions[identifier] = []
        try:
            assert condition
        except AssertionError as e:
            self.soft_assertions[identifier].append((False, message))

    @allure.testcase("Test Case 1")
    @allure.feature("V1 Data Loading")
    @allure.step("Step 1: Perform V1 Data Loading")
    def test_v1_data_loading(self):
        for identifier, data in self.v1_data.items():
            self.assertIsNotNone(data, f"Failed to load V1 data for {identifier}")
            allure.attach(self.take_screenshot(), name=f"{identifier}_success_screenshot", attachment_type=allure.attachment_type.PNG)


            # Additional tests for data type, null values, and missing values
            for v1_date, v1_observation in data.items():
                for v1_d, v1_val in v1_observation.items():
                    self.assertTrue(isinstance(v1_date, str), "As Of date should be a string")
                    self.assertTrue(isinstance(v1_d, str), "Observation date should be a string")
                    allure.attach(self.take_screenshot(), name=f"{identifier}_success_screenshot", attachment_type=allure.attachment_type.PNG)
              #      self.assertTrue(isinstance(v1_val, (float, int)), "Observation value should be a numeric type")
              #      self.assertIsNotNone(v1_val, "Observation value should not be null")

    @allure.testcase("Test Case 2")
    @allure.feature("V2 Data Loading")
    @allure.step("Step 2: Perform V2 Data Loading")
    def test_v2_data_loading(self):
        self.assertIsNotNone(self.v2_data, "Failed to load V2 data")
        allure.attach(self.take_screenshot(), name=f"V2 Data Loading_success_screenshot", attachment_type=allure.attachment_type.PNG)

        # Additional tests for data type, null values, and missing values
        for row in self.v2_data:
            for every_item in row:
                self.assertTrue(isinstance(every_item[0], str), "Observation date should be a string")
                self.assertTrue(isinstance(every_item[2], str), "Observation value should be a numeric type")
                self.assertIsNotNone(every_item[2], "Observation value should not be null")

    @allure.testcase("Test Case 3")
    @allure.feature("Regression Test")
    @allure.step("Step 3: Perform Regression Test")
    def test_regression_between_v1_and_v2(self):
        # Compared V1 and V2 responses
        for identifier, v1_values in self.v1_data.items():
            for v1_date, v1_observation in v1_values.items():
                for v1_d, v1_val in v1_observation.items():
                    v1_timestamp = v1_d.replace('T', ' ').replace('Z', '')
                    date_format = datetime.datetime.strptime(v1_timestamp, "%Y-%m-%d %H:%M:%S")
                    v1_observation_date_unix_time = datetime.datetime.timestamp(date_format)
                    v1_value = v1_val

                # Finded corresponding V2 data based on observation date
                for row in self.v2_data:
                    for every_item in row:
                        v2_observation_date = every_item[0]
                        v2_value = float(every_item[2])
                        if float(v2_observation_date) == v1_observation_date_unix_time:
                            self.soft_assert(identifier, abs(v1_value - v2_value) < 0.01, "Values do not match")

    # Checked all soft assertions and fail the test if any failed
        for identifier, assertions in self.soft_assertions.items():
            for condition, message in assertions:
                self.assertTrue(condition, f"{identifier}: {message}")

if __name__ == '__main__':
    unittest.main()
