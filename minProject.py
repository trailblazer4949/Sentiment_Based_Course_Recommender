from nltk.sentiment.vader import SentimentIntensityAnalyzer
from PIL import ImageTk, Image
import PIL
import pyaudio
import pandas as pd
import numpy
from tkinter import *
import random
import speech_recognition as sr
from nltk import *
import pyttsx3
import math


def speak(command):

    engine = pyttsx3.init()  # engine initialized
    engine.setProperty("rate", 200)
    engine.say(command)
    engine.runAndWait()
    engine.stop


def recognize():
    r = sr.Recognizer()
    while True:
        try:
            with sr.Microphone() as source2:  # here i have set the microphone as source2
                print("Speak something : ")

                # activated microphone
                audio = r.listen(source2, timeout=1, phrase_time_limit=5)
                MyText = r.recognize_google(audio)
                r.adjust_for_ambient_noise(source2, duration=0.2)
                print("Thinking....wait ")

                MyText = MyText.lower()  # convert the text in lower case
                inp_val = MyText

                print("user says " + MyText)  # input by the user

                if "credit required" in MyText:
                    speak("You must have 80 credits")
                elif "submit" in MyText:
                    speak("Okay sir")
                    submit()
                elif "what you can do":
                    info()

                elif "stop" in MyText:
                    print("Bye Bye")
                    break

        except sr.RequestError as e:
            print("Not possile now")


speak("Welcome to Course Recommender!")


def submit():
    sentiment_Result = [""]
    msg = inp_val.get()
    sentiment = SentimentIntensityAnalyzer()

    print(msg)
    print()
    ss = sentiment.polarity_scores(msg)
    temp = ss.items()
    print(temp)
    temp1 = list(ss.values())

    print(temp1[0])
    print('{0}: {1}, '.format(msg, ss), end='')
    print(ss)
    sentiment_Result.append(ss)
    print()

    credit = inp_Entry_Credit.get()

    if temp1[0] < 0.4:
        speak("You can apply courses of your interest!")
        if inp_credit_vals.get() < min_credit:
            required_Credit = min_credit - inp_credit_vals.get()
            speak("You are not Eligible for MIT Courses!")
            print("You have ", end=" ")
            print(required_Credit, end=" ")
            print("more to")
            speak("You have to gain")
            speak(required_Credit)
            speak("more credits")
            # speak(csvFile['MITCourse'])

            speak("you can go with")

            if inp_val.get() in machineLearning:
                print("You can go with -->", end="")
                print(random.choices(csvFile['MachineLearning']))
                speak(random.choices(csvFile['MachineLearning']))

            elif msg in DataAnalysis:
                print(random.choices(csvFile['DataAnalysis']))
                speak(random.choices(csvFile['DataAnalysis']))

            elif msg in DataStructure:
                print(random.choices(csvFile['Datastrucure']))
                speak(random.choices(csvFile['Datastrucure']))

            elif msg in DataVisualization:
                print(random.choices(csvFile['DataVisualization']))
                speak(random.choices(csvFile['DataVisualization']))

            elif msg in Marketing:
                print(random.choices(csvFile['Marketing']))
                speak(random.choices(csvFile['Marketing']))

            elif msg in ContentMarketing:
                print(random.choices(csvFile['ContentMarketing']))
                speak(random.choices(csvFile['ContentMarketing']))

            elif msg in WebDeveloment:
                print(random.choices(csvFile['WebDeveloment']))
                speak(random.choices(csvFile['WebDeveloment']))

            elif msg in Architecture:
                print(random.choices(csvFile['Architecture']))
                speak(random.choices(csvFile['Architecture']))

            elif msg in GraphicDesign:
                print(random.choices(csvFile['Graphicdesign']))
                speak(random.choices(csvFile['Graphicdesign']))

            elif msg in CloudComputing:
                print(random.choices(csvFile['Cloudcomputing']))
                speak(random.choices(csvFile['Cloudcomputing']))
            else:
                print("Not understood")
                speak("I'm not able to understand")

    else:
        if inp_credit_vals.get() < min_credit:
            required_Credit = min_credit - inp_credit_vals.get()
            speak("You are not Eligible for MIT Courses!")
            print("You have ", end=" ")
            print(required_Credit, end=" ")
            print("more to")
            speak("You have to gain")
            speak(required_Credit)
            speak("more credits")
            speak("You can enter other course as per your interest ")

        else:
            speak(csvFile['MITCourse'])
            print(csvFile['MITCourse'])


def info():
    speak("I can recommend you a good course as per your inerest, i can also check that if student is eligible for MIT courses or not")


print("RUNNNNNNNNN")
csvFile = pd.read_csv("Book411.csv")


course = csvFile['MachineLearning']

print("********")
print(csvFile.head())

machineLearning = ["ML", "Machine Learning", "AI", "ml", "machine learning"]
DataAnalysis = ["data analysys", "DataAnalysis", "Data Analysis"]
DataVisualization = ["Data Visualization",
                     "data visualization", "datavisualization"]
GraphicDesign = ["Graphic Design", "graphicdesign", "GraphicDesign"]

DataStructure = ["datastructure", "DataStructure",
                 "data structure", "Data Structure"]
CloudComputing = ["Cloud Computing", "Cloudcomputing"]

Marketing = ["Marketing", "marketting"]

ContentMarketing = ["ContentMarketing", "Content Marketting"]

SocialMediaMarketting = ["Social Media Marketing", "social media marketting"]

WebDeveloment = ["Web", "Web development", "Web Development"]

Architecture = ["Architecture", "architecture"]


machineLearningCourse = ["ML for everybody",
                         "ML and Datastrucure", "Ml with Piyush"]
course_credits = ['7', '8', '9', '10']


root = Tk()


load = PIL.Image.open("G:\\VSCODE\\NLP_LAB\\1.jpg")
render = ImageTk.PhotoImage(load)
img = Label(root, image=render)
img.place(x=0, y=0)

root.geometry("800x450")
lab = Label(text="Course Recommender",
            font="timesnewroman 22", padx=12, pady=44)
lab.grid(row=1, column=10)

root.title("Course Recommender")

inp_val = StringVar()
inp_credit_vals = IntVar()

# x = inp_credit_vals.get()
Course_Credit = 10
min_credit = 80
# y = int(inp_credit_vals.get())
# required_Credit = min_credit - y


button1 = Button(text="MIT Courses", activebackground="red", command="")
button1.grid(row=20, column=10)
photo = PhotoImage(file=r"G:\\VSCODE\\NLP_LAB\\mic.png")
photo = photo.subsample(4)
button2 = Button(root, text="Click To Speak", image=photo,
                 activebackground="red", command=recognize)
button2.grid(row=3, column=19)

msg = inp_val.get()
print(msg)


frame = Frame(root, width=5, height=5)
frame.grid(row=12, column=10)

lab = Label(frame, text="Course Eligibility", wraplength=200, font="20")
lab.grid(row=12, column=10)

inp_entry = Entry(root, textvariable=inp_val,
                  insertbackground="skyblue", width=30, bg='red')

inp_entry.grid(row=3, column=10)

inp_Entry_Credit = Entry(root, textvariable=inp_credit_vals,
                         width=10, insertbackground="skyblue", bg="red")

inp_Entry_Credit.grid(row=16, column=10, pady=12)

label1 = Label(text="Your Interest")
label2 = Label(text="Enter Credits")


label1.grid(row=3)
label2.grid(row=16)
button = Button(text="Submit", activebackground="red", command=submit)

button.grid(row=5, column=10, pady=12)


root.mainloop()
