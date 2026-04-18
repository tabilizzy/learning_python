class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

class User:
    count = 0
    @classmethod
    def increment_count(cls):
        cls.count += 1        