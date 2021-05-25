# Rearrange array such that arr[i] >= arr[j] if i is even and arr[i]<=arr[j] if i is odd and j < i

class array_element_reposition:
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
            reversed_list = []
            for i in range(len(first_half)-1, -1, -1):
                reversed_list.append(first_half[i])
            for i in range(int(len(sorted_array)/2)):
                output_array.append(reversed_list[i])
                output_array.append(second_half[i])
            output_array.append(reversed_list[len(reversed_list)-1])
        else:
            first_half = sorted_array[0: int(len(sorted_array)/2)]
            second_half = sorted_array[int(
                len(sorted_array)/2): len(sorted_array)]
            reversed_list = []
            for i in range(len(first_half)-1, -1, -1):
                reversed_list.append(first_half[i])
            for i in range(int(len(sorted_array)/2)):
                output_array.append(reversed_list[i])
                output_array.append(second_half[i])

        return output_array


array_element_reposition()
