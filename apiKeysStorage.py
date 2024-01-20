import random

class ApiKeys:
    def __init__(self, keys: list):
        """
        Initialize the rotator with a variable number of API keys.
        :param keys: A variable number of API keys.
        """
        self.keys = list(keys)
        self.index = random.randint(0, len(keys) - 1) if keys else 0

    def get(self):
        """
        Returns the next API key in the rotation.
        :return: An API key.
        """
        if not self.keys:
            raise ValueError("No API keys available.")

        key = self.keys[self.index]
        self.index = (self.index + 1) % len(self.keys)
        return key

if __name__ == "__main__":
    rotator = ApiKeys("key1", "key2", "key3")
    print(rotator.get())
    print(rotator.get())
    print(rotator.get())
    print(rotator.get()) 