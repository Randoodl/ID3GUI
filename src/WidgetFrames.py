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
    "EditFilesLabel":      WidgetFrame(40,    1,      5,    1,   5,      "EW",     "Rename files:"),
    "EditFilesBox":        WidgetFrame(40,    9,      5,    2,   5,      "EW",     ""),
    "CharIndexCutoffBox":  WidgetFrame(64,    1,      0,    3,   7,      "W",      ""),
    "TPE1Label":           WidgetFrame(16,    1,      0,    4,   2,      "EW",     "Artist:"),
    "TPE1Box":             WidgetFrame(46,    1,      2,    4,   6,      "W",      ""),
    "TALBLabel":           WidgetFrame(16,    1,      0,    5,   2,      "EW",     "Album:"),
    "TALBBox":             WidgetFrame(46,    1,      2,    5,   6,      "W",      ""),
    "TYERLabel":           WidgetFrame(16,    1,      0,    6,   2,      "EW",     "Year:"),
    "TYERBox":             WidgetFrame(46,    1,      2,    6,   6,      "W",      ""),
    "TCONLabel":           WidgetFrame(16,    1,      0,    7,   2,      "EW",     "Genre:"),
    "TCONBox":             WidgetFrame(46,    1,      2,    7,   6,      "W",      "")
}

ListOfLabels      = ["FoundFilesLabel", "EditFilesLabel","TPE1Label", "TALBLabel", "TYERLabel", "TCONLabel"]