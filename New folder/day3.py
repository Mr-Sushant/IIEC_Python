import os

print("Enter your choice",end=' ')
ch = input()
if (ch == 1):
    os.system("chrome")
elif (ch == 2):
    os.system("notepad")
else:
    os.system("chrome google.com")
