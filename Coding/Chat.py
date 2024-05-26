from tkinter import *
root=Tk()
def send():
    send="You => "+e.get()
    txt.insert(END,"\n"+send)
    if(e.get()=="hello"):
        txt.insert(END,"\n"+"Bot => Hi how can i help you?")
    elif(e.get()=="hi"):
        txt.insert(END,"\n"+"Bot => Hello how can i help you?")
    elif(e.get().find("profile")>=0):
        txt.insert(END,"\n"+"Bot => Name: Mahesh"+"\n\t"+"Email: umahesh987654321@gmail.com"+"\n\t"+"Age: 21"+"\n\t"+"Phone Number: 8143099143"+"\n\t"+"Researches Completed: 14"+"\n\t"+"Designation: Ph.d"+"\n\t"+"Researches Ongoing: 5")
    elif(e.get()=="fine"):
        txt.insert(END,"\n"+"Bot => Thank You , do you want me to help anyting?")
    else:
        if(e.get()=="hello"):
            txt.insert(END,"\n"+"Bot => Hi")
    e.delete(0,END)
txt=Text(root)
txt.grid(row=0,column=0,columnspan=1)
e=Entry(root,width=100)
send=Button(root,text="Send",command=send).grid(row=1,column=1)
e.grid(row=1,column=0)
root.title("CHATBOT")
root.mainloop()