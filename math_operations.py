class MathOperations:

    @staticmethod
    def addition(*args):
        result = 0
        for arg in args:
            result += arg
        return result
