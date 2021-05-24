# Find the minimum element in a sorted and rotated array
class minimum_element:
    def __init__(self):
        self.input_aaray()

    def input_aaray(self):
        input_length = int(input("Enter number of elements in array: "))
        input_list = []
        for i in range(input_length):
            input_list.append(int(input("Enter element into array: ")))
        print("Input array = ", input_list)
        print("Minimum element = ", min(input_list))


minimum_element()
