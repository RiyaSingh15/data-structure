# Search an element in a sorted and rotated array

class rotated_array_search:
    def __init__(self):
        self.array_input()

    def array_input(self):
        input_length = int(input("Enter number of elements in array: "))
        input_list = []
        for i in range(input_length):
            input_list.append(
                int(input("Enter element into array (enter sorted elements only): ")))
        sorted_list = sorted(input_list)
        if(sorted_list != input_list):
            print("Array is unsorted")
            return self.array_input()
        print("Input array = ", input_list)
        rotation_factor = int(
            input("Enter the number to rotate the elements by: "))
        self.rotation(input_list, rotation_factor, input_length)

    def rotation(self, ar, d, n):
        input_list = []
        input_list = ar
        for i in range(d):
            input_list.append(input_list.pop(0))
        print("Rotated array = ", input_list)
        self.array_search(input_list, int(
            input("Enter element to find location (the location will be 0 based): ")))

    def array_search(self, array, element):
        if(element in array):
            print("Position of ", element, " in ",
                  array, " is ", array.index(element))
        else:
            print(element, " does not exist in ", array)


rotated_array_search()
