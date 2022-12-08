import os


def rectangle(length, width):
    def area():
        rect_area = length * width
        return f"Rectangle area: {rect_area}"

    def perimeter():
        rect_perim = 2*(length + width)
        return f"Rectangle perimeter: {rect_perim}"

    if not isinstance(length, int) or not isinstance(width, int):
        return "Enter valid values!"

    return f"{area()}{os.linesep}{perimeter()}"



print(rectangle(2, 10))

print(rectangle('2', 10))