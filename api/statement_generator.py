from flask import request
from api.response_structure import ResponseStructure
from enum import Enum


class EmailClassifier(Enum):

    STATEMENT_REQUEST = "Statement Request"
    NO_STATEMENT_REQUEST = "No Request"


class StatementGenerator:
    def generate_statement_payload(self):
        payload = request.get_json(force=True)
        case_id = payload['case_id']
        response_code = payload['response_code']
        email_classification = payload['email_classification']
        response_email_object = payload['response_email_object']

        response_structure = ResponseStructure()
        response_structure.case_id = case_id
        response_structure.response_code = response_code
        response_structure.email_classification = email_classification
        response_structure.response_email_object = response_email_object

        response = {}

        if response_structure.email_classification == EmailClassifier.NO_STATEMENT_REQUEST.value:
            response = {
                'classification_result': EmailClassifier.NO_STATEMENT_REQUEST.value,
                'response_code': '200',
                'response_message': 'Successful'
            }
        elif response_structure.email_classification == EmailClassifier.STATEMENT_REQUEST.value:
            response = {
                'classification_result': EmailClassifier.STATEMENT_REQUEST.value,
                'parameters': {
                    'account_number': 123456789,
                    'date_range': 'march 2024'
                }
            }

        print(response_structure.to_json())

        return response
