# Given an array, cyclically rotate the array clockwise by one.

class array_clockwise_rotation:
    def __init__(self):
        self.array_input()

    def array_input(self):
        array_length = int(input("Enter the number of elements in array: "))
        input_array = []
        for i in range(array_length):
            input_array.append(int(input("Enter the element into array: ")))
        print("Input array ", input_array)
        self.array_rotation(input_array, array_length)

    def array_rotation(self, array, length):
        array.insert(0, array.pop(length-1))
        print("Array after cyclically rotate the array clockwise by one ", array)


array_clockwise_rotation()
