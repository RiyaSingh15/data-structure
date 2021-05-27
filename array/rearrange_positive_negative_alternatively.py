# Rearrange array in alternating positive & negative items

class rearrange_positive_negative_alternatively:
    def __init__(self):
        self.array_input()

    def array_input(self):
        length = int(input("Enter number of elements in the array: "))
        input_array = []
        for i in range(length):
            input_array.append(int(input("Enter element into array: ")))

        print("Input array= ", input_array)
        print("Output array= ", self.array_reposition(input_array))

    def array_reposition(self, array):
        sorted_array = sorted(array)
        output_array = []
        if(len(sorted_array) % 2 != 0):
            first_half = sorted_array[0: int(len(sorted_array)/2)+1]
            second_half = sorted_array[int(
                len(sorted_array)/2)+1: len(sorted_array)]
            for i in range(int(len(sorted_array)/2)):
                output_array.append(first_half[i])
                output_array.append(second_half[i])
            output_array.append(first_half[len(first_half)-1])
        else:
            first_half = sorted_array[0: int(len(sorted_array)/2)]
            second_half = sorted_array[int(
                len(sorted_array)/2): len(sorted_array)]
            for i in range(int(len(sorted_array)/2)):
                output_array.append(first_half[i])
                output_array.append(second_half[i])

        return output_array


rearrange_positive_negative_alternatively()
