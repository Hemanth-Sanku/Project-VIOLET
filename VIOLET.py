#pattern
def pattern(n):
      k = 2*n -2
      for i in range(n,-1,-1):
           for j in range(k,0,-1):
                print(end=" ")
           k = k +1
           for j in range(0, i+1):
                print("V", end=" ")
           print("\r")
pattern(8)



#START

print("       ")
print("Hi.I'm VIOLET. A Smart ChatBot.")
name=input("What is your name. ")
print("Hi ",name)



#LIBRARIES

import math

from datetime import date
date = date.today().strftime('%d/%m/%Y')

import time
time=time.strftime("%I:%M:%S")

import calendar
cal=calendar.calendar(2020)

import random

import pytube
from pytube import YouTube

import speedtest
from speedtest import Speedtest


while True:
    question = input("Ask me:")
    question = question.lower()



#SPECIAL CONVERSATIONS

    if question in ['hi','hello','hi elbo','hii','hello elbo','hey','hola','elbo','howdy','elbo','hi. elbo','say hello','say hi']:
          a=("hi","hello","hi I'm Elbo","hai","hello I'm Elbo","Hey","Hey. How may I help You")
          print(random.choice(a))
          
    elif question in ['how are you','how do you do','how are you?','how r u']:
        print("I am fine.Thankyou.")

    elif question in ['are you working','are you doing any job',"do you have any job"]:
        print("yes. I can answer the simple questions from you")

    elif question in ['your salary','how much do you get paid',"what is your salary"]:
          print("I don't get paid for my work.")

    elif question in ['what is your name','who are you','your name','ur name']:
        print("Hi I'm Elbo.") 
    
    elif question in ['what are you doing']:
        print("I'm waiting for your question.")

    elif question in ['Thankyou','thanks','thank you','thankyou so much','thank you so much','thankyou soo much','thank you soo much','thankyou very much','thank you very much']:
        t=("You are Welcome,","Never mind","Don't mention")
        print(random.choice(t))

    elif question in ['what are you doing']:
        print("I'm waiting for your question.")

    elif question in ['are you male or female','are you male','are you female','whats your gender','what is your gender']:
        print("I'm Female.")


#Features INFO
    elif question in ['what can you do','help','info','your abilities','your features','abilities','features']:
        print("\nMy abilities: \n-Special Conversations:\n 1.Vote Eligibility.\n 2.Age Calculator.\n-Tools:\n 1.Time, date and calendar.\n-Converter:\n 1.km to mile.\n 2.kg to lbs.\n 3.cm to m.\n 4.ft to cm.\n-Math Skills:\n 1.Addition.\n 2.Subtraction.\n 3.Division.\n 4.Multiplication.\n-Areas:\n 1.Area of circle.\n 2.Area of triangle.\n 3. Area of square.\n-PI Value.\n-Internet Skills:\n 1.Youtube Video Downloader.\n 2.Internet Speedtest.\n")



#SKILLS AND TOOLS

#Time, Date and Calendar
    elif question in ['what is the time now','time','what is the time now?','tell me the time now','tell me the time?','tell me the time']:
        print(time)

    elif question in ['what is the date today','date','what is the date tody?','what is the today date','tell me the date today','tell me the date?','tell me the date']:
        print("Today's date is -", date,".(dd/mm/YYYY)")

    elif question in ['show Calendar','Calendar','cal','show me calendar']:
        yy=int(input("Which year: "))
        mm=int(input("Which month: "))
        print(calendar.month(yy,mm))

#Vote eliggibility
    elif question in ['do i eligible to vote','vote eligiblity','am i eligible to vote','do i eligible to vote in coming ellections','am i eligible to vote in coming ellections','am i eligible to vote in this ellections','do i eligible to vote in coming ellections']:
        age=int(input("Enter your age:"))
        if(age>=18):
                    print("You are eligible to vote, As you are above 18 Years.")
        else:
             print("You are not eligible to vote, As you are under 18 Years.")

    elif question in ['my name','what is my name','whats my name','wht is my name']:
        print("You said your name is ",name)

        
#Age calculator
    elif question in ['what is my age','age','whats my age','my age']:
        b=int(input("Ok. Tell me in which year do you born: "))
        age=2021-b
        print("Your age now: ",age)



