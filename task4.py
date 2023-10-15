class DefaultList(list):
    def __init__(self, default_value):
        self.default_value = default_value
        super().__init__()

    def __getitem__(self, index):
        try:
            return super().__getitem__(index)
        except IndexError:
            return self.default_value


# Пример 1
s1 = DefaultList(5)
s1.extend([4, 10])
indexes1 = [1, 124, 1882]
for i in indexes1:
    print(s1[i], end=" ")

print('\n')

# Пример 2
s2 = DefaultList(51)
s2.extend([1, 5, 7])
indexes2 = [0, 2, 1000, -1]
for i in indexes2:
    print(s2[i], end=" ")
