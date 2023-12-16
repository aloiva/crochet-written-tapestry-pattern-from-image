from PIL import Image
from collections import Counter
from Helpers.GeneralMethods import RGBToHex, GetHexColorName

class ColorMatrixAnalyzer:
    unique_colors = {}
    dominant_color_matrix = []
    rows = 1
    cols = 1
    img = None

    def __init__(self, rows=1, cols=1):
        self.rows = rows
        self.cols = cols

    def set_image(cls, image):
        cls.img = image

    def set_rows_cols(cls, rows, cols):
        cls.rows = rows
        cls.cols = cols

    def get_dominant_color(cls, image):
        pixels = list(image.getdata())
        color_count = Counter(pixels)
        most_common_color = color_count.most_common(1)[0][0]
        hex_color = RGBToHex(most_common_color)
        
        if hex_color not in cls.unique_colors:
            cls.unique_colors[hex_color] = GetHexColorName(hex_color)
            
        return hex_color

    def Analyse(cls):
        img = cls.img
        img = img.convert("RGB")
        
        width, height = img.size
        block_width = width // cls.cols
        block_height = height // cls.rows
        
        cls.dominant_color_matrix = []

        for i in range(cls.rows):
            row_colors = []
            for j in range(cls.cols):
                left = j * block_width
                upper = i * block_height
                right = left + block_width
                lower = upper + block_height
                
                block = img.crop((left, upper, right, lower))
                dominant_color = cls.get_dominant_color(block)
                row_colors.append(dominant_color)
            
            cls.dominant_color_matrix.append(row_colors)

    def GetUniqueColors(cls):
        return cls.unique_colors

    def ProcessImageToMatrix(cls):
        return cls.dominant_color_matrix

def ProcessImageToMatrix(img, rows = 1, cols = 1):
    analyzer = ColorMatrixAnalyzer()
    analyzer.set_rows_cols(rows, cols)
    analyzer.set_image(img)
    analyzer.Analyse()

    unique_colors = analyzer.GetUniqueColors()
    dominant_color_matrix = analyzer.ProcessImageToMatrix()

    return unique_colors, dominant_color_matrix

if __name__ == '__main__':
    # Example usage
    image_path = "test4.jpg"
    image = Image.open(image_path)

    unique_colors, dominant_color_matrix = ProcessImageToMatrix(image)

    for row in dominant_color_matrix:
        print(row)

    print("Unique Colors:", unique_colors)
