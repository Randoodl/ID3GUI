"""
Initialise the Main Window, Frame Widgets and Button Widgets
"""

import WidgetFrames as WF 
import ButtonActions as BA

from tkinter import scrolledtext


def CreateWindow(WindowWidth, WindowHeight, WindowTitle):
    #Create the main window to attach widgets to, returns window
    Main = BA.Tk.Tk()
    Main.title(WindowTitle)
    Main.geometry(str(WindowWidth) + "x" +  str(WindowHeight))
    Main.resizable(False, False)
    
    return Main


def CreateTextBox(Main, WFrame, ScrollState):
    #Create a non-interactive box to display text, optionally scrollable

    #Determine whether or not to add a scrollbar
    if ScrollState:
        TextBox = scrolledtext.ScrolledText(Main, height=WFrame.WFheight, width=WFrame.WFwidth, wrap=BA.Tk.WORD)
    else:
        TextBox = BA.Tk.Text(Main, height=WFrame.WFheight, width=WFrame.WFwidth, wrap=BA.Tk.WORD)

    #Populate to main window    
    TextBox.grid(row=WFrame.WFrow, column=WFrame.WFcol, columnspan=WFrame.WFcolspan, sticky=WFrame.WFsticky)

    return TextBox


def CreateTextLabel(Main, WFrame):
    #Create labels and populate them to the main window
    TextLabel = BA.Tk.Label(Main, text= WFrame.WFlabeltext)
    TextLabel.grid(column=WFrame.WFcol, row=WFrame.WFrow, columnspan=WFrame.WFcolspan, sticky=WFrame.WFsticky)


def SetupWindowTextBoxes(MainWindow):
    #Create all the on-screen text boxes and populate the dict in ButtonActions to interact with them

    SourcePathBox      = CreateTextBox(MainWindow, WF.WidgetFrames["SourcePathBox"], False)
    FoundFilesBox      = CreateTextBox(MainWindow, WF.WidgetFrames["FoundFilesBox"], True)
    EditFilesBox       = CreateTextBox(MainWindow, WF.WidgetFrames["EditFilesBox"], True)
    CharIndexCutoffBox = CreateTextBox(MainWindow, WF.WidgetFrames["CharIndexCutoffBox"], False)
    CharIndexLimitBox  = CreateTextBox(MainWindow, WF.WidgetFrames["CharIndexLimitBox"], False)
    TPE1Box            = CreateTextBox(MainWindow, WF.WidgetFrames["TPE1Box"], False)
    TALBBox            = CreateTextBox(MainWindow, WF.WidgetFrames["TALBBox"], False)
    TYERBox            = CreateTextBox(MainWindow, WF.WidgetFrames["TYERBox"], False)
    TCONBox            = CreateTextBox(MainWindow, WF.WidgetFrames["TCONBox"], False)
    MessageBox         = CreateTextBox(MainWindow, WF.WidgetFrames["MessageBox"], False)

    BA.FramesDict = {"SourcePathBox" : SourcePathBox, "FoundFilesBox" : FoundFilesBox, "EditFilesBox" : EditFilesBox, 
                     "CharIndexCutoffBox" : CharIndexCutoffBox, "CharIndexLimitBox" : CharIndexLimitBox,
                     "TPE1Box" : TPE1Box, "TALBBox" : TALBBox, "TYERBox" : TYERBox, "TCONBox" : TCONBox, "MessageBox" : MessageBox}



