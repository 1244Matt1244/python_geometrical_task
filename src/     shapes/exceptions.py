# In exceptions.py
class InvalidDimensionError(ValueError):
    def __init__(self, message: str) -> None:
        super().__init__(message)
