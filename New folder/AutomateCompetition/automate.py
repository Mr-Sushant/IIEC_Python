import os
import pyttsx3 as pt
import smtplib
import time
import sys
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from getpass import getpass as gp
from random import randint as rand
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import sys


pt.speak("Welcome "+os.getenv('username'))
pt.speak("How may I help you ?")


while(True):
    x = input("What do you want : ")
    
    if(("run" in x or "open" in x) and ("notepad" in x or "editor" in x)):
        os.system("notepad")
        
    elif(("run" in x or "open" in x) and ("calculator" in x or "calc" in x)):
        os.system("calc")
        
    elif(("run" in x or "open" in x) and ("camera" in x)):
        os.system("start microsoft.windows.camera:")
        
    elif("send" in x and "mail" in x):
        #The mail addresses and password
        sender_address = input("Enter your mail: ")
        sender_pass = gp("Enter your password : ")
        receiver_address = input("Enter reciever address : ")
        #Setup the MIME
        message = MIMEMultipart()
        message['From'] = sender_address
        message['To'] = receiver_address
        message['Subject'] = input("Enter Subject : ")   #The subject line
        #The body and the attachments for the mail
        mail_content = input("Enter Body of Mail : ")
        message.attach(MIMEText(mail_content, 'plain'))
        #Create SMTP session for sending the mail
        session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
        session.starttls() #enable security
        session.login(sender_address, sender_pass) #login with mail_id and password
        text = message.as_string()
        session.sendmail(sender_address, receiver_address, text)
        session.quit()
        pt.speak('Mail Sent')
        
        
    elif("open" in x and ("youtube" in x or "utube" in x)):
        os.system("chrome youtube.com")
        
        
    elif("open" in x and ("songs" in x or "music" in x)):
        os.system("chrome gaana.com")
        
        
    elif(("open" in x or "run" in x) and ("store" in x or "microsoft store" in x)):
        os.system("start ms-windows-store:")
        
        
    elif(("open" in x or "run" in x or "execute" in x) and ("vscode" in x or "code" in x)):
        os.system("code")
        
        
    elif("open" in x and ("facebook" in x or "fb" in x)):
        os.system("chrome facebook.com")
        
        
    elif("time" in x and "what" in x ):
        os.system("time")
        
        
    elif("go to" in x):
        dir = input("Enter directory : ")
        os.system("cd "+dir)
        
        
    elif("shutdown" in x or "close pc" in x or "turn off" in x):
        os.system("shutdown/i")
        
        
    elif("open" in x and "bash" in x):
        os.system("bash")
        
        
    elif("open" in x and "netflix" in x):
        os.system("chrome netflix.com")
        
        
    elif(("do" in x or "go to" in x) and ("shopping" in x or "shop" in x)):
        os.system("chrome amazon.in")
        
        
    elif("open" in x and "whatsapp"):
        os.system("chrome web.whatsapp.com")
        
        
    elif(("watch" in x or "play" in x) and ("star wars" in x)):
        os.system("telnet towel.blinkenlights.nl")
        
    elif(("start" in x or "open" in x) and ("timer" in x or "watch in x")):
        print("Enter time in seconds: " , end = '')
        sec = input()
        print("Time Remaining")
        t = int(sec)
        print()
        while t>=0 :
          print(t, end=" \r")
          time.sleep(1)
          t=t-1
        pt.speak("Time Over")
        
    elif ((("play" in x)  or ("start" in x )) and ("quiz" in x)):
        print("\n\n\n")
        print("****Welcome to my Quiz game****")
        print()
        print("You Have 4 categories to choose from : ")
        print()
        print()
        print("Choose one category and you will have to answer 5 questions")
        print()
        print("1 marks for correct answer and 0 for wrong")
        print()
        print("Are you ready!")
        print()
        print("Press any key to start")
        print()
        print("Press 0 or type exit to quit the game")
        print()
        
        start_game = input()
        if (start_game == "exit" ) or (start_game == "0") or (start_game == "quit") : 
          os.system("exit()")
        else : 
            
        
          print("1. C")
          print("2. C++")
          print("3. Python")
          print("4. Java")
          choice = input()
          if choice == "1" : 
            total =0
            q = 1
            os.system("cls")
            print("Question 1 :" , end = '')
            print("\tWhich of the following statement can be used to free the allocated memory?")
            print("A - remove(var-name);")
            print("B - free(var-name);")
            print("C - vanish(var-name);")
            print("D - erase(var-name);")
            ans = input()
            if ans == "B" or ans == "b" :
                total=total+1
            if (ans == "exit" ) or (ans == "0") or (ans == "quit") : 
                os.system("exit()")
            else :
                print("Wrong answer")
        
            os.system("cls")
            print("Question 2 :" , end = '')
            print("\tThe library function strrchr() finds the first occurrence of a substring in another string.")
            print("A - Yes")
            print("B - Strstr()")
            print("C - strchr()")
            print("D - strnset()")
            ans = input()
            if ans == "B" or ans == "b" :
                total=total+1
            if (ans == "exit" ) or (ans == "0") or (ans == "quit") : 
                os.system("exit()")
            else :
                print("Wrong answer")
            os.system("cls")
            print("Question 3 :" , end = '')
            print("\tWhich of the following has a global scope in the program?")
            print("A - Formal parameters")
            print("B - Constants")
            print("C - Macros")
            print("D - Local variables")
            ans = input()
            if ans == "C" or ans == "c" :
                total=total+1
            if (ans == "exit" ) or (ans == "0") or (ans == "quit") : 
                os.system("exit()")
            else :
                print("Wrong answer")
            os.system("cls")
            print("Question 4 :" , end = '')
            print("\tWhich of the following statements about functions is false?")
            print("A - The main() function can be called recursively")
            print("B - Functions cannot return more than one value at a time")
            print("C - A function can have multiple return statements with different return values")
            print("D - The maximum number of arguments a function can take is 128")
            ans = input()
            if ans == "B" or ans == "b" :
                total=total+1
            if (ans == "exit" ) or (ans == "0") or (ans == "quit") : 
                os.system("exit()")
            else :
                print("Wrong answer")
            os.system("cls")
            print("Question 5 :" , end = '')
            print("\tFor using ceil() function, which header file needs to be included?")
            print("A - string.h")
            print("B - stdlib.h")
            print("C - math.h")
            print("D - stderr.h")
            ans = input()
            if ans == "C" or ans == "c" :
                total=total+1
            if (ans == "exit" ) or (ans == "0") or (ans == "quit") : 
                os.system("exit()")
            else :
                print("Wrong answer")
            print("Total Marks:" , end = '')
            print(total)
            
        
          elif choice == "2" : 
            total =0
            q = 1
            os.system("cls")
            print("Question 1 :" , end = '')
            print("\tChoose the operator which cannot be overloaded.")
            print("A - /")
            print("B - ()")
            print("C - ::")
            print("D - %")
            ans = input()
            if ans == "C" or ans == "c" :
                total=total+1
            if (ans == "exit" ) or (ans == "0") or (ans == "quit") : 
                os.system("exit()")
            else :
                print("Wrong answer")
            os.system("cls")
            print("Question 2 :" , end = '')
            print("\t‘cin’ is an __")
            print("A - class")
            print("B - object")
            print("C - package")
            print("D - namespace")
            ans = input()
            if ans == "B" or ans == "b" :
                total=total+1
            if (ans == "exit" ) or (ans == "0") or (ans == "quit") : 
                os.system("exit()")
            else :
                print("Wrong answer")
            os.system("cls")
            print("Question 3 :" , end = '')
            print("\tHow many number of arguments can a destructor of a class receives?")
            print("A - 0")
            print("B - 1")
            print("C - 2")
            print("D - None of the above")
            ans = input()
            if ans == "A" or ans == "a" :
                total=total+1
            if (ans == "exit" ) or (ans == "0") or (ans == "quit") : 
                os.system("exit()")
            else :
                print("Wrong answer")
            os.system("cls")
            print("Question 4 :" , end = '')
            print("\tAn array can be passed to the function with call by value mechanism.")
            print("A - True")
            print("B - False")
            ans = input()
            if ans == "B" or ans == "b" :
                total=total+1
            if (ans == "exit" ) or (ans == "0") or (ans == "quit") : 
                os.system("exit()")
            else :
                print("Wrong answer")
            os.system("cls")
            print("Question 5 :" , end = '')
            print("\tThe default executable generation on UNIX for a C++ program is ___")
            print("A - a.exe")
            print("B - a")
            print("C - a.out")
            print("D - out.a")
            ans = input()
            if ans == "C" or ans == "c" :
                total=total+1
            if (ans == "exit" ) or (ans == "0") or (ans == "quit") : 
                os.system("exit()")
            else :
                print("Wrong answer")
            print("Total Marks:" , end = '')
            print(total)
        
          elif choice == "3" : 
            total =0
            q = 1
            os.system("cls")
            print("Question 1 :" , end = '')
            print("\t Which operator is right-associative")
            print("A - *")
            print("B - =")
            print("C - +")
            print("D - %")
            ans = input()
            if ans == "B" or ans == "b" :
                total=total+1
            if (ans == "exit" ) or (ans == "0") or (ans == "quit") : 
                os.system("exit()")
            else :
                print("Wrong answer")
            os.system("cls")
            print("Question 2 :" , end = '')
            print("\tWhat is output for − min(''hello world'')")
            print("A - e")
            print("B - a blank space character")
            print("C - w")
            print("D - none of the above")
            ans = input()
            if ans == "B" or ans == "b" :
                total=total+1
            if (ans == "exit" ) or (ans == "0") or (ans == "quit") : 
                os.system("exit()")
            else :
                print("Wrong answer")
            os.system("cls")
            print("Question 3 :" , end = '')
            print("\tWhich module is used in python to create Graphics?")
            print("A - Turtle")
            print("B - Canvas")
            print("C - Tkinter")
            print("D - Graphics")
            ans = input()
            if ans == "A" or ans == "a" :
                total=total+1
            if (ans == "exit" ) or (ans == "0") or (ans == "quit") : 
                os.system("exit()")
            else :
                print("Wrong answer")
            os.system("cls")
            print("Question 4 :" , end = '')
            print("\tWhich way among them is used to create an event loop ?")
            print("A - Window.eventloop()")
            print("B - Window.mainloop()")
            ans = input()
            if ans == "B" or ans == "b" :
                total=total+1
            if (ans == "exit" ) or (ans == "0") or (ans == "quit") : 
                os.system("exit()")
            else :
                print("Wrong answer")
            os.system("cls")
            print("Question 5 :" , end = '')
            print("\tWhich function can be used on the file to display a dialog for saving a file?")
            print("A - Filename = savefilename()")
            print("B - Filename = asksavefilename()")
            print("C - Fielname = asksaveasfilename()")
            print("D - No such option in python.")
            ans = input()
            if ans == "C" or ans == "c" :
                total=total+1
            if (ans == "exit" ) or (ans == "0") or (ans == "quit") : 
                os.system("exit()")
            else :
                print("Wrong answer")
            print("Total Marks:" , end = '')
            print(total)
        
          elif choice == "4" : 
            total =0
            q = 1
            os.system("cls")
            print("Question 1 :" , end = '')
            print("\tIs it necessary that each try block must be followed by a finally block?")
            print("A - True")
            print("B - False")
            ans = input()
            if ans == "B" or ans == "b" :
                total=total+1
            if (ans == "exit" ) or (ans == "0") or (ans == "quit") : 
                os.system("exit()")
            else :
                print("Wrong answer")
            os.system("cls")
            print("Question 2 :" , end = '')
            print("\tWhat is the default value of Boolean variable?")
            print("A - true")
            print("B - false")
            print("C - 0")
            print("D - not defined")
            ans = input()
            if ans == "B" or ans == "b" :
                total=total+1
            if (ans == "exit" ) or (ans == "0") or (ans == "quit") : 
                os.system("exit()")
            else :
                print("Wrong answer")
            os.system("cls")
            print("Question 3 :" , end = '')
            print("\tWhat is the default value of float variable?")
            print("A - 0.0d")
            print("B - 0.0f")
            print("C - 0")
            print("D - not defined")
            ans = input()
            if ans == "B" or ans == "b" :
                total=total+1
            if (ans == "exit" ) or (ans == "0") or (ans == "quit") : 
                os.system("exit()")
            else :
                print("Wrong answer")
            os.system("cls")
            print("Question 4 :" , end = '')
            print("\tPrimitive variables are stored on Stack.")
            print("A - True")
            print("B - False")
            ans = input()
            if ans == "A" or ans == "a" :
                total=total+1
            if (ans == "exit" ) or (ans == "0") or (ans == "quit") : 
                os.system("exit()")
            else :
                print("Wrong answer")
            os.system("cls")
            print("Question 5 :" , end = '')
            print("\t What is the size of boolean variable?")
            print("A - 8 bit")
            print("B - 16 bit")
            print("C - 32 bit")
            print("D - not precisely defined")
            ans = input()
            if ans == "B" or ans == "b" :
                total=total+1
            if (ans == "exit" ) or (ans == "0") or (ans == "quit") : 
                os.system("exit()")
            else :
                print("Wrong answer")
            print("Total Marks:" , end = '')
            print(total)
        
          else : 
              print("Choice not recognised")

        
    elif(("play" in x) and ("game" in x)):
          t = ["rock","paper","scissors"]
          player = False
          while(player == False):
            computer = t[rand(0,2)]
            play = input("rock, paper, scissors ?")
            if(play == computer):
                print("Tie..!!!!!")
            elif(play == "rock"):
                if(computer == "paper"):
                    print("YOU LOSE...")
                else:
                    print("YOU WON...")
                    player=True
            elif(play == "paper"):
                if(computer == "scissors"):
                    print("YOU LOSE...")
                else:
                    print("YOU WON...")
                    player = True
            else:
                if(computer == "rock"):
                    print("YOU LOSE...")
                else:
                    print("YOU WON...")
                    player = True
    elif("portfolio" in x):
          os.system("chrome mr-sushant.github.io/")
    elif("exit" in x or "quit" in x):
          break
