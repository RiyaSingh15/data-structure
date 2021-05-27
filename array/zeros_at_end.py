# Move all zeroes to end of array

class zeroes_at_end:
    def __init__(self):
        self.array_input()

    def array_input(self):
        length = int(input("Enter number of elements in the array: "))
        input_array = []
        for i in range(length):
            input_array.append(int(input("Enter element into array: ")))

        print("Input array= ", input_array)
        print("Output array= ", self.zero_reposition(input_array))

    def zero_reposition(self, array):
        numberOfZeros = array.count(0)
        output_array = []
        for x in array:
            if x != 0:
                output_array.append(x)
        for x in range(numberOfZeros):
            output_array.append(0)

        return output_array


zeroes_at_end()
