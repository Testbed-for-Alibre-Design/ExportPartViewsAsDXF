# Credit NateLiquidGravity https://www.alibre.com/forum/index.php?threads/script-release-export-part-views-as-dxf.24804/
from __future__ import division  # Ensures the division operation uses float division by default (e.g., 1 / 2 = 0.5)
import os  # Imports the os module to handle file paths and file operations
import clr  # Imports the Common Language Runtime interface
import _winreg  # Imports the module to interact with the Windows registry

# Function to retrieve the installation path of Alibre Design from the Windows registry
def getalibrepath():
    try:
        # Constructs a registry key string dynamically based on Alibre Design version
        keystring = r'SOFTWARE\Alibre, Inc.\Alibre Design' + '\\' + str(Global.Root.Version).split(' ')[1].replace(',', '.')
        hKey = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE, keystring)  # Opens the registry key
        result = _winreg.QueryValueEx(hKey, 'HomeDirectory')  # Retrieves the home directory value
        return result[0]  # Returns the directory path
    except Exception as e:
        try:
            # Tries a different registry path if the first fails
            hKey = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE, 'Software\\Alibre, Inc.\\Alibre Design')
            result = _winreg.QueryValueEx(hKey, 'HomeDirectory')
            return result[0]
        except Exception as e:
            # Handles any exceptions by informing the user of the failure
            print('\n')
            print('Could not get Alibre Path.')
            return ''

# Adds a reference to the AlibreX.dll file, which allows access to Alibre's API
clr.AddReferenceToFileAndPath(os.path.join(getalibrepath(), r'Program\AlibreX.dll'))

from AlibreX import ADUnits, ADDrawingViewType, ADDetailingOption, ADViewOrientation, IAD2DPoint, IADTransformation  # Imports specific classes from Alibre's API

Win = Windows()  # Creates an instance of the Windows class

def InputChanged(Index, Value):
    # Placeholder function for handling input changes; does nothing currently
    return

def ExportFaceDXF(Values):
    # Function to export the face of a part to a DXF file
    if Values[0] == None or Values[0] == '':
        # Checks if the part face is selected; if not, prints a message and returns
        print('No Face Selected.')
        return
    InputFace = Values[0]  # The selected face from the input
    if Values[1] == None or Values[1] == '':
        # Checks if the output file path is set; if not, prints a message and returns
        print('No Export File set.')
        return
    OutputFile = Values[1]  # The path for the output file
    if not os.path.splitext(OutputFile)[1]:
        # If the file extension is not set, add ".dxf"
        print('Extension not set for DXF Output File.\nAdding .dxf extension.')
        OutputFile = str(OutputFile) + '.dxf'
    if not os.path.splitext(OutputFile)[1] == '.dxf':
        # Ensures the file extension is ".dxf", otherwise prints an error message and returns
        print('Wrong extension for DXF File.')
        return
    print('Please Wait!')
    Root = Global.Root  # Accesses the global root object of Alibre API
    top_sess = Root.TopmostSession  # Gets the topmost session in Alibre
    part_path = InputFace.GetPart().FileName  # Gets the file name of the part
    my_drawing = Root.CreateEmptyDrawing('Hello World')  # Creates an empty drawing
    point_orgin = my_drawing.GeometryFactory.Create2DPoint(0.0,0.0)  # Creates a 2D point at the origin
    test_sheet = my_drawing.Sheets.ActiveSheet  # Gets the active sheet in the drawing
    # Modifies the sheet settings and creates standard views of the part
    test_sheet.ModifySheetBlank('Working Please Wait', 1.0, 1.0, ADUnits.AD_CENTIMETERS, 1.0, 1.0)
    test_sheet.CreateStandardViews(str(part_path), ADDrawingViewType.AD_STANDARD, ADDetailingOption.AD_TANGENT_EDGES, 1.0, 1.0, ADViewOrientation.AD_FRONT | ADViewOrientation.AD_BACK | ADViewOrientation.AD_LEFT | ADViewOrientation.AD_RIGHT | ADViewOrientation.AD_TOP | ADViewOrientation.AD_BOTTOM | ADViewOrientation.AD_TOP_LEFT | ADViewOrientation.AD_TOP_RIGHT | ADViewOrientation.AD_BOTTOM_LEFT | ADViewOrientation.AD_BOTTOM_RIGHT , point_orgin)
    my_drawing.ExportDXF(OutputFile)  # Exports the drawing to a DXF file
    my_drawing.Close(0)  # Closes the drawing
    print('Exported: ' + str(OutputFile))  # Notifies the user of the successful export
    print('Done')  # Indicates completion
    return

# Array to hold option settings for the utility dialog
Options = []
Options.append(['Select part', WindowsInputTypes.Face, None])
Options.append(['File', WindowsInputTypes.SaveFile, None, 'File', 'DXF|*.dxf', '.dxf'])
Options.append(['Label', WindowsInputTypes.Label , 'Export the drawing views of a part 1:1 in DXF. Nothing else fancy.'])

# Creates a utility dialog to interact with the user for exporting DXF files
Win.UtilityDialog('Export Part Views as DXF', 'Export', ExportFaceDXF, InputChanged, Options, 300)
