# Task 1: Legacy Code in Python

def compute_stats(file):
    total = 0
    summation = 0
    average = 0
    minimum = 0
    maximum = 0

    try:
        with open(file, "r") as f:
            line = f.readline()
            first_line = int(line.strip())
            minimum = first_line
            maximum = first_line

            while line:
                num = int(line.strip())
                total += 1
                summation += num

                if minimum > num:
                    minimum = num
                if maximum < num:
                    maximum = num

                line = f.readline()

        print("total =", total)
        print("summation =", summation)
        print("average =", round(summation / total))
        print("Minimum =", minimum)
        print("Maximum =", maximum)

    except:
        print("Error reading file")


compute_stats("random_nums.txt")


# Task 2: Refactored Code in Python

class ComputeStatistics:

    def __init__(self, file):
        self.file = file

    def readInt(self):
        data = []
        try:
            with open(self.file, "r") as f:
                for line in f:
                    num = int(line.strip())
                    data.append(num)
        except:
            print("Error reading file")
        return data

    def count(self):
        data = self.readInt()
        return len(data)

    def summation(self):
        data = self.readInt()
        total = 0
        for x in data:
            total += x
        return total

    def average(self):
        total = self.summation()
        count = self.count()
        return total / count

    def minimum(self):
        data = self.readInt()
        return min(data)

    def maximum(self):
        data = self.readInt()
        return max(data)


file = "random_nums.txt"
cs = ComputeStatistics(file)

print("The values are:", cs.readInt())
print("Total values in file are:", cs.count())
print("Summation of data is:", cs.summation())
print("Average of data is:", cs.average())
print("Minimum value from data is:", cs.minimum())
print("Maximum value from data is:", cs.maximum())