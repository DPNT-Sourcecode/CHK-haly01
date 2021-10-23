
def sum(param):
    try:
        if 0<=param[0]<=100 and 0<=param[0]<=100:
            val = param[0]+param[1]
            return val
        else:
            return f'Please enter positive integers between 0-100 instead of {param[0]} and {param[1]}'
    except:
        return f'Invalid parameters {param[0]} and {param[1]}'

def main():
    param = [21,99]
    print(sum(param[0], param[1]))


if __name__ == "__main__":
    main()
