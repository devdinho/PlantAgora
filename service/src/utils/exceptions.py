from rest_framework.exceptions import APIException


class SimpleDetailError(APIException):
    status_code = 400
    default_detail = "A validation error occurred."
    default_code = "invalid"

    def __init__(self, detail):
        self.detail = {"detail": detail}
