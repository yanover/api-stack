class Pile:
    def __init__(self):
        self.values = []

    def push(self, item):
        self.values.append(item)

    def get(self):
        return self.values[len(self.values) - 1]

    def __str__(self):
        print(self.values)
        
