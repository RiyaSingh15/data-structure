# Given an array (or string), the task is to reverse the array/string.

class array_reverse:
    def __init__(self):
        self.input_array()

    def input_array(self):
        input_list = []
        while True:
            input_variable = input(
                "Enter element into array (enter } to stop): ")
            if (input_variable == '}'):
                break
            input_list.append(input_variable)

        print("Input array = ", input_list)
        reversed_list = []
        for i in range(len(input_list)-1, -1, -1):
            reversed_list.append(input_list[i])
        print("Reversed array = ", reversed_list)


array_reverse()
