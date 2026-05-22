"""
This overengineered tkinter script is meant to act as a front-end to ID3v2
Mainly so I can tag audio files in peace without ever having to interact with a spooky CLI

It also cuts down the filename, getting rid of leading strings like track number and album title
"""

import InitialiseElements as IE
import ButtonFrames as BF

def main():
    #Create the Main window
    MainWindow = IE.CreateWindow(680, 345, "ID3v2 lazy GUI")

    #Create TextBox frames
    #This also populates the FramesDict in ButtonActions.py
    #  linking the actions to their relevant frames
    IE.SetupWindowTextBoxes(MainWindow)

    #Now that the frames exist, the button actions can be updated with the relevant command
    BF.ButtonFrames["SourceSelect"].Baction = IE.BA.UpdateSource
    BF.ButtonFrames["GetCharIndex"].Baction = IE.BA.GetCharIndex
    BF.ButtonFrames["CutAndEncode"].Baction = IE.BA.StartTagging

    #Create and populate the buttons
    AllButtons = {}
    for Button in BF.ListOfButtons:
        ButtonData = BF.ButtonFrames[Button]
        #Create
        AllButtons[Button] = IE.BA.Tk.Button(MainWindow, text=ButtonData.Btext, padx=ButtonData.Bpadx, command=ButtonData.Baction)
        #Populate
        AllButtons[Button].grid(row=ButtonData.Brow, column=ButtonData.Bcol, columnspan=ButtonData.Bcolspan, rowspan=ButtonData.Browspan, sticky=ButtonData.Bsticky)

    #Create Labels
    for FrameLabel in IE.WF.ListOfLabels:
        IE.CreateTextLabel(MainWindow, IE.WF.WidgetFrames[FrameLabel])

    MainWindow.mainloop()


if __name__ == "__main__":
    main()
