"""
Class to contain all widget information
"""


class WidgetFrame:
    def __init__(self, WFwidth, WFheight, WFcol, WFrow, WFcolspan, WFsticky, WFlabeltext):
        self.WFwidth     = WFwidth
        self.WFheight    = WFheight
        self.WFcol       = WFcol
        self.WFrow       = WFrow
        self.WFcolspan   = WFcolspan
        self.WFsticky    = WFsticky
        self.WFlabeltext = WFlabeltext


WidgetFrames = {
    #                                  Width  Height  Col   Row  ColSp   Sticky    Label
    "SourcePathBox":       WidgetFrame(64,    1,      2,    0,   8,      "EW",     ""),
    "FoundFilesLabel":     WidgetFrame(40,    1,      0,    1,   5,      "EW",     "Source files:"),
    "FoundFilesBox":       WidgetFrame(40,    9,      0,    2,   5,      "EW",     ""),
    "EditFilesLabel":      WidgetFrame(40,    1,      5,    1,   5,      "EW",     "Title Preview:"),
    "EditFilesBox":        WidgetFrame(40,    9,      5,    2,   5,      "EW",     ""),
    "RenameLabel":         WidgetFrame(20,    1,      0,    3,   10,     "W",     " Isolating the title string from the file name:"),
    "CharIndexCutoffBox":  WidgetFrame(15,    1,      2,    4,   2,      "W",      ""),
    "CharIndexLimitBox":   WidgetFrame(15,    1,      5,    4,   2,      "W",      ""),
    "CharCutoffLabel":     WidgetFrame(16,    1,      0,    4,   2,      "W",      "   Leading characters: "),
    "CharLimitLabel":      WidgetFrame(16,    1,      4,    4,   1,      "W",      " Trailing characters: "),
    "TagLabel":            WidgetFrame(16,    1,      0,    5,   1,      "W",      " Tag setup:"),
    "TPE1Label":           WidgetFrame(16,    1,      0,    6,   2,      "E",     " Artist:"),
    "TPE1Box":             WidgetFrame(46,    1,      2,    6,   5,      "EW",     ""),
    "TALBLabel":           WidgetFrame(16,    1,      0,    7,   2,      "E",     " Album:"),
    "TALBBox":             WidgetFrame(46,    1,      2,    7,   5,      "EW",     ""),
    "TYERLabel":           WidgetFrame(16,    1,      0,    8,   2,      "E",     " Year:"),
    "TYERBox":             WidgetFrame(46,    1,      2,    8,   5,      "EW",     ""),
    "TCONLabel":           WidgetFrame(16,    1,      0,    9,   2,      "E",     " Genre:"),
    "TCONBox":             WidgetFrame(46,    1,      2,    9,   5,      "EW",     ""),
    "MessageBox":          WidgetFrame(64,    1,      0,    10,   10,     "EW",     "")
}

ListOfLabels      = ["FoundFilesLabel", "EditFilesLabel", "RenameLabel", "CharCutoffLabel", "CharLimitLabel", "TagLabel", "TPE1Label", "TALBLabel", "TYERLabel", "TCONLabel"]