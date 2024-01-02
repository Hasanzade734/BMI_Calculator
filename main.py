import tkinter

window = tkinter.Tk()
window.title("BMI Calculator")
window.minsize(width=300,height=300)

my_label1= tkinter.Label(text="Enter Your Weight (kg)",font=("Arial",10,"bold"))
my_label1.pack()

my_entry1= tkinter.Entry()
my_entry1.place(y=30,x=88)

my_label2= tkinter.Label(text="Enter Your Height (cm)",font=("Arial",10,"bold"))
my_label2.place(y=60,x=76)

my_entry2= tkinter.Entry()
my_entry2.place(y=90,x=88)

resualt_lable = tkinter.Label()
resualt_lable.pack()



def calculator():
    try:
        weight = my_entry1.get()
        height = my_entry2.get()
        if weight == "" or height == "":
            print(resualt_lable.config(text="Entry both weight and height"))
            print(resualt_lable.place(y=160,x=80))
        else:
            intw = int(weight)
            inth = int(height)
            BMI = intw / (inth / 100) ** 2

            if 0 <= BMI <= 18.4:
                print(resualt_lable.config(text=f"Your BMI score : {int(BMI)} Under Wight"))
                print(resualt_lable.place(y=160, x=80))

            elif 18.5 <= BMI <= 24.9:
                print(resualt_lable.config(text=f"Your BMI score : {int(BMI)} Normal Weight"))
                print(resualt_lable.place(y=160, x=80))

            elif 25.0 <= BMI <= 29.9:
                print(resualt_lable.config(text=f"Your BMI score : {int(BMI)} Over Weight"))
                print(resualt_lable.place(y=160, x=80))

            elif 30 <= BMI <= 34.9:
                print(resualt_lable.config(text=f"Your BMI score : {int(BMI)} OBESITY (CLASS 1)"))
                print(resualt_lable.place(y=160, x=80))

            elif 35.0 <= BMI <= 39.9:
                print(resualt_lable.config(text=f"Your BMI score : {int(BMI)} OBESITY (CLASS 2)"))
                print(resualt_lable.place(y=160, x=80))

            else:
                print(resualt_lable.config(text=f"Your BMI score : {int(BMI)}  OBESITY (CLASS 3)"))
                print(resualt_lable.place(y=160, x=80))
    except ValueError:
        print (resualt_lable.config(text="Please entry intiger number"))
        print(resualt_lable.place(y=160, x=80))








my_button= tkinter.Button(text="Calculator",command=calculator)
my_button.place(y=120,x=117)




tkinter.mainloop()