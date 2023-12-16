# packages to get data from user
from Helpers.DataRetrievers.UploadImage import GetImage
from Helpers.DataRetrievers.GridRowColsCount import GetRowColsCount
from Helpers.DataRetrievers.FileDownloader import DownloadOrViewFile

# packages that perform high level operations
from Helpers.MatrixCreator import ProcessImageToMatrix
from Helpers.CodeColors import GetCodedDictMatrix
from Helpers.TempFileManager import CreateTempFile
import Helpers.GeneralMethods as Methods
import sys
import time

def main():
    # rows, cols = 1, 1
    img = GetImage()
    rows, cols = GetRowColsCount()
    unique_colors, matrix = ProcessImageToMatrix(img, rows, cols)
    # Color dictionary
    # unique_colors = {
    #     "#FF0000": "Red",
    #     "#00FF00": "Green",
    #     "#0000FF": "Blue",
    #     "#FFFF00": "Yellow",
    #     "#FF00FF": "Magenta",
    #     "#00FFFF": "Cyan"
    # }

    # # Example 4x4 matrix using hex codes from the dictionary
    # matrix = [
    #     ["#FF0000", "#00FF00", "#0000FF", "#FFFF00"],
    #     ["#00FFFF", "#00FFFF", "#FF00FF", "#0000FF"],
    #     ["#00FFFF", "#FF00FF", "#00FF00", "#FFFF00"],
    #     ["#FFFF00", "#00FFFF", "#00FFFF", "#00FFFF"]
    # ]
    # create the colour codes to display on pattern
    coded_colors, matrix = GetCodedDictMatrix(unique_colors, matrix)
    print()
    print("rows: ", rows, "\ncolumns: ", cols)
    print()
    Methods.print_coded_table(coded_colors, unique_colors)
    print("\n\n\n\n*************** Right handed RS ***************")
    print("\n\n-----------------------------------------------")
    print("Tapestry Bottom right to Top left - Right to Left")
    Methods.tapestry_bottom_right_to_top_left_rtl(matrix)
    print("---------------------------------------------------")

    print("\n\n-----------------------------------------------")
    print("Tapestry Top right to Bottom left - Right to Left")
    Methods.tapestry_top_right_to_bottom_left_rtl(matrix)
    print("---------------------------------------------------")

    print("\n\n\n\n*************** Left handed RS ***************")
    print("\n\n-----------------------------------------------")
    print("Tapestry Bottom left to Top right - Left to Right")
    Methods.tapestry_bottom_left_to_top_right_ltr(matrix)
    print("---------------------------------------------------")

    print("\n\n-----------------------------------------------")
    print("Tapestry Top left to Bottom right - Left to Right")
    Methods.tapestry_top_left_to_bottom_right_ltr(matrix)
    print("---------------------------------------------------")
    print()
    for row in matrix:
        print(row)
    print()


if __name__ == "__main__":
    try:
        stdout = sys.stdout
        file = CreateTempFile()
        with open(file, "w") as f:
            sys.stdout = f
            main()
        DownloadOrViewFile(file)
        sys.stdout = stdout
    except Exception as e:
        print("Error:", e)