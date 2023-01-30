from tkinter import*
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

root=Tk()
root.title("Weather APP")
root.geometry("900x600+300+200")
root.config(background="#B5E61D")


root.resizable(0,0)

def getweather():
    try:
        city=textfield.get()
        geolocation=Nominatim(user_agent="geoapiExercises")
        location=geolocation.geocode(city)
        obj=TimezoneFinder()
        result=obj.timezone_at(lng=location.longitude,lat=location.latitude)
        #print(result)
        home=pytz.timezone(result)
        local_time=datetime.now(home)
        current_time=local_time.strftime("%H:%M")
        clock.config(text=current_time)
        name.config(text="CURRENT WHEATHER")

    #wheather
        api="https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=3df3f30f6b41eca8554207f647e88b5d"
        json_data=requests.get(api).json()
        condition=json_data['weather'][0]['main']
        description=json_data['weather'][0]['description']
        temp=int(json_data['main']['temp']-273.15)
        pressure=json_data['main']['pressure']
        humidity=json_data['main']['humidity']
        wind=json_data['wind']['speed']

        t.config(text=(temp,"°"))
        c.config(text=(condition,"|","FEELS","LIKE",temp,"°"))
        w.config(text=wind)
        h.config(text=humidity)
        d.config(text=description)
        p.config(text=pressure)
    except Exception as e:
        messagebox.showerror("Weather App","Invalid Entry")
#search box
search_image=PhotoImage(file="search.png")
myimage=Label(image=search_image)
myimage.place(x=20,y=20)

textfield=tk.Entry(root,justify="center",width=20,font=("poppins",25,"bold"),bg="#404040",border=0,fg="white")
textfield.place(x=32,y=30)
textfield.focus()

search_icon=PhotoImage(file="searchicon.png")
myimage_icon=Button(image=search_icon,borderwidth=0,cursor="hand2",bg="#404040",command=getweather)
myimage_icon.place(x=480,y=35)

#logo
logo_image=PhotoImage(file="logo.png")
logo=Label(image=logo_image,bg="#B5E61D")
logo.place(x=150,y=160)

#bottom box
frame_image=PhotoImage(file="banner.png")
frame_my_image=Label(image=frame_image)
frame_my_image.pack(padx=5,pady=5,side=BOTTOM)

#time
name=Label(root,font=("arial",15,"bold"))
name.place(x=30,y=120)
clock=Label(root,font=("helvetica",20))
clock.place(x=30,y=150)


#label
label1=Label(root,text="WIND",font=("Helvetica",15,"bold"),fg="white",bg="#1ab5ef")
label1.place(x=120,y=430)

label2=Label(root,text="HUMIDITY",font=("Helvetica",15,"bold"),fg="white",bg="#1ab5ef")
label2.place(x=250,y=430)

label3=Label(root,text="DESCRIPTION",font=("Helvetica",15,"bold"),fg="white",bg="#1ab5ef")
label3.place(x=430,y=430)

label4=Label(root,text="PRESSURE",font=("Helvetica",15,"bold"),fg="white",bg="#1ab5ef")
label4.place(x=650,y=430)

t=Label(font=("arial",70,"bold"),fg="#ee666d")
t.place(x=400,y=150)
c=Label(font=("arial",15,"bold"))
c.place(x=400,y=250)

w=Label(text="....",font=("arial",20,"bold"),bg="#1ab5ef")
w.place(x=120,y=460)

h=Label(text="....",font=("arial",20,"bold"),bg="#1ab5ef")
h.place(x=280,y=460)

d=Label(text="....",font=("arial",20,"bold"),bg="#1ab5ef")
d.place(x=450,y=460)

p=Label(text="....",font=("arial",20,"bold"),bg="#1ab5ef")
p.place(x=670,y=460)
 

root.mainloop()