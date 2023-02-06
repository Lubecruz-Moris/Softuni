class reverse_iter:
    def __init__(self, nums):
        self.nums = nums
        self.idx = len(self.nums) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.idx > -1:
            value = self.nums[self.idx]
            self.idx -= 1
            return value
        raise StopIteration


reversed_list = reverse_iter([1, 2, 3, 4])

for item in reversed_list:
    print(item)
