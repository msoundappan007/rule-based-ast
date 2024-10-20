

import unittest
from unittest.mock import patch
import requests
from app.schemas.rule_schema import RuleCreate, RuleEvaluate, RuleCombine


class TestRuleEngineAPI(unittest.TestCase):
    BASE_URL = "http://127.0.0.1:8000"

    @patch('requests.post')
    def test_create_rule(self, mock_post):
        # Mock response data
        mock_response = {
            "id": 1,
            "message": "Rule created successfully."
        }
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = mock_response

        rule_data = {"rule_string": "(age > 30 AND department = 'Sales')"}
        rule_create = RuleCreate(**rule_data)  # Create an instance of RuleCreate
        # Simulate the API call
        response = requests.post(f"{self.BASE_URL}/api/rules/create", json=rule_data)
        
        self.assertEqual(response.json()['id'], 1)  # Assert the returned rule ID is correct
        mock_post.assert_called_once_with(f"{self.BASE_URL}/api/rules/create", json=rule_data)

    @patch('requests.post')
    def test_combine_rules(self, mock_post):
        # Mock response data
        mock_response = {
            "id": 2,
            "message": "Rules combined successfully."
        }
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = mock_response

        rule_ids = [1, 2]
        rule_combine = RuleCombine(rule_ids=rule_ids)  # Create an instance of RuleCombine
        # Simulate the API call
        response = requests.post(f"{self.BASE_URL}/api/rules/combine", json=rule_ids)

        self.assertEqual(response.json()['id'], 2)  # Assert the returned combined rule ID is correct
        mock_post.assert_called_once_with(f"{self.BASE_URL}/api/rules/combine", json=rule_ids)

    @patch('requests.post')
    def test_evaluate_rule(self, mock_post):
        # Mock response data
        mock_response = {
            "result": True,
            "message": "Evaluation successful."
        }
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = mock_response

        rule_id = 1
        data = {
            "age": 35,
            "department": "Sales",
            "salary": 60000,
            "experience": 6
        }
        rule_evaluate = RuleEvaluate(rule_id=rule_id, data=data)  # Create an instance of RuleEvaluate
        # Simulate the API call
        response = requests.post(f"{self.BASE_URL}/api/rules/evaluate", json={"rule_id": rule_id, "data": data})

        self.assertTrue(response.json()['result'])  # Assert the evaluation result is correct
        mock_post.assert_called_once_with(f"{self.BASE_URL}/api/rules/evaluate", json={"rule_id": rule_id, "data": data})


if __name__ == "__main__":
    unittest.main()


