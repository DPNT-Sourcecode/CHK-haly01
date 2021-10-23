# noinspection PyShadowingBuiltins,PyUnusedLocal
def compute(int1, int2):
    try:
        if 0<=int1<=100 and 0<=int2<=100:
            val = int1+int2
            return val
        else:
            return f'Please enter positive integers between 0-100 instead of {int1} and {int2}'
    except:
        return f'Invalid parameters {int1} and {int2}'

