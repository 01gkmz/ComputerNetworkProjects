from enum import Enum

class TestErrorCode(Enum):
    TEST_ERROR_NONE = 0
    TEST_ERROR_HTTP_CONNECT_FAILED = 1
    TEST_ERROR_HTTP_SEND_FAILED = 2
    TEST_ERROR_PARSE_PARTIAL = 3
    TEST_ERROR_PARSE_FAILED = 4
