from random import randint


class Utility:
    @staticmethod
    def gen_code(n=12):
        code = "T-"
        for i in range(n):
            code += str(randint(0, 10))

        return code
