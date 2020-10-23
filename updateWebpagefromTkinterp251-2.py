import tkinter
from tkinter import *
import webbrowser


'''this will only work if user has access to the same directory as programmer. If that is the case, the webpage opens at the same time
as the GUI in the background, and the user can see what is currently on the webpage.
f = open("index.html", 'r')
f.read()
f.close()
webbrowser.open('index.html', new=2)
''' 

#standard 3 first lines of code
class ParentWindow(Frame):
    #the Frame = parent class from TKinter
    def __init__ (self, master):
        Frame.__init__(self)
        self.master = master
        # self is like a key to all the widgets within the class
        #from now on we can start referencing Frame as master, and the class as self
        # it is possible to add **args or **kwargs to the init parameters
#Customize Main frame
        #Not used - self.master.geometry("{}x{}".format(700, 400))
            # if used: we would be fixing the window to 700 pixels by 400 pixels
            # here we are letting tkinter decides
        self.master.title("Update Webpage")
        #The window will have that title
        self.master.config(bg="lightgray")
        #that was the code for the basic Tkinter window

#Create Widgets: 1 label, 1 entry box, 1 open button,  1 update button
        self.lbl_instructions = Label(self.master, text="Enter content to be posted to the webpage in the box below: ", font=("hevetica", 16), fg="black", bg="lightgray")
        #this instantiate a label
        self.lbl_instructions.grid(row=0,column=0, padx=(30,0),pady=(30,0), sticky=W)
        #this positions the label on the window
#User Input
        self.varContent = StringVar()
        self.entry_content = Entry(self.master, text = self.varContent, width = 50, font=("hevetica", 16), fg="black", bg="white")
        self.entry_content.grid(row=1, column=0, padx=(20,20),pady=(10,20))
#buttons
        #self.btnOpen = Button(self.master, text="Open URL", width=15, height=1, command=self.open)
        #self.btnOpen.grid(row=2,column=0, padx=(50,0),pady=(60,0), sticky=W)
        #open button not needed because I am making the website open automatically with the GUI, so user can view what is already on the page
        self.btnSubmit = Button(self.master, text="Submit Changes", width=15, height=1, command=self.submit)
        #the command function is what gives the buttton something to do - not defining the function makes the button disappear
        self.btnSubmit.grid(row=2,column=0, padx=(0,0),pady=(15,10))
        self.btnClose = Button(self.master, text="Cancel", width=15, height=1, command=self.cancel)
        self.btnClose.grid(row=2,column=0, padx=(0,20),pady=(15,10), sticky=E)

#Button Activations
    def cancel(self): #if cancel is pressed, we want the window to close
        self.master.destroy()

    
    def submit(self): #this is the function definition for the command in the buttons
        #this submit button is part of the class root (main window) therefore submit(self) where self is the class, submit the method
        NewContent = self.varContent.get()# this will go get the value stored in that variable at the time the button is pressed
        #post content to website
        #f.close("index.html") - not needed because the page is not currently open
        f=open("index.html", 'w')
        #f.write= ("<html><body><h1>%s</h1></body></html>") % (NewContent)
        #f.write("<html><body><h1>",{}.format(NewContent), "</h1></body></html>")
        #f.write("<html><body><h1><%"{}".format(NewContent)%></h1></body></html>")
        #f.write("<html><body><h1><script>"{}".format(NewContent)<script></h1></body></html>")
        f.write("<html><body><h1>{}</h1></body></html>".format(NewContent))
        f.close
        webbrowser.open('index.html',new=2)
            


if __name__ == "__main__":
    root = Tk() #this instantiate the class and we name it root
    App = ParentWindow(root)#this opens the window
    root.mainloop()#without this code the window opens and closes immediately. This code opens it continuously





