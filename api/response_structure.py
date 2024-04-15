

class ResponseStructure:
    def __int__(self, case_id, response_code, email_classification, response_email_object):
        self.case_id = case_id
        self.response_code = response_code
        self.email_classification = email_classification
        self.response_email_object = response_email_object

    def to_json(self) -> dict:
        return {
            'case_id': self.case_id,
            'response_code': self.response_code,
            'email_classification': self.email_classification,
            'response_email_object': self.response_email_object
        }



