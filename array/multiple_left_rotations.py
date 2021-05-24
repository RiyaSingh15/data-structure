# Quickly find multiple left rotations of an array

class multiple_left_rotations:
    def __init__(self):
        self.input_aaray()

    def input_aaray(self):
        input_length = int(input("Enter number of elements in array: "))
        input_list = []
        for i in range(input_length):
            input_list.append(int(input("Enter element into array: ")))
        print("Input array = ", input_list)
        rotation_number = int(input("Enter number of rotations: "))
        rotation_list = []
        for i in range(0, rotation_number):
            rotation_list.append(int(input("Enter the rotation factor: ")))

        input_array = input_list
        rotation_list = sorted(rotation_list)
        for i in range(0, rotation_number):
            if i == 0:
                for j in range(0, rotation_list[i]):
                    input_array.append(input_array.pop(0))
            else:
                for j in range(rotation_list[i-1], rotation_list[i]):
                    input_array.append(input_array.pop(0))
            print("Array rotated ", rotation_list[i], " times = ", input_array)


multiple_left_rotations()
