# Given a sorted and rotated array, find if there is a pair with a given sum

class pair_with_given_sum:
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
        self.rotation(input_list, int(
            input("Enter the number to rotate the elements by: ")))

    def rotation(self, ar, d):
        input_list = []
        input_list = ar
        for i in range(d):
            input_list.append(input_list.pop(0))
        print("Rotated array = ", input_list)
        self.array_search_sum(input_list, int(
            input("Enter element to find sum pair: ")))

    def array_search_sum(self, array, sum):
        for i in range(0, len(array)-1):
            for j in range(i, len(array)-1):
                if(array[i]+array[j] == sum):
                    print("{", array[i], " + ", array[j], "} = ", sum)
                    break
        else:
            print("There is no pair in array with sum = ", sum)


pair_with_given_sum()
