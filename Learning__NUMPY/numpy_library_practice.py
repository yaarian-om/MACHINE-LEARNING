# -*- coding: utf-8 -*-
"""NumPy Library Practice

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1pZCiizCV_Vc1diSFw5o_kaw4qd2_v8cA

import numpy as np

Importing "numpy" Library
"""

# Import "numpy" Library
import numpy as np

"""Creating an 1D array by converting a list to an array"""

#  Creating an 1D array by converting a list to an array
a = [1,2,3,4,5]
generated_array = np.array(a)
generated_array

"""Converting a user inputed list into an array"""

generated_list = []
n = int(input("Enter the list size : "))
for i in range(n):
  val = int(input("Enter value : "))
  generated_list.append(val)

# generatd_list
generated_array = np.array(generated_list)
generated_array

"""Creating 2D array"""

# Creating 2D Array
generated_list = [[1,2,3],[4,5,6],[7,8,9]]
generated_array = np.array(generated_list)
generated_array

"""Matrix dimension & Shape"""

# Matrix dimension & Shape
print("Dimensions of array = ",generated_array.ndim)
print("Shape of array = ",generated_array.shape)

"""# numpy Functions
[1] .zeros(value)
"""

# numpy Functions
#  [1] .zeros(value)
#  ------------ for 1D Array ----------------
one_dimensional_array = np.zeros(5)
print("One Dimensional Array = ",one_dimensional_array)
#  ------------ for 2D Array ----------------
two_dimensional_array = np.zeros((2,3))
print("Two Dimensional Array = \n",two_dimensional_array)

"""[2] .ones(value)"""

#  [2] .ones(value)
one_dimensional_array = np.ones(5)
print("One Dimensional Array = ",one_dimensional_array)
#  ------------ for 2D Array ----------------
two_dimensional_array = np.ones((2,3))
print("Two Dimensional Array = \n",two_dimensional_array)

"""[3] .eye(value)"""

# .eye(value)
two_dimensional_square_array = np.eye(3)
#  ------------ for 2D Square Array ----------------
print("Two Dimensional Square Array = \n",two_dimensional_square_array)
#  ------------ for 2D non-square Array ----------------
two_dimensional_array = np.eye(2,3)
print("Two Dimensional Array = \n",two_dimensional_array)

"""[4] .diag([list])"""

# .diag([list])
two_dimensional_scaler_array = np.diag([1,2,3])
print("Two Dimensional Scaler Array = \n",two_dimensional_scaler_array)

"""[5] .randint(min,max,total_values)"""

# .randint(min,max,total_values)
random_number_array = np.random.randint(1,10,3)
print("Random Number Array = ",random_number_array)

"""[6] .rand(total_value)"""

# .rand(total_values)
random_number = np.random.rand(3)
print("Random Number Array = ",random_number)

"""[7] .randn(total_values)"""

# .randn(total_values)
random_number = np.random.randn(3)
print("Random Number Array = ",random_number)

"""#Slicing
new_array = old_array[start:end:increment]
"""

new_array = generated_array[2:4:2]
print("New Array = ",new_array)

"""# Reshaping of Array
[1] 1D to 2D
[2] 2D to 1D
"""

# Reshaping of Array
# 1D to 2D
generated_list = [1,2,3,4,5,6,7,8,9,10,11,12]
generated_array = np.array(generated_list)
# Now Reshaping
reshaped_array1 = generated_array.reshape(2,6)
print("RESHAPED ARRAY 1 = \n",reshaped_array1,"\nReshaped Array 1 shape = ",reshaped_array1.shape)
reshaped_array2 = generated_array.reshape(3,4)
print("RESHAPED ARRAY 2 = \n",reshaped_array2,"\nReshaped Array 2 shape = ",reshaped_array2.shape)
reshaped_array3 = generated_array.reshape(4,3)
print("RESHAPED ARRAY 3 = \n",reshaped_array3,"\nReshaped Array 3 shape = ",reshaped_array3.shape)
# 2D to 1D
new_one_dim_array = reshaped_array3.reshape(12)
print("NEW ONE DIMENSIONAL ARRAY = \n",new_one_dim_array,"\nNew One Dimensional Array shape = ",new_one_dim_array.shape)

"""# Seed Function
.random.seed(value)
"""

# Seed Function
# .random.seed(value)
np.random.seed(3)
new_array = np.random.randint(1,100,5)
print("New Array = ",new_array)

"""# User Defined 2D Array"""

# User Defined 2D Array
matrix = []
row = int(input("Enter the Number of Rows : "))
column = int(input("Enter the Number of Columns : "))

for i in range(row) :
  get_row = []
  for j in range(column) :
    get_row.append(int(input("Enter the value = "))) # Getting 1 Row values in 1 list
  matrix.append(get_row) # Putting 1 Row in that matrix list
# Now Convert the List into Matrix or 2D array
matrix = np.array(matrix)
# print("\n\n The Matrix is = \n",matrix)

# For printing the matrix
for i in range(row):
    for j in range(column):
        print(matrix[i][j], end = " ")
    print()

"""# 2D Array Slicing"""

# 2D Array Slicing
np.random.seed(111)
a = np.random.randint(1,500,30).reshape(6,5)
print("Full Array = \n",a)
#  Now take a portion of the array
b = a[2:5,2:5]
print("New Sliced Array = \n",b)

"""# View VS Copy"""

# View VS Copy
# view
a = np.array([10,20,30,40,50,60,70,80])
slicing = a[3:6]
slicing[:] = 0 # This will update the a[3:6] positions also with the value 0
print("Mother Array = ",a)
# Copy
slicing2 = a[0:3].copy()
slicing2[:] = 0 # This will update the a[3:6] positions also with the value 0
print("Slicing 2 Array = ",slicing2)

"""# Conditional Selection"""

# Conditional Selection
print(a[(a>0) & (a<60)])

"""# Various array function in mathematics
One Dimensional </br>
Two Dimensional
"""

# Various array function in mathematics
# One Dimensional
new_array1 = a*2
print("New Array1 = ",new_array1)
new_array2 = a+2
print("New Array2 = ",new_array2)
new_array3 = a**3
print("New Array3 = ",new_array3)
new_array4 = new_array2 + new_array3
print("New Array4 = ",new_array4)
# Two Dimensional
new_array5 = new_array2.reshape(2,4)
print("New Array5 = \n",new_array5)
new_array6 = new_array5 + 2
print("New Array6 = \n",new_array6)
# It's Just Like normal multiplication not matrix multiplication
new_array7 = new_array5 * 2
print("New Array7 = \n",new_array7)
# For Matrix multiplication, we use .dot() for scaler multiply
mult_mat = np.random.randint(1,9,8).reshape(4,2)
new_array8 = new_array5.dot(mult_mat)
print("New Array8 = \n",new_array8)

"""# Stacks in numpy
Horizontal Stack <br/>
Vertical Stack
"""

# Stacks in numpy
# Horizontal Stack
# Vertical Stack
arr1 = np.random.randint(1,9,5)
arr2 = np.random.randint(1,9,5)
mat1 = np.random.randint(1,21,9).reshape(3,3)
mat2 = np.random.randint(1,21,9).reshape(3,3)
print(np.hstack((arr1,arr2)))
print(np.vstack((arr1,arr2)))
print(np.hstack((mat1,mat2)))
print(np.vstack((mat1,mat2)))