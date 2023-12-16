import requests 
import numpy as np

def RGBToHex(rgb_tuple):
    return "#{:02x}{:02x}{:02x}".format(rgb_tuple[0], rgb_tuple[1], rgb_tuple[2])

def GetHexColorName(hex_color):
    api_url = f"https://api.color.pizza/v1/?values={hex_color[1:]}"
    # return 'Black Grey'
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        # print(data)
        color_name = data.get("paletteTitle", "Unknown")
        return color_name
    else:
        return "Error fetching color name"
    # print(api_url)

def create_coded_dictionary(input_dict):
    coded_dict = {}
    used_codes = {}

    for key, value in input_dict.items():
        code = value[0]
        for i in range(1, len(value)):
            if code in used_codes and value != used_codes[code]:
                code += value[i]
            else:
                break
        used_codes[code] = value
        coded_dict[key] = code

    return coded_dict

def print_coded_table(coded_colours, unique_colours):
    print("REFERENCE")
    print("----------------------------------------")
    print("Hexcode     Colour name         Notation")
    print("----------------------------------------")

    for color in coded_colours:
        print("{:<12} {:<20} {:<10}".format(color, unique_colours[color], coded_colours[color]))

def crate_coded_matrix(matrix, coded_colours):
    if matrix != None:
        m, n = np.array(matrix).shape
        for i in range(m):
            for j in range(n):
                matrix[i][j] = coded_colours[matrix[i][j]]
    return matrix

def WritePatternForList(lst):
    result = []
    count = 1
    
    for i in range(1, len(lst)):
        if lst[i] == lst[i - 1]:
            count += 1
        else:
            result.append(f"{count}{lst[i - 1]}")
            count = 1
    
    result.append(f"{count}{lst[-1]}")
    print(", ".join(result))

def tapestry_bottom_right_to_top_left_rtl(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    for r in range(rows - 1, -1, -1):
        row_list = []
        print(f"row {r + 1}:", end=" ")
        if r % 2 == 0:
            for c in range(cols):
                row_list.append(matrix[r][c])
        else:
            for c in range(cols - 1, -1, -1):
                row_list.append(matrix[r][c])
        WritePatternForList(row_list)

def tapestry_top_right_to_bottom_left_rtl(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    for r in range(rows):
        row_list = []
        print(f"row {r + 1}:", end=" ")
        if r % 2 == 0:
            for c in range(cols - 1, -1, -1):
                row_list.append(matrix[r][c])
        else:
            for c in range(cols):
                row_list.append(matrix[r][c])
        WritePatternForList(row_list)

def tapestry_bottom_left_to_top_right_ltr(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    for r in range(rows - 1, -1, -1):
        row_list = []
        print(f"row {r + 1}:", end=" ")
        if r % 2 == 0:
            for c in range(cols - 1, -1, -1):
                row_list.append(matrix[r][c])
        else:
            for c in range(cols):
                row_list.append(matrix[r][c])
        WritePatternForList(row_list)

def tapestry_top_left_to_bottom_right_ltr(matrix):
    if matrix == None:
        return
    rows = len(matrix)
    cols = len(matrix[0])

    for r in range(rows):
        row_list = []
        print(f"row {r + 1}:", end=" ")
        if r % 2 == 0:
            for c in range(cols):
                row_list.append(matrix[r][c])
        else:
            for c in range(cols - 1, -1, -1):
                row_list.append(matrix[r][c])
        WritePatternForList(row_list)