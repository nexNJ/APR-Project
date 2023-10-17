try:
    file= open("D:\Python problem\Python_ejudge\Problem ejudge\Problem 12\input.txt",'r')
    line = file.readlines()
    print(line)
except FileNotFoundError:
    print("1")
except Exception as e:
    print(type(e),e)
else:
    print("Closing file")
    file.close()
finally:
    print('good bye')