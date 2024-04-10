import tkinter as tk 
from main import get_weather_data
 #making gui for weather
 
def get_city():
    question = city_entry.get()
    response = get_weather_data(question)
    print(response, " degrees fahrenehiet")
    return response

    
    
master = tk.Tk()

master.config(width = 800,height = 800)
master.title("Weather Application")

question_label = tk.Label(master, text = "what city would you like to know the tempature for? ")
question_label.pack()

city_entry = tk.Entry(master)
city_entry.pack()

print_button = tk.Button(master, text = "submit", command = get_city)
print_button.pack()

master.mainloop()
