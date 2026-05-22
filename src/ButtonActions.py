"""
All the various actions and doodads that spring into play once a button is pressed
"""

from natsort import natsorted
from tkinter import filedialog
from pathlib import Path
import tkinter as Tk
import os


#This dict gets populated after InitialiseElements.py has created the Widgets
FramesDict = {}

#This dict stores all file tag data as {current filename: updated filename}
DictOfSongNames = {}

#The directory from which the files are sourced
SOURCEPATH = ""

def OverwriteTextField(Frame, NewText):
    #Unified function to clear and then overwrite the input field of a TextBox
    Frame.delete("1.0", Tk.END)
    Frame.insert(Tk.END, NewText)


def UpdateSource():
    #Update the absolute filepath from where to source files
    global SOURCEPATH

    SOURCEPATH = filedialog.askdirectory(title="Select Source Directory")

    if SOURCEPATH != "":
        #Catch check if the opening of a directory is cancelled
        OverwriteTextField(FramesDict["SourcePathBox"], SOURCEPATH)
        ShowFoundFiles(SOURCEPATH)


def ShowFoundFiles(SourceDirectoryPath):
    #List all the audio files found in the source directory, also create a dict to preview renamed files

    #Make sure to start with clean slate dicts to avoid issues down the line
    DictOfSongNames.clear()

    #Temporary list of song names for sorting
    UnsortedSongs = []

    #Clear the filename frames of all data
    for Frame in ["FoundFilesBox", "EditFilesBox"]:
        OverwriteTextField(FramesDict[Frame], "")

    if Path(SourceDirectoryPath).is_dir():
        for File in os.listdir(SourceDirectoryPath):
            #Fie type is checking by checking the extension after the first period, forced lowercase
            if File.split('.')[-1].lower() in ["flac", "mp3"]:
                UnsortedSongs.append(File)
                
    for Song in natsorted(UnsortedSongs):
        DictOfSongNames[Song] = Song
        FramesDict["FoundFilesBox"].insert(Tk.END, Song + "\n")
        

