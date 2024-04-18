using System;
using System.Runtime.InteropServices;
using AlibreX;
namespace ExportPartViewsAsDXF
{
    public class Program
    {
        public static IADSession Session;
        public static IADPartSession objADPartSession;
        public static IAutomationHook Hook;
        public static IADRoot Root;
        public static void Main()
        {
            Hook = (IAutomationHook)Marshal.GetActiveObject("AlibreX.AutomationHook");
		    Root = (IADRoot)Hook.Root;
		    Session = Root.Sessions.Item(0);
            var InputFace = "";
            var outputFile = "";
            Console.WriteLine("Please Wait!");
            var topSession = Root.TopmostSession;
            var partPath = InputFace.GetPart().FileName;
            var myDrawing = Root.CreateEmptyDrawing("Hello World");
            var pointOrigin = myDrawing.GeometryFactory.Create2DPoint(0.0, 0.0);
            var testSheet = myDrawing.Sheets.ActiveSheet;
            testSheet.ModifySheetBlank("Working Please Wait", 1.0, 1.0, ADUnits.AD_CENTIMETERS, 1.0, 1.0);
            testSheet.CreateStandardViews(partPath, ADDrawingViewType.AD_STANDARD, ADDetailingOption.AD_TANGENT_EDGES, 1.0, 1.0, ADViewOrientation.AD_FRONT | ADViewOrientation.AD_BACK | ADViewOrientation.AD_LEFT | ADViewOrientation.AD_RIGHT | ADViewOrientation.AD_TOP | ADViewOrientation.AD_BOTTOM | ADViewOrientation.AD_TOP_LEFT | ADViewOrientation.AD_TOP_RIGHT | ADViewOrientation.AD_BOTTOM_LEFT | ADViewOrientation.AD_BOTTOM_RIGHT, pointOrigin);
            myDrawing.ExportDXF(outputFile);
            myDrawing.Close();
            Console.WriteLine($"Exported: {outputFile}");
            Console.WriteLine("Done");
        }
    }
}
