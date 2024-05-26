from tkinter import *
import time
import tkinter.messagebox
#from csvgui import response
import threading

saved_username = ["You"]
window_size="690x420"
text = ''
class ChatInterface(Frame):   
    
    def init(self, master=None):
        global text
        Frame.init(self, master)
        self.master = master
        self.tl_bg = "black"
        self.tl_bg2 = "black"
        self.tl_fg = "black"
        self.font = "Verdana 10"
        menu = Menu(self.master)
        self.master.config(menu=menu, bd=5,bg="black")
        self.text_frame = Frame(self.master, bd=6,bg="black")
        self.text_frame.pack(expand=True, fill=BOTH)
        self.text_box_scrollbar = Scrollbar(self.text_frame, bd=0)
        self.text_box_scrollbar.pack(fill=Y, side=RIGHT)
        self.text_box = Text(self.text_frame, yscrollcommand=self.text_box_scrollbar.set, state=DISABLED,
                             bd=1, padx=4, pady=4, spacing3=8, wrap=WORD, bg="black", font="Verdana 10", relief=GROOVE,
                             width=10, height=1,fg="white")
        self.text_box.pack(expand=True, fill=BOTH)
        self.text_box_scrollbar.config(command=self.text_box.yview)
        self.entry_frame = Frame(self.master, bd=1,bg="black")
        self.entry_frame.pack(side=LEFT, fill=BOTH, expand=True)
        self.entry_field = Entry(self.entry_frame, bd=1, justify=LEFT)
        self.entry_field.pack(fill=X, padx=4, pady=4, ipady=3)
        
        self.send_button_frame = Frame(self.master, bd=0)
        self.send_button_frame.pack(fill=None)
        self.send_button = Button(self.send_button_frame, text="Text", width=5, relief=GROOVE, bg='white',
                                  bd=1, command=lambda: self.send_message_insert(1,None), activebackground="#FFFFFF",
                                  activeforeground="#000000")
        
        
        self.send_button_frame2 = Frame(self.master, bd=0)
        self.send_button_frame2.pack(fill=BOTH)
        self.send_button2 = Button(self.send_button_frame2, text ='voice', width=5, relief=GROOVE, bg='white',
                                  bd=2, command=lambda: self.send_message_insert(2,None), activebackground="#FFFFFF",
                                  activeforeground="#000000")
        #self.send_button2.config(image=icon1)

        
        self.send_button.pack(side=LEFT, ipady=8)
        self.send_button2.pack(side=LEFT, ipady=8)
        self.master.bind("<Return>", self.send_message_insert)


       
        
    
    def chatexit(self):
        exit()
    
    def send_message_insert(self,id, message):
        user_input = self.entry_field.get()
        pr1 = "User : " + user_input + "\n"
        self.text_box.configure(state=NORMAL)
        self.text_box.insert(END, pr1)
        self.text_box.configure(state=DISABLED)
        self.text_box.see(END)
        ob=response(user_input)
        pr="Bot : " + ob + "\n"
        self.text_box.configure(state=NORMAL)
        self.text_box.insert(END, pr)
        self.text_box.configure(state=DISABLED)
        self.text_box.see(END)
        self.entry_field.delete(0,END)
        time.sleep(0)
        
        
        
root=Tk()
def send():
    
    send="You : "+e.get()
    txt.insert(END,"\n"+send)
    if(e.get()=="hello" or e.get()=="hi"):
        txt.insert(END,"\n"+"Bot : Hello !!! Its great meeting you !")
    elif(e.get().find("tasks")>=0):
        txt.insert(END,"\n"+"Bot : 1. You need to submit test-1 marks by 4th October"+"\n\t"+"2. You need to publish a research paper by the end of this month")
    elif(e.get().find("pending")>=0):
        txt.insert(END,"\n"+"Bot : yet to publish reasearch paper")
    elif(e.get().find("profile")>=0):
        txt.insert(END,"\n"+"Bot :  Emp_id : 1521"+"\n\t"+"Name: Mahesh"+"\n\t"+"Email: umahesh987654321@gmail.com"+"\n\t"+"Age: 21"+"\n\t"+"Phone Number: 8143099143"+"\n\t"+"Publication Completed: 14"+"\n\t"+"Designation: Ph.d"+"\n\t"+"Researches Ongoing: 5")
    elif(e.get()=="fine" or e.get()=='thankq'):
        txt.insert(END,"\n"+"Bot : Thank You , do you want me to help anyting?")
    else:
        if(e.get()=="hello"):
            txt.insert(END,"\n"+"Bot : Hi")
        else:
            txt.insert(END,"\n"+"Bot : Meet you again")
    e.delete(0,END)
txt=Text(root)
txt.grid(row=0,column=0,columnspan=1)
e=Entry(root,width=100)
txt.insert(END,"\n"+"Bot : Hi how can i help you?")
send=Button(root,text="Send",command=send).grid(row=1,column=1)
e.grid(row=1,column=0)
a = ChatInterface(root)
root.geometry(window_size)
root.title("NextGenBot")
#root.iconbitmap('favicon.ico')
root.mainloop()