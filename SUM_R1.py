
def sum(int1, int2):
    try:
        if 0<=int1<=100 and 0<=int2<=100:
            val = int1+int2
            return val
        else:
            return f'Please enter positive integers between 0-100 instead of {int1} and {int2}'
    except:
        return f'Invalid parameters {int1} and {int2}'

def main():
    param = [21,99]
    print(sum(param[0], param[1]))


if __name__ == "__main__":
    main()