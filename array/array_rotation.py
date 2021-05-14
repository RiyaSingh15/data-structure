# Write a function rotate(ar[], d, n) that rotates arr[] of size n by d elements. 

class array_rotation:
    def __init__(self):
        self.array_input()

    def array_input(self):
       input_length = int(input("Enter number of elements in array: "))
       input_list = []
       for i in range(input_length):
           input_list.append(int(input("Enter element into array: ")))
       print("Input array = ", input_list)
       rotation_factor = int(input( "Enter the number to rotate the elements by: "))
       self.rotation(input_list, rotation_factor, input_length)

    def rotation(self, ar, d, n):
        input_list = []
        input_list = ar
        for i in range(d):
            input_list.append(input_list.pop(0))
        print("Rotated array = ", input_list)        
        
array_rotation()