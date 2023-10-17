
try:
    x = float(input())
    try:
        y = float(input())
    except:
        print('ERROR: Invalid input')
    finally:
        print(x+y)
except:
    print('ERROR: Invalid input')
