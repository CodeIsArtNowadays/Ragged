class AuthRequireException(Exception):
    def __init__(self):
        super().__init__('Authentication Require')