from Helpers.GeneralMethods import create_coded_dictionary, crate_coded_matrix
from Helpers.DataRetrievers.ColorNames import GetNewColorData

def GetCodedDictMatrix(color_data, matrix=None):
    color_data = GetNewColorData(color_data)

    coded_colors = create_coded_dictionary(color_data)
    coded_matrix = crate_coded_matrix(matrix, coded_colors)
    return coded_colors, coded_matrix

if __name__ == "__main__":
    color_data = {
        "#FF0000": "red",
        "#00FF00": "green",
        "#0000FF": "blue",
        "#FFFF00": "yellow",
        "#FF00FF": "magenta",
        "#00FFFF": "cyan",
        "#800080": "purple",
        "#FFA500": "orange",
        "#808080": "gray",
        "#800000": "maroon"
    }
    coded, _ = GetCodedDictMatrix(color_data)
    print(coded)
