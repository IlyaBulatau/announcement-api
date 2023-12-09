class InvalidInput(Exception):
    """
    Invalid input for query argument during query to database 
    """
    def __init__(self, error: str | None = None):
        self.error = error