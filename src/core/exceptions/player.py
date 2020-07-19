
class PlayerAlreadyExist(Exception):
    def __init__(self, message="Player already exist."):
        super().__init__(message)
