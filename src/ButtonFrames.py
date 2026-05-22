"""
Class to contain all button information
"""

class ButtonFrame:
    def __init__(self, Btext, Bpadx, Bcol, Brow, Bcolspan, Browspan, Bsticky, Baction):
        self.Btext    = Btext
        self.Bpadx    = Bpadx
        self.Bcol     = Bcol
        self.Brow     = Brow
        self.Bcolspan = Bcolspan
        self.Browspan = Browspan
        self.Bsticky  = Bsticky
        self.Baction  = Baction


ButtonFrames = {
    #                           Text                Padx   Col   Row   ColSp   RowSpan   Sticky    Action (Overwritten later)
    "SourceSelect": ButtonFrame("Open Directory",   0,     0,    0,    2,      1,        "EW",     print),
    "GetCharIndex": ButtonFrame("Isolate title",    0,     7,    4,    3,      1,        "EW",     print),
    "CutAndEncode": ButtonFrame("Cut and Encode",   0,     7,    6,    3,      4,        "NESW",   print),
}

ListOfButtons = ["SourceSelect", "GetCharIndex", "CutAndEncode"]