class Stack:
    def __init__(self):
        self.values = []
        self.sorted = []

    def push(self, item):
        # Add item to stack and sorted arrays
        self.values.append(item)
        self.sorted.append(item)
        # Sort reference array
        self.sorted = self.sort(self.sorted)

    def get(self):
        if(len(self.values)):
            return self.values[len(self.values) - 1]
        else:
            return None

    def remove(self):
        del self.values[len(self.values) - 1]

    def sort(self, toSort):

        # [2, 3, 4, 1]
        for i, e in reversed(list(enumerate(toSort))):
            print(i, e)
            if(toSort[i] <= toSort[i-1]):
                toSort[i],toSort[i-1]=toSort[i-1],toSort[i]

        return toSort

        return ""

    def max(self):
        return self.sorted[len(self.values) - 1]
        """ cursor = self.values[0]
        for i in self.values:
            if(i > cursor):
                cursor = i
        return cursor """

    def min(self):
        return self.sorted[0]
        """ cursor = self.values[0]
        for i in self.values:
            if(i < cursor):
                cursor = i
        return cursor """

    def __str__(self):
        print("===== VALUES =====")
        for idx, value in list(enumerate(self.values)):
            print(f"[{idx}] : {value}")
        print("===== SORTED =====")
        for idx, value in list(enumerate(self.sorted)):
            print(f"[{idx}] : {value}")
