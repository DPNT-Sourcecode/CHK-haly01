
def addInt(param):
    try:
        if 0<=param[0]<=100 and 0<=param[0]<=100:
            val = param[0]+param[1]
            return val
        else:
            return 'Please enter positive integers between 0-100'
    except:
        return f'Invalid parameters {param[0]} and {param[1]}'

def main():
    print(addInt([210, 99]))
    

if __name__ == "__main__":
    main()
