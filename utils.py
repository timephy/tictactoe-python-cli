# Manages coordinates input, return (x, y)
def input_coords(prompt):
    while True:
        try:
            # split string input at ","
            input_value = input(prompt).split(",")
            # parses the input values as integer
            coords = (int(input_value[1]) - 1, int(input_value[0]) - 1)
            # asserts that input values are between 1 and 3
            if coords[0] not in range(0, 3) or coords[1] not in range(0, 3):
                raise Exception
            # if input values are valid, return them
            return coords
        except Exception:
            # ignore error and try again
            print("Input was invalid!")


def new_field():
    return [[None, None, None],
            [None, None, None],
            [None, None, None]]