#CONVERTER
    elif question in ['converter','convert','open converter','unit converter']:
      print("What do you want me to convert:\n1.km to mile\n2.kg to lbs\n3.cm to m\n4.ft to cm")
      
#1.km to mile
    elif question in ['km to mile','km to mi','convert km to miles','convert km to mile', 'kms to miles']:
      km=float(input("Enter no of km to convert: "))
      mile=(km/1.609344)
      print("Your km conversion to Miles:",round(mile,2),"miles.")
#2.kg to lbs
    elif question in ['kg to lbs','kg to lb','convert kg to lbs','convert kg to lb', 'kgs to lbs']:
      kg=float(input("Enter no of kg to convert: "))
      lbs=(kg*2.205)
      print("Your kg conversion to lbs:",round(lbs,2),"lbs.")

#3.cm to m
    elif question in ['cm to m','cm to meter','convert cm to meter','convert cm to m', 'cm to meters']:
      cm=float(input("Enter no of cm to convert: "))
      meter=(cm/100)
      print("Your cm conversion to meter:",round(meter,2),"meters.")

#4.ft to cm
    elif question in ['fts to cm','ft to cm','convert ft to cm','convert fts to cm', 'ft to cms']:
      ft=float(input("Enter no of ft to convert: "))
      cm=(ft*30.48)
      print("Your ft conversion to cm:",round(cm,2),"cm.")




#MATH SKILLS
        
#1.Addition

    elif question in ['addition','add','add two numbers','do addition','add 2 numbers']:
        a=int(input("Enter first value: "))
        b=int(input("Enter second value: "))
        add=a+b
        print("Addition is: ",add)
        
#2.Subtraction

    elif question in ['subtraction','sub','subtract','subtract two numbers','subtract 2 numbers']:
        a=int(input("Enter first value: "))
        b=int(input("Enter second value: "))
        sub=a-b
        print("subtraction is: ",sub)
        
#3.Division

    elif question in ['division','div','divide','divide two numbers','divide 2 numbers']:
        a=int(input("Enter first value: "))
        b=int(input("Enter second value: "))
        div=a/b
        print("Division is: ",div)
        
#4.Multiplication

    elif question in ['multiplication','mul','multiply','multiply two numbers','multipy 2 numbers']:
        a=int(input("Enter first value: "))
        b=int(input("Enter second value: "))
        mul=a*b
        print("Division is: ",mul)
        
#Areas
        
#1.Circle
    elif question in ['area of circle','area of the circle','can you tell me area of circle','I want to know area of circle','circle']:
          r=float(input("Enter the radius of Circle:"))
          area=(math.pi*(r**2))
          circumference=(2*math.pi*r)
          print("Area of the Circle is=",round(area,2),"\nCircumference of Circle is=",round(circumference,2))
          
#2.Triangle
    elif question in ['area of triangle','area of the triangle','can you tell me area of triangle','I want to know area of triangle','triangle']:
          b=float(input("Enter the Base of triangle:"))
          h=float(input("Enter the Height of triangle:"))
          area=(1/2*(b*h))
          print("Area of the triangle is=",round(area,2))
#3.Square
    elif question in ['area of square','area of the Square','can you tell me area of Square','I want to know area of Square','square']:
          s=float(input("Enter the Base of Square:"))
          area=(s**2)
          print("Area of the Square is=",round(area,2))

#PI Value
    elif question in ['what is the pi value','pi value', 'whats the pi value','value of pi','pi']:
          print(math.pi)
          


#INTERNET SKILLS

#1.Youtube Downloader

    elif question in ['youtube download','YouTube video download','youtube downloader','download youtube video']:
        video_url=input("Paste the YouTube URL: ")
        youtube = pytube.YouTube(video_url)
        video = youtube.streams.first()
        video.download('F:/')
        print("Video downloaded in drive:F")

#Speedtest
        
    elif question in ['speedtest','speed test',"do speedtest","do speed test"]:
          st=Speedtest()
          print("Checking your Download and Upload Speeds wait.....")
          print("Your Download Speed is:",round((st.download()/1000000),2),"Mbps")
          print("Your Upload Speed is:",round((st.upload()/1000000),2),"Mbps")



#THE END
    elif question in ['quit','exit','end','the end','stop','bye','see you later','good bye','get lost','go away','see you','close']:
        break
    else:
          print("Sorry. I did'nt get you. You can ask 'help' or 'info' for more information.")
