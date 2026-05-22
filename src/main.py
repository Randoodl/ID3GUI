"""
Copyright (c) 2026, Dylan Ooijevaar

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""


"""
This overengineered tkinter script is meant to act as a front-end to ID3v2
Mainly so I can tag audio files in peace without ever having to interact with a spooky CLI
It also cuts down the filename, getting rid of leading strings like track number and album title

It is a terrible way of doing this, but I made the mistake of starting out this small project, and now I have got to stick with it
"""

import InitialiseElements as IE
import ButtonFrames as BF

def main():
    #Create the Main window
    MainWindow = IE.CreateWindow(730, 410, "ID3GUI - Lazy GUI for id3v2")

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
