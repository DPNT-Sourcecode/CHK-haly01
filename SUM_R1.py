
def addInt(param):
    try:
        val = param[0]+param[1]
        return val
    except:
        return f'Invalid parameters {param[0]} and {param[1]}'



def main():
    print(addInt([21, 99]))
    
    

if __name__ == "__main__":
    main()