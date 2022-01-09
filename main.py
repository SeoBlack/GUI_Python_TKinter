from tkinter import *
FONT = ("Arial",16,"normal")
def calculate():
    value = float(textinput.get())
    result = round(value * 1.609  , 3)
    result_Label.config(text=result)

window = Tk()
window.minsize(width=300,height=150)
window.config(pady=30,padx=50)
window.title("Miles to Kilometer converter")
#labels

Miles_Label = Label(text="Miles", font=FONT)
Miles_Label.grid(column=2, row=0)


Kilo_Label = Label(text="Km", font=FONT)
Kilo_Label.grid(column=2, row=1)

equal_to_Label = Label(text="is equal to", font=FONT)
equal_to_Label.grid(column=0, row=1)

result_Label = Label(text=0, font=FONT)
result_Label.grid(column=1, row=1)
#textinput

textinput = Entry(width=10, textvariable=IntVar(), font=FONT)
textinput.grid(column=1, row=0)


#buttons

B1 = Button(text="Calculate",command=calculate,font=FONT)
B1.grid(column=1,row=2)













window.mainloop()