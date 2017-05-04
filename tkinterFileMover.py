from tkinter import *
from tkinter import ttk as ttk, messagebox, filedialog
from datetime import datetime, timedelta
from glob import glob
import os
import time
import shutil



class FileCheck:

    def __init__(self, master):

        self.frameHeader = ttk.Frame(master)
        self.frameHeader.pack()
        
        #Daily Folder
        self.chooseFolderName = StringVar()
        print (self.chooseFolderName)
        self.daily = (self.chooseFolderName.get())
        
        #Destination Folder
        self.destFolderName = StringVar()
        print (self.destFolderName)
        self.dest = (self.destFolderName.get())

        #Frame
        self.frameSteps = ttk.Frame(master)
        self.frameSteps.pack()

        #Labels
        titleLabel = ttk.Label(self.frameHeader, text = 'UI for File Transfer project - Python 3.4 - IDLE ', font = 'bold')
        titleLabel.grid(row = 0, column = 0, columnspan = 2, pady = 5, sticky = 'W')
        dailyStepLabel = ttk.Label(self.frameSteps, text = '1) Choose a Starting Folder')
        dailyStepLabel.grid(row = 0, column = 0, columnspan = 2, pady = 5, sticky = 'W')
        destStepLabel = ttk.Label(self.frameSteps, text = '2) Choose a Destination Folder')
        destStepLabel.grid(row = 3, column = 0, columnspan = 2, pady = 5, sticky = 'W')
        initiateStepLabel = ttk.Label(self.frameSteps, text = '3) Run Manual File Check')
        initiateStepLabel.grid(row = 7, column = 0, columnspan = 2, pady = 5, sticky = 'W')
        
        #Buttons   
        dailyButton = ttk.Button(self.frameSteps, text = 'Start Folder', command = self.chooseStartFolder)
        dailyButton.grid(row = 1, column = 1, sticky = 'W')
        destButton = ttk.Button(self.frameSteps, text = 'Destination Folder', command = self.chooseDestFolder)
        destButton.grid(row = 4, column = 1, sticky = 'W')
        initiateButton = ttk.Button(self.frameSteps, text = 'Initiate File Check', command = lambda: self.fileMover(self.filesStart,self.filesEnd))
        initiateButton.grid(row = 8, column = 1, sticky = 'W')
        
        #Paths
        self.framePath = ttk.Frame(master)
        self.framePath.pack()
        dailyPathLabel = ttk.Label(self.frameSteps, text = self.chooseFolderName, textvariable = self.chooseFolderName)
        dailyPathLabel.grid(row = 1, column = 2, rowspan = 1, sticky = 'W')
        destPathLabel = ttk.Label(self.frameSteps, text = self.destFolderName, textvariable = self.destFolderName)
        destPathLabel.grid(row = 4, column = 2, rowspan = 1, sticky = 'W')
        
        
    def chooseStartFolder(self):
        self.filesStart = filedialog.askdirectory(initialdir = "/Users/seanbass/Desktop", title = "Choose Starting Folder")
        self.chooseFolderName.set(self.filesStart)
        print (self.filesStart)
        print (self.chooseFolderName.get())
        
      
    def chooseDestFolder(self):
        self.filesEnd = filedialog.askdirectory(initialdir = "/Users/seanbass/Desktop", title = "Choose Destination Folder")
        self.destFolderName.set(self.filesEnd)
        print (self.filesEnd)
        print (self.destFolderName.get())


    #The File Mover
    def fileMover(self, filesStart, filesEnd):
        print (format(filesStart))
        print (format(filesEnd)) 
        timeNow = datetime.now()
        oneDayOld = timeNow - timedelta(hours = 24)
        for f in os.listdir(filesStart): 
            files = os.path.realpath(os.path.join(filesStart,f))
            if files.endswith('.txt'):
                filesToMove = datetime.fromtimestamp(os.path.getmtime(files)) 
                if filesToMove > oneDayOld: 
                    print (files, "Copied: ", filesEnd)
                    shutil.copy(files,filesEnd)
                else:
                    print (files, "not copied")
                    


def main():
    root = Tk()
    root.title("File Check")
    root.minsize(400, 280)
    filecheck = FileCheck(root)
    root.mainloop()

if __name__ == '__main__' : main()

