import os
os.chdir('D:\Python problem\Python_ejudge\Problem ejudge\Problem 12\\')




with open('input.txt','r') as rf:
    with open('output.txt','w') as wf:
        for i in rf:
            wf.write(i.capitalize())