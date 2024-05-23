from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime, timedelta
import requests
from PIL import Image, ImageTk

root = Tk()
root.title("Weather App")
root.geometry("890x470+300+200")
root.configure(bg="#57adff")
root.resizable(False, False)

def get_weather():
    city = textfield.get()
    if city:
        try:
            url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=71584e1d7c594ed2e2a15aaa6820fa80&units=metric"
            response = requests.get(url)
            data = response.json()
        
            if response.status_code == 200:
                current_time = datetime.now().strftime('%I:%M %p')

                city_name = data['name']
                city_label.config(text=city_name)
                
                Temperature = data['main']['temp']
                Humidity = data['main']['humidity']
                Pressure = data['main']['pressure']
                Wind = data['wind']['speed']
                Description = data['weather'][0]['description']
    
                temp.config(text=f"{Temperature}°C")
                humi.config(text=f"{Humidity}%")
                pres.config(text=f"{Pressure} hPa")
                wind.config(text=f"{Wind} m/s")
                des.config(text=Description)

                forecast_url = f"https://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid=71584e1d7c594ed2e2a15aaa6820fa80&units=metric"
                forecast_response = requests.get(forecast_url)
                data_info = forecast_response.json()
                
                if forecast_response.status_code == 200:
                    forecast_temps = []
                    forecast_descs = []
                    forecast_icons = []

                    # 5 days forecast
                    num_forecast_entries = min(len(data_info['list']), 5 * 8)  
                    for i in range(0, num_forecast_entries, 8):
                        forecast = data_info['list'][i]
                        forecast_temp = forecast['main']['temp']
                        forecast_desc = forecast['weather'][0]['description']
                        forecast_icon = forecast['weather'][0]['icon']
                        icon_url = f"https://openweathermap.org/img/wn/{forecast_icon}@2x.png"
                        icon = Image.open(requests.get(icon_url, stream=True).raw)
                        icon = ImageTk.PhotoImage(icon.resize((50, 50)))

                        forecast_temps.append(forecast_temp)
                        forecast_descs.append(forecast_desc)
                        forecast_icons.append(icon)

                    day1_temp.config(text=f"{forecast_temps[0]}°C" if len(forecast_temps) > 0 else "")
                    day1_desc.config(text=f"{forecast_descs[0]}" if len(forecast_descs) > 0 else "")
                    firstimage.config(image=forecast_icons[0] if len(forecast_icons) > 0 else None)
                    firstimage.image = forecast_icons[0] if len(forecast_icons) > 0 else None

                    day2_temp.config(text=f"{forecast_temps[1]}°C" if len(forecast_temps) > 1 else "")
                    day2_desc.config(text=f"{forecast_descs[1]}" if len(forecast_descs) > 1 else "")
                    secondimage.config(image=forecast_icons[1] if len(forecast_icons) > 1 else None)
                    secondimage.image = forecast_icons[1] if len(forecast_icons) > 1 else None

                    day3_temp.config(text=f"{forecast_temps[2]}°C" if len(forecast_temps) > 2 else "")
                    day3_desc.config(text=f"{forecast_descs[2]}" if len(forecast_descs) > 2 else "")
                    thirdimage.config(image=forecast_icons[2] if len(forecast_icons) > 2 else None)
                    thirdimage.image = forecast_icons[2] if len(forecast_icons) > 2 else None

                    day4_temp.config(text=f"{forecast_temps[3]}°C" if len(forecast_temps) > 3 else "")
                    day4_desc.config(text=f"{forecast_descs[3]}" if len(forecast_descs) > 3 else "")
                    fourthimage.config(image=forecast_icons[3] if len(forecast_icons) > 3 else None)
                    fourthimage.image = forecast_icons[3] if len(forecast_icons) > 3 else None

                    day5_temp.config(text=f"{forecast_temps[4]}°C" if len(forecast_temps) > 4 else "")
                    day5_desc.config(text=f"{forecast_descs[4]}" if len(forecast_descs) > 4 else "")
                    fifthimage.config(image=forecast_icons[4] if len(forecast_icons) > 4 else None)
                    fifthimage.image = forecast_icons[4] if len(forecast_icons) > 4 else None

                    first = datetime.now()
                    day1.config(text=first.strftime("%A"))

                    second = first + timedelta(days=1)
                    day2.config(text=second.strftime("%A"))

                    third = first + timedelta(days=2)
                    day3.config(text=third.strftime("%A"))

                    fourth = first + timedelta(days=3)
                    day4.config(text=fourth.strftime("%A"))

                    fifth = first + timedelta(days=4)
                    day5.config(text=fifth.strftime("%A"))

                    clock.config(text=current_time)
                else:
                    messagebox.showerror("Error", "Unable to fetch forecast data. Please try again later.")
            else:
                messagebox.showerror("Error", "Unable to fetch weather data. Please try again later.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
    else:
        messagebox.showwarning("Warning", "Please enter a location.")

#icon
image_icon = PhotoImage(file="images/logo.png")
root.iconphoto(False, image_icon)
Round_box = PhotoImage(file="images/rectangle.png")
Label(root, image=Round_box, bg="#57adff").place(x=30, y=100)

#Label
label1 = Label(root, text="Temperature", font=('Helvetica', 11), fg="white", bg="#203243")
label1.place(x=50, y=120)

label2 = Label(root, text="Humidity", font=('Helvetica', 11), fg="white", bg="#203243")
label2.place(x=50, y=140)

label3 = Label(root, text="Pressure", font=('Helvetica', 11), fg="white", bg="#203243")
label3.place(x=50, y=160)

label4 = Label(root, text="Wind Speed", font=('Helvetica', 11), fg="white", bg="#203243")
label4.place(x=50, y=180)

label5 = Label(root, text="Description", font=('Helvetica', 11), fg="white", bg="#203243")
label5.place(x=50, y=200)

#search box
Search_image = PhotoImage(file="images/rectangle box.PNG")
myimage = Label(image=Search_image, bg="#57adff")
myimage.place(x=270, y=120)

weat_image = PhotoImage(file="images/cloud.png")
weatherimage = Label(root, image=weat_image, bg="#203243")
weatherimage.place(x=305, y=135)

textfield = tk.Entry(root, justify='center', width=15, font=('times of roman', 25, 'bold'), bg="#203243", fg="white", border=0, borderwidth=0, highlightthickness=0)
textfield.place(x=375, y=143)
textfield.focus()

Search_icon = PhotoImage(file="images/search_icon.png")
myimage_icon = Button(image=Search_icon, borderwidth=0, cursor="hand2", bg="#203243", command=get_weather)
myimage_icon.place(x=645, y=132)

#bottom of the app
frame = Frame(root, width=900, height=180, bg="#212120")
frame.pack(side=BOTTOM)

#bottom box
firstbox = PhotoImage(file="images/Rounded Rectangle 2.png")
secondbox = PhotoImage(file="images/Rounded Rectangle 2 copy.png")

Label(frame, image=firstbox, bg="#212120").place(x=45, y=20)
Label(frame, image=secondbox, bg="#212120").place(x=340, y=30)
Label(frame, image=secondbox, bg="#212120").place(x=460, y=30)
Label(frame, image=secondbox, bg="#212120").place(x=580, y=30)
Label(frame, image=secondbox, bg="#212120").place(x=700, y=30)

#clock
clock = Label(root, font=("Helvetica", 30), fg="white", bg="#57adff")
clock.place(x=30, y=20)

#city name 
city_label = tk.Label(root, text="", font=('Arial 20', 30), fg="white", bg="#57adff")
city_label.place(x=630, y=30)

#timezone
long_lat = Label(root, font=("Helvetica", 10), fg="white", bg="#57adff")
long_lat.place(x=700, y=50)

#temperature, humidity, pressure, wind speed, and description labels
temp = Label(root, font=('Helvetica', 11), fg="white", bg="#203243")
temp.place(x=150, y=120)

humi = Label(root, font=('Helvetica', 11), fg="white", bg="#203243")
humi.place(x=150, y=140)

pres = Label(root, font=('Helvetica', 11), fg="white", bg="#203243")
pres.place(x=150, y=160)

wind = Label(root, font=('Helvetica', 11), fg="white", bg="#203243")
wind.place(x=150, y=180)

des = Label(root, font=('Helvetica', 11), fg="white", bg="#203243")
des.place(x=150, y=200)

# first cell
firstframe = Frame(root, width=230, height=132, bg="#282829")
firstframe.place(x=50, y=315)

day1 = Label(firstframe, font="arial 21", bg="#282829", fg="#fff")
day1.place(x=78, y=5)

firstimage = Label(firstframe, bg="#282829")
firstimage.place(x=4, y=15)

day1_temp = Label(firstframe, font="arial 16", bg="#282829", fg="#fff")
day1_temp.place(x=78, y=42)

day1_desc = Label(firstframe, font="arial 16", bg="#282829", fg="#fff")
day1_desc.place(x=78, y=65)

# second cell
secondframe = Frame(root, width=70, height=115, bg="#282829")
secondframe.place(x=345, y=325)

day2 = Label(secondframe, bg="#282829", fg="#fff")
day2.place(x=10, y=5)

secondimage = Label(secondframe, bg="#282829")
secondimage.place(x=7, y=26)

day2_temp = Label(secondframe, font="arial 10", bg="#282829", fg="#fff")
day2_temp.place(x=10, y=70)

day2_desc = Label(secondframe, font="arial 10", bg="#282829", fg="#fff")
day2_desc.place(x=10, y=90)

# third cell
thirdframe = Frame(root, width=70, height=115, bg="#282829")
thirdframe.place(x=465, y=325)

day3 = Label(thirdframe, bg="#282829", fg="#fff")
day3.place(x=10, y=5)

thirdimage = Label(thirdframe, bg="#282829")
thirdimage.place(x=7, y=26)

day3_temp = Label(thirdframe, font="arial 10", bg="#282829", fg="#fff")
day3_temp.place(x=10, y=70)

day3_desc = Label(thirdframe, font="arial 10", bg="#282829", fg="#fff")
day3_desc.place(x=10, y=90)

# fourth cell
fourthframe = Frame(root, width=70, height=115, bg="#282829")
fourthframe.place(x=585, y=325)

day4 = Label(fourthframe, bg="#282829", fg="#fff")
day4.place(x=10, y=5)

fourthimage = Label(fourthframe, bg="#282829")
fourthimage.place(x=7, y=26)

day4_temp = Label(fourthframe, font="arial 10", bg="#282829", fg="#fff")
day4_temp.place(x=10, y=70)

day4_desc = Label(fourthframe, font="arial 10", bg="#282829", fg="#fff")
day4_desc.place(x=10, y=90)

# fifth cell
fifthframe = Frame(root, width=70, height=115, bg="#282829")
fifthframe.place(x=705, y=325)

day5 = Label(fifthframe, bg="#282829", fg="#fff")
day5.place(x=10, y=5)

fifthimage = Label(fifthframe, bg="#282829")
fifthimage.place(x=7, y=26)

day5_temp = Label(fifthframe, font="arial 10", bg="#282829", fg="#fff")
day5_temp.place(x=10, y=70)

day5_desc = Label(fifthframe, font="arial 10", bg="#282829", fg="#fff")
day5_desc.place(x=10, y=90)

root.mainloop()
