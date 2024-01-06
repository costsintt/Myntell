class APIKeyRotator:
    def __init__(self, keys):
        """
        Initialize the rotator with a variable number of API keys.
        :param keys: A variable number of API keys.
        """
        self.keys = list(keys)
        self.index = 0

    def get_next(self):
        """
        Returns the next API key in the rotation.
        :return: An API key.
        """
        if not self.keys:
            raise ValueError("No API keys available.")

        # Get the next key and update the index
        key = self.keys[self.index]
        self.index = (self.index + 1) % len(self.keys)
        return key

if __name__ == "__main__":
    rotator = APIKeyRotator("key1", "key2", "key3")
    print(rotator.get_next())
    print(rotator.get_next())
    print(rotator.get_next())
    print(rotator.get_next()) 