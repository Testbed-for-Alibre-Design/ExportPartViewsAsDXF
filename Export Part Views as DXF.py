https://www.alibre.com/forum/index.php?threads/script-release-export-part-views-as-dxf.24804/
from __future__ import division # This fixes division with integers. For example the 1 / 2 = 0.5 instead of 0
import os # for working with file paths
import clr
import _winreg

def getalibrepath():
    try:
        keystring = r'SOFTWARE\Alibre, Inc.\Alibre Design' + '\\' + str(Global.Root.Version).split(' ')[1].replace(',', '.')
        hKey = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE, keystring)
        result = _winreg.QueryValueEx(hKey, 'HomeDirectory')
        return result[0]
    except Exception, e:
        try:
            hKey = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE, 'Software\\Alibre, Inc.\\Alibre Design')
            result = _winreg.QueryValueEx(hKey, 'HomeDirectory')
            return result[0]
        except Exception, e:
            print('\n')
            print('Could not get Alibre Path.')
            return ''
import clr
clr.AddReferenceToFileAndPath(os.path.join(getalibrepath(),r'Program\AlibreX.dll'))
from AlibreX import ADUnits, ADDrawingViewType, ADDetailingOption, ADViewOrientation, IAD2DPoint, IADTransformation


Win = Windows()

def InputChanged(Index, Value):
    return

def ExportFaceDXF(Values):
    if Values[0] == None or Values[0] == '':
        print('No Face Selected.')
        return
    InputFace = Values[0]
    if Values[1] == None or Values[1] == '':
        print('No Export File set.')
        return
    OutputFile = Values[1]
    if not os.path.splitext(OutputFile)[1]:
        print('Extension not set for DXF Output File.\nAdding .dxf extension.')
        OutputFile = str(OutputFile) + '.dxf'
    if not os.path.splitext(OutputFile)[1] == '.dxf':
        print('Wrong extension for DXF File.')
        return
    print('Please Wait!')
    Root = Global.Root
    top_sess = Root.TopmostSession
    part_path = InputFace.GetPart().FileName
    my_drawing = Root.CreateEmptyDrawing('Hello World')
    point_orgin = my_drawing.GeometryFactory.Create2DPoint(0.0,0.0)
    test_sheet = my_drawing.Sheets.ActiveSheet
    test_sheet.ModifySheetBlank('Working Please Wait', 1.0, 1.0, ADUnits.AD_CENTIMETERS, 1.0, 1.0)
    test_sheet.CreateStandardViews(str(part_path), ADDrawingViewType.AD_STANDARD, ADDetailingOption.AD_TANGENT_EDGES, 1.0, 1.0, ADViewOrientation.AD_FRONT | ADViewOrientation.AD_BACK | ADViewOrientation.AD_LEFT | ADViewOrientation.AD_RIGHT | ADViewOrientation.AD_TOP | ADViewOrientation.AD_BOTTOM | ADViewOrientation.AD_TOP_LEFT | ADViewOrientation.AD_TOP_RIGHT | ADViewOrientation.AD_BOTTOM_LEFT | ADViewOrientation.AD_BOTTOM_RIGHT , point_orgin)
    my_drawing.ExportDXF(OutputFile)
    my_drawing.Close(0)
    print('Exported: ' + str(OutputFile))
    print('Done')
    return

Options = []
Options.append(['Select part', WindowsInputTypes.Face, None])
Options.append(['File', WindowsInputTypes.SaveFile, None, 'File', 'DXF|*.dxf', '.dxf'])
Options.append(['Label', WindowsInputTypes.Label , 'Export the drawing views of a part 1:1 in DXF. Nothing else fancy.'])

Win.UtilityDialog('Export Part Views as DXF', 'Export', ExportFaceDXF, InputChanged, Options, 300)
