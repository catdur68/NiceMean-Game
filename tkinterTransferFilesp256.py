import tkinter as tk
from tkinter import *
from tkinter import filedialog, messagebox
import os
import shutil
from time import *
import datetime

#this program's purpose is to let the user pick a folder from a directory
#and move its content to another folder of his/her choice based on modified/created date
#We will use UI (tkinter) with # 2 text boxes, 1 label for each, 1 button for each, and add'l Copy and Exit buttons




#set up GUI
class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__(self,master)
        self.master = master
        #self.master.minsize(800, 300)# Height, Width
        #self.master.maxsize(800, 300)
        #self.master.resizable(width=False, height=False)
        #Creates a title for the main frame
        self.master.title("Move Files...")
        self.master.config(bg="#F0F0F0")
        #that was the code for the basic Tkinter window

#Source Section = 1 label, 1 button, 1 text box.
        #Pressing the button will box pop up a tkinter file directory. 
        #The user select a folder (after clicking the browse button).
        #The path of the selected source folder is returned in the entry box. 
        self.lbl_From = tk.Label(self.master, text="...FROM")
        self.lbl_From.grid(row=0, column=0, padx=(27,0), pady=(13,5),sticky=N+W)
                                  
        self.btn_browse1 = tk.Button(self.master, width=12, height=1, text="Browse from", command=self.openFromDirectory)
        self.btn_browse1.grid(row=0, column=1, padx=(10, 0), pady=(10,0),sticky=W)

        self.txt_1stEntry = tk.Entry(self.master, width = 100, text="")
        self.txt_1stEntry.grid(row=0, column=2, padx=(7, 50), pady=(10,0),sticky=E)

#Destination Section = 1 label, 1 button, 1 text box.
        #Text box receives the path of the selected destination directory 
        self.lbl_To = tk.Label(self.master, text="...TO")
        self.lbl_To.grid(row=1, column=0, padx=(27,0), pady=(13,5),sticky=N+W)
                                  
        self.btn_browse2 = tk.Button(self.master, width=12, height=1, text="Browse to", command=self.openToDirectory)
        self.btn_browse2.grid(row=1, column=1, padx=(10, 0), pady=(10,0),sticky=W)

        self.txt_2ndEntry = tk.Entry(self.master, width = 100, text="")
        self.txt_2ndEntry.grid(row=1, column=2, padx=(7, 50), pady=(10,0),sticky=E)

#creates the last 2 buttons (Copy Files, Exit Program)
        self.btn_Copy = tk.Button(self.master, width=25, height=2, text="Copy Files to destination...", command=self.CopyFiles)
        self.btn_Copy.grid(row=2, column=2, padx=(5, 20), pady=(20,30),sticky=W)

        self.btn_close = tk.Button(self.master, width=15, height=2, text="EXIT", command=self.exit)
        self.btn_close.grid(row=2, column=2, padx=(0, 50), pady=(20,30),sticky=SE)


#Define 4 functions: Select Directory Button (for Browse1, Browse2), Copy, and exit App
    def openFromDirectory(self):
        #opens file explorer (tkinter version) at the current directory
        folder_rel_path = filedialog.askdirectory()
        folder = os.path.abspath(folder_rel_path) # ok, working
        # & allows selection of a folder
        #need to pass that value (path/folder) to self_txt_1stEntry in the mainframe - that is we want to insert into the entry box
        self.txt_1stEntry.insert(0,folder) # insert at beginning of text box
        #that Entry text box now contains the path to the SOURCE folder where the files are
        #create filter to only show files changed/modified TODAY

    def openToDirectory(self):
        folder_rel_path = filedialog.askdirectory()
        folder = os.path.abspath(folder_rel_path) #absolue path of the FOLDER!!!! 
        self.txt_2ndEntry.insert(0,folder)
        #that Entry text box now contains the path to the DESTINATION folder where the files will be copied

    def CopyFiles(self):
        #assign selected source and destination folders to their respective variables with get()
        source = self.txt_1stEntry.get()
        #print(source) # fullpath OF THE FOLDER!!!!
        destination = self.txt_2ndEntry.get()
        #print(destination) # fullpath OF THE FOLDER!!!!
        grab_date = datetime.datetime.now()
        today = grab_date.strftime('%Y-%m-%d')
        #print("today is: ", today)
        
        
        files = os.listdir(source)
        print(files) #this is only returning filenames with extentions
        
        for file in files:
            fullpath = os.path.join(source, file)# FOLDER + FILENAME WITH EXTENSION
            #print(fullpath)
            #check file created/modified date
            created_On = os.path.getmtime(fullpath)
            local_time = datetime.datetime.fromtimestamp(created_On)
            date_created = local_time.strftime('%Y-%m-%d')
            if (date_created == today):
               #make a copy of the file created/modified TODAY in the selected destination folder 
               shutil.copy(fullpath, destination)

    def exit(self): #if cancel is pressed, we want the window to close
        self.master.destroy()
        

        
if __name__ =="__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
    
   