def GetCharIndex():
    #Grab the value stored at the char index text box and use that to edit the new filenames

    ReadInIndexStart = FramesDict["CharIndexCutoffBox"].get('1.0', Tk.END)
    ReadInIndexEnd   = FramesDict["CharIndexLimitBox"].get('1.0', Tk.END)

    try:
        #If the cutoffs are valid, update the previewed names
        i_CharStart = int(ReadInIndexStart)
        i_CharEnd   = int(ReadInIndexEnd)

        #File extension to add to the chopped up name in the most heinous way imaginable
        #Sometimes I just write monstrous code and I do not care if God will forgive me
        FileExtension = "." + list(DictOfSongNames.keys())[0].split('.')[-1]

        #A silly way to cut files names with double digit song track listings correctly
        TrackNumber = 0

        #Dumb little false state check
        if len(DictOfSongNames) == 0:
            OverwriteTextField(FramesDict["MessageBox"], "No files to rename!")
        else:
            for Filename in DictOfSongNames:
                #This gets rid of leading zeroes if song titles are listed as "01 - Song" instead of "1 - Song"
                ZeroCounter = 1 if Filename[0] == "0" else 0

                #This counter essentially controls how much of the filename to snip off
                #  "1.- Song Title" and "10.- Song Title" differ by exactly 1 index
                #  The weird boolean dance is just to make sure to keep names as is when no cutting is required
                TrackNumber += 1
                DictOfSongNames[Filename] = Filename[ZeroCounter + i_CharStart + bool(bool(i_CharStart) * (TrackNumber // 10)):-(i_CharEnd + len(FileExtension))] + FileExtension
   
        
        UpdateNamePreviews(DictOfSongNames)
    except:
        #Display an error warning when, for some reason, the cutoff fails
        OverwriteTextField(FramesDict["MessageBox"], "Invalid cutoff")


def UpdateNamePreviews(PreviewedNames):
    #Take the previewed names dict and list them in the preview screen
    OverwriteTextField(FramesDict["EditFilesBox"], "")

    for File in PreviewedNames:
        FramesDict["EditFilesBox"].insert(Tk.END, PreviewedNames[File] + "\n")


def GetFieldData():
    #Collect all the data entered in the tag text boxes and turn them into executable commands

    AllTagData = []
    for Frame in ["TPE1Box", "TALBBox", "TYERBox", "TCONBox"]:
        PulledFieldData = (FramesDict[Frame].get('1.0', Tk.END)).replace("\n", "")
        
        #Only add tags that aren't left empty
        if PulledFieldData != "":
            #TYER and TRCK tags take ints, not strings, so handle TYER separately
            if Frame != "TYERBox":
                #Lobbing 'Box' off Frame to double as the actual tag
                CommandString = " --" + Frame[:-3] + " \"" + PulledFieldData + "\""
            else:
                CommandString = " --" + Frame[:-3] + " " + PulledFieldData

            AllTagData.append(CommandString)

    return AllTagData


def RunTaggingCommand(ListOfSharedTags):
    #Actually run the shell command, golly

    #This just keeps track of the track listing
    IncrementTrack = 1

    for File in DictOfSongNames:

        #This will build the entire command to send to the shell
        #It's a stupid way of doing it, but it is mine and it works, so I do not care
        CommandString = "id3v2"

        #Add the shared tags (Artist/Album/Year/Genre)
        for TaggedCommand in ListOfSharedTags:
            CommandString += TaggedCommand

        #Add the track number
        CommandString += (" --TRCK " + str(IncrementTrack))

        #Set the song name - remember to remove the file extension
        CommandString += (" -t \"" + DictOfSongNames[File].split('.')[0] + "\"")

        #Set the source file
        CommandString += " \"" + SOURCEPATH + "/" + File + "\""

        #Issue the command
        os.system(CommandString)

        IncrementTrack += 1


def CreateNewSongNameDict():
    #Once files have been renamed and tagged, show the updated names and set up a new Dict

    UpdatedDict = {}

    #Construct a new Dict of {New Name : New Name}
    for Entry in DictOfSongNames:
        UpdatedDict[DictOfSongNames[Entry]] = DictOfSongNames[Entry]
    
    #Reconstruct DictOfSongNames
    DictOfSongNames.clear()
    for Line in UpdatedDict:
        DictOfSongNames[Line] = Line


def StartTagging():
    #Begin the process of querying the text fields for data, renaming the file names and setting the ID3 tags

    #Change the default linux move command if running on windows
    MoveCommand = "mv \""
    if os.name == "nt":
        MoveCommand  = "move \""

    #Another dumb little false state check
    if len(DictOfSongNames) == 0:
        OverwriteTextField(FramesDict["MessageBox"], "No files to tag!")
    else:
        #Collect the data shared amongst all files (artist, album, year, genre)
        AllTagData = GetFieldData()

        #Tag all the files
        OverwriteTextField(FramesDict["MessageBox"], "Tagging files...")
        RunTaggingCommand(AllTagData)

        #Rename the files, doing something funky with mv/move
        OverwriteTextField(FramesDict["MessageBox"], "Renaming files...")
        for File in DictOfSongNames:
            os.system(MoveCommand + SOURCEPATH + "/" + File + "\" \"" + SOURCEPATH + "/" + DictOfSongNames[File] + "\"")

        #Lastly, reset the Dict and update the FoundFilesBox to reflect the change in names
        CreateNewSongNameDict()
        OverwriteTextField(FramesDict["FoundFilesBox"], "")
        for File in DictOfSongNames:
            FramesDict["FoundFilesBox"].insert(Tk.END, DictOfSongNames[File] + "\n")
        
        OverwriteTextField(FramesDict["MessageBox"], "Done!")