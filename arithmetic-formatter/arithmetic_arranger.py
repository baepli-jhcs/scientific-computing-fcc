import re


def arithmetic_arranger(problems, show=False):
    if len(problems) > 5:
        return "Error: Too many problems."
    top_row = []
    mid_row = []
    line_row = []
    bottom_row = []
    for problem in problems:
        top = ""
        mid = ""
        row = ""
        bottom = ""
        result = 0
        elements = problem.split()
        if len(elements) != 3:
            return "Error: Operator must be '+' or '-'."
        if re.search("[a-z]+", elements[0]) or re.search("[a-z]+", elements[2]):
            return "Error: Numbers must only contain digits."
        if len(elements[0]) > 4 or len(elements[2]) > 4:
            return "Error: Numbers cannot be more than four digits."
        if elements[1] == "+":
            result = int(elements[0]) + int(elements[2])
        elif (elements[1]) == "-":
            result = int(elements[0]) - int(elements[2])
        else:
            return "Error: Operator must be '+' or '-'."
        length = max(len(elements[0]), len(elements[2])) + 2
        for item in range(0, length):
            row += "-"
        top = format(str(elements[0]), " >" + str(length))
        mid += elements[1]
        mid = mid.ljust(length - len(elements[2]), " ")
        mid += elements[2]
        bottom = format(str(result), " >" + str(length))
        top_row.append(top)
        mid_row.append(mid)
        line_row.append(row)
        bottom_row.append(bottom)
    return_string = (
        fill_row(top_row) + "\n" + fill_row(mid_row) + "\n" + fill_row(line_row)
    )
    if show:
        return_string += "\n" + fill_row(bottom_row)
    return return_string


def fill_row(arr):
    new_str = ""
    for row in arr:
        new_str += row + "    "
    new_str = new_str[:-4]
    return new_str