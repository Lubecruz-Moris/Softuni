from math import floor


class Integer:
    def __init__(self, value):
        self.value = value

    @classmethod
    def from_float(cls, float_value):
        try:
            if not isinstance(float_value, float):
                raise ValueError
            floor(float(float_value))
            return cls(int(float_value))
        except ValueError:
            return "value is not a float"

    @classmethod
    def from_roman(cls, value):
        rom_vals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        for i, c in enumerate(value):
            if (i + 1) == len(value) or rom_vals[c] >= rom_vals[value[i + 1]]:
                result += rom_vals[c]
            else:
                result -= rom_vals[c]
        return cls(int(result))

    @classmethod
    def from_string(cls, value):
        try:
            if not isinstance(value, str):
                raise ValueError
            return cls(int(value))
        except ValueError:
            return "wrong type"


first_num = Integer(10)
print(first_num.value)

second_num = Integer.from_roman("IV")
print(second_num.value)

print(Integer.from_float("2.6"))
print(Integer.from_string(2.6))
