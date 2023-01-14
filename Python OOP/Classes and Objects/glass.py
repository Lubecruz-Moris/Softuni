class Glass:
    capacity = 250

    def __init__(self):
        self.initial_content = 0
        self.content = self.initial_content

    def fill(self, ml):
        space_left = self.get_space_left()
        if space_left < ml:
            return f"Cannot add {ml} ml"
        self.content += ml
        return f"Glass filled with {ml} ml"

    def empty(self):
        self.content = self.initial_content
        return "Glass is now empty"

    def info(self):
        return f"{self.get_space_left()} ml left"

    def get_space_left(self):
        return self.capacity - self.content


glass = Glass()
print(glass.fill(100))
print(glass.fill(200))
print(glass.empty())
print(glass.fill(200))
print(glass.info())
