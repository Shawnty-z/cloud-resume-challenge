import unittest
from unittest.mock import patch, MagicMock
import app  # This should match your Lambda function file name

class TestLambdaFunction(unittest.TestCase):
    
    @patch('app.dynamodb.Table')
    def test_lambda_handler_increment_count(self, mock_dynamodb_table):
        # Mock the get_item response to simulate a DynamoDB get request
        mock_table_instance = mock_dynamodb_table.return_value
        mock_table_instance.get_item.return_value = {'Item': {'Count': 10}}

        # Call the lambda handler function
        event = {}  # Mock event data
        context = {}  # Mock context
        response = app.lambda_handler(event, context)

        # Verify the count is incremented
        self.assertEqual(response['statusCode'], 200)
        self.assertIn('"count": 11', response['body'])

        # Verify that DynamoDB put_item was called with the incremented count
        mock_table_instance.put_item.assert_called_with(
            Item={'ID': 'visitors', 'Count': 11}
        )

if __name__ == '__main__':
    unittest.main()
