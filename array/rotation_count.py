# Find the Rotation Count in Rotated Sorted array

class rotation_count:
    def __init__(self):
        self.input_aaray()

    def input_aaray(self):
        input_length = int(input("Enter number of elements in array: "))
        input_list = []
        for i in range(input_length):
            input_list.append(int(input("Enter element into array: ")))
        print("Input array = ", input_list)
        self.number_of_rotations(input_list)

    def number_of_rotations(self, array):
        print("Rotation count = ", array.index(min(array)))


rotation_count()
