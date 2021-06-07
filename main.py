# Tkinter
import tkinter as tk
from tkinter import *
import requests
root = tk.Tk()
root.title("Weather")
root.geometry("400x500")
root.configure(bg="skyblue")
insert_city=StringVar

# create constant labels

city_label=Label(root,text="City",font='Helvetica 40 bold',bg="skyblue")
city_label.place(x=30,y=40)
city_entry=Entry(root,textvariable="city",bg="skyblue")
city_entry.place(x=150,y=50, width=100)

# define function to get weather for city entered

def get_weather():
    # code to initialize weather request from API

    city = city_entry.get()
    r = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=51524588b0fa12fa3f0257f244a31490")
    data = r.json()
    # create labels which will appear once the city iis entered

    temp = Label(root, text=int(data['main']['temp'] - 273.15),font='Helvetica 40 bold', bg="skyblue")
    temp.place(x=160, y=150)
    degrees = Label(root, text="degrees", font='Helvetica', bg="skyblue")
    degrees.place(x=160, y=210)
    temp_m=Label(root,text=int(data['main']['temp_min'] - 273.15), font='Helvetica', bg="skyblue")
    temp_m.place(x=180,y=240)
    min=Label(root, text="low: ",font='Helvetica', bg="skyblue" )
    min.place(x=125,y=240)
    temp_h=Label(root,text=int(data['main']['temp_max']- 273.15),font='Helvetica', bg="skyblue")
    temp_h.place(x=250, y=240)
    low= Label(root, text="high: ", font='Helvetica', bg="skyblue")
    low.place(x=200,y=240)
    winds = Label(root, text="Wind speed: " + str(data['wind']['speed']) + "KM/h", font='Helvetica', bg="skyblue")
    winds.place(x=120,y=290)
    hum = Label(root, text="humidity: " + str(data['main']['humidity']),font='Helvetica', bg="skyblue")
    hum.place(x=150,y=315)
    cloudcover=Label(root,text=str(data['weather'][0]['main'] + " skies"), font='Helvetica', bg="skyblue")
    cloudcover.place(x=150,y=265)

    # define clear button to clear all fields called after weather was fethced

    def clear1():
        city_entry.delete(0,END)
        temp.config(text="")
        degrees.config(text="")
        temp_m.config(text="")
        min.config(text="")
        temp_h.config(text="")
        low.config(text="")
        winds.config(text="")
        hum.config(text="")
        cloudcover.config(text="")


    # create clear button and place
    clear=Button(root,text="clear All fields", command=clear1, bg="yellow")
    clear.place(x=135,y=350)

# create cutton to initialize get weather function
get=Button(root,text="weather",command=get_weather,bg="yellow")
get.place(x=300,y=50)
root.mainloop()
