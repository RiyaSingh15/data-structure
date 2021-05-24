# Rearrange an array such that arr[i] = i

class rearrange_aaray:
    def __init__(self):
        self.array_input()

    def array_input(self):
        input_length = int(input("Enter number of elements in array: "))
        input_list = []
        for i in range(input_length):
            input_list.append(int(input("Enter element into array: ")))
        print("Input array = ", input_list)
        print("Rearranged array = ", self.array_rearrangement(input_list))

    def array_rearrangement(self, array):
        output_array = []
        for i in range(0, len(array)):
            if i in array:
                output_array.append(i)
            else:
                output_array.append(-1)

        return output_array


rearrange_aaray()
