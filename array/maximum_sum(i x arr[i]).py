# Find maximum value of Sum( i*arr[i]) with only rotations on given array allowed

class sum_maximum:
    def __init__(self):
        self.array_input()

    def array_input(self):
        length = int(input("Enter the number of elements: "))
        input_array = []
        for i in range(0, length):
            input_array.append(int(input("Enter element into array: ")))
        print("Input array: ", input_array)
        self.maximum_sum(input_array)

    def maximum_sum(self, array):
        sum_array = []
        for i in range(0, len(array)):
            total = 0
            for j in range(0, len(array)):
                total = total + j * array[j]
            sum_array.append(total)
            array.insert(0, array.pop(len(array)-1))
        print("Maximum sum we can get = ", max(sum_array))


sum_maximum()
