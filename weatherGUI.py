import tkinter as tk 
 #making gui for weather
 
def print_question():
    question = question_entry.get()
    print("Question:", question)


master = tk.Tk()

master.config(width =400,height = 300)
master.title("Weather Application")

question_label = tk.Label(master, text = "Enter your question: ")
question_label.pack()

question_entry = tk.Entry(master, width = 50)
question_entry.pack()

print_button = tk.Button(master, text = "submit", command = print_question)
print_button.pack()


master.mainloop()
