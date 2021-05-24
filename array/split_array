# Split the array and add the first part to the end

class split_array:
    def __init__(self):
        self.input_array()

    def input_array(self):
        input_length = int(input("Enter number of elements in array: "))
        input_list = []
        for i in range(input_length):
            input_list.append(int(input("Enter element into array: ")))
        print("Input array = ", input_list)

        split_index = int(
            input("Enter split index: "))

        first_part = input_list[0:split_index]
        second_part = input_list[split_index: len(input_list)]
        resultant_list = second_part + first_part
        print("Array after splitting at index ",
              split_index, " = ", resultant_list)


split_array()
