from tkinter import *
import time
import tkinter.messagebox
from csvgui import response
import threading

saved_username = ["You"]
window_size="500x500"
text = ''
class ChatInterface(Frame):   
    
    def __init__(self, master=None):
        global text
        icon1=PhotoImage(file="voice image.png")
        icon2 = icon1.subsample(16,16)
        
        Frame.__init__(self, master)
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


a = ChatInterface(root)
root.geometry(window_size)
root.title("csvgui")
root.iconbitmap('favicon.ico')
root.mainloop()
