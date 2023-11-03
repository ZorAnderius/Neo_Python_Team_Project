class Address:
    def __init__(self, text=""):
        self.set_address(text)

    def set_address(self, text):
        if text is not None:
            if not any(char.isalpha() for char in text):
                raise ValueError("Address must contain at least one alphabet character.")
        self.text = text

    def get_address(self):
        return self.text

    def serialize(self):
        return self.text

    def __str__(self):
        return self.text
