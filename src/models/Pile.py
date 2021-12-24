class Pile:
    def __init__(self):
        self.values = []

    def push(self, item):
        self.values.append(item)
        return self.get()

    def get(self):
        return self.values[len(self.values) - 1]

    def remove(self):
        del self.values[len(self.values) - 1]

    def max(self):
        cursor = self.values[0]
        for i in self.values:
            if(i > cursor):
                cursor = i
        return cursor

    def min(self):
        cursor = self.values[0]
        for i in self.values:
            if(i < cursor):
                cursor = i
        return cursor

    def __str__(self):
        return self.values