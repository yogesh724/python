from  tkinter import * 
root =Tk()
root.geometry("500x300")

def getvals():
    print("Accepted")

Label(root,text="regration form",font="ar 15 bold").grid(row=0,column=3)
#field name
name = Label(root, text="Name")
phone = Label(root, text="Phone")
gender = Label(root, text="Gender")
emergency = Label(root, text="Emergency")
payment = Label(root, text="Payment")
#packing fields
name.grid(row=1,column=2)
phone.grid(row=2,column=2)
gender.grid(row=3,column=2)
emergency.grid(row=4,column=2)
payment.grid(row=5,column=2)
#variable for storing data
namevalue =StringVar
phonevalue =StringVar
gendervalue =StringVar
emergencyvalue =StringVar
paymentvalue =StringVar
checkvalue = IntVar
#creating entry field
nameentry =Entry(root, textvariable =namevalue)
phoneentry =Entry(root, textvariable =phonevalue)
genderentry =Entry(root, textvariable =gendervalue)
emergencyentry =Entry(root, textvariable =gendervalue)
paymententry =Entry(root, textvariable =paymentvalue)
#packing entry field
nameentry.grid(row=1,column=3)
phoneentry.grid(row=2,column=3)
genderentry.grid(row=3,column=3)
emergencyentry.grid(row=4,column=3)
paymententry.grid(row=5,column=3)

#creating checkbox
checkbtn = Checkbutton(text="remember me?",variable =checkvalue)
checkbtn.grid(row=6, column=3)

#submit button
Button(text="submit",command=getvals).grid(row=7, column=3)

root.mainloop()



