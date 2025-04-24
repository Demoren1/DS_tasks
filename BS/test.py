class ShizoBool:
    def __init__(self, value):
        self.value = value
    def __bool__(self):
        return self.value
    def __eq__(self, other):
        if isinstance(other, ShizoBool):
            return self.value == other.value
        return self.value == other


if (x == 1):
    print("hi")