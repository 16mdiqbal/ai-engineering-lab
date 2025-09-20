import numpy as np

def create_matrix():
    #return np.random.randint(0, 51, size=(5, 50))
    rng =  np.random.default_rng()
    return rng.integers(low=0, high=51, size=(5, 50))

def statistical_analysis(matrix):
    
    #Calculate the average execution time per cycle. 
    average_per_cycle = np.mean(matrix, axis=1)
    print("Average execution time per cycle : ", average_per_cycle)

    # Identify the test case with the maximum execution time in the entire dataset.
    max_of_all_cycle = np.max(matrix, axis=1)
    max_numer = np.max(max_of_all_cycle)
    print("Maximum execution time of all the cycle : ", max_numer)

    # other way of doing it
    max_n_wo_axis = np.max(matrix)
    print("Maximum execution time of all the cycle : ", max_n_wo_axis)

    #Find the standard deviation of execution times for each cycle to measure consistency.
    std_deviation_all_cycle = np.std(matrix, axis=1)
    print("Standard deviation of execution times for each cycle : ", std_deviation_all_cycle)

def slicing_operations(matrix):
    
    #Extract the first 10 test execution times from Cycle 1.
    print("Extract the first 10 test execution times from Cycle 1 : ", matrix[0, 0:10])

    #Extract the last 5 test execution times from Cycle 5.
    print(matrix[4:, -5:])

    #Extract the last 5 test execution times from each cycle.
    print(matrix[0:, -5:])

    #Extract every alternate test from Cycle 3.
    print(matrix[2:3, 0::2])

    #or
    print(matrix[2, 0::2])

def arithmetic_operation(matrix):

    #Perform element-wise addition and subtraction between Cycle 1 and Cycle 2.
    #Addition
    matrix_0 = matrix[0, :] - matrix[1, :]
    print("Perform element-wise addition between Cycle 1 and Cycle 2:  ", matrix_0)
    
    matrix_1 = matrix[0, :] + matrix[1, :]
    print("Perform element-wise addition between Cycle 1 and Cycle 2: ", matrix_1)

    #OR
    matrix_sum = matrix[0] + matrix[1]
    print("Perform element-wise addition between Cycle 1 and Cycle 2 : ", matrix_sum)
    
    #Perform element-wise multiplication and division between Cycle 4 and Cycle 5.

    #Multiplication
    matrix_mul = matrix[3, :] * matrix[4, :]
    print("Perform element-wise multiplication between Cycle 4 and Cycle 5 : ", matrix_mul)

    #Division
    matrix_div = matrix[3, :] / matrix[4, :]
    print("Perform element-wise division between Cycle 4 and Cycle 5 : ", matrix_div)

def power_functions(matrix):

    #Square and cube all execution times.
    #square
    square_all_matrix = np.square(matrix)
    print("Square all execution times : ", square_all_matrix)

    pow_2 = np.power(matrix, 2)
    print("Square all execution times : ", pow_2)

    #cube
    cube_all_matrix = np.power(matrix, 3)
    print("Cube all execution times : ", cube_all_matrix)

    #Apply a square root transformation on the dataset
    square_rootall_all_matrix = np.sqrt(matrix)
    print("Apply a square root transformation on the dataset : ", square_rootall_all_matrix)

    #Apply logarithmic transformation (np.log(array+1)) to normalize skewed data.
    normalize_skewed_data = np.log(matrix + 1)
    print("Apply logarithmic transformation (np.log(array+1)) to normalize skewed data : ", normalize_skewed_data)

def copy_operations_shallow(matrix):

    #Create a shallow copy of the dataset and modify one cycle. Observe if the original changes
    shallowcopy = matrix.view()
    print("Create a shallow", shallowcopy)
    shallowcopy[0, 0] = 100
    print("Create a shallow after change", shallowcopy)

    print("Original", matrix)
    print(np.equal(matrix, shallowcopy))

def copy_operations_deep(matrix):
    #Create a deep copy of the dataset and modify one cycle. Observe if the original changes.
    deep_copy = matrix.copy()
    print("Create a deep", deep_copy)
    deep_copy[0, 0] = 100

    print("After change of deep copy matrix : ", deep_copy)

    print("Original", matrix)

    print(np.equal(matrix, deep_copy))

def filtering_with_conditions(matrix):
    #Extract all test cases in Cycle 2 that take more than 30 seconds.
    second_matrix = matrix[1, :]
    print("Cycle 2 : ", second_matrix)
    
    gretaer_30 = second_matrix[second_matrix > 30]
    print("Cycle 2 > 30 : ", gretaer_30)

    # Identify tests that consistently (in every cycle) take more than 25 seconds.
    print("orif¥ginal matrix : ", matrix)
    consistent = np.all(matrix > 25, axis=0)
    print("Consistent : ", consistent)
    print("Consistent : ", consistent.shape)
    print("Shape of matrix : ", matrix.shape)
    print("Test consistently more than 25 : ", matrix[:, consistent])


    # Replace all execution times below 10 seconds with 10 (minimum thresholding).
    matrix[matrix < 10] = 10
    print("Updated matrix : ", matrix)



if __name__ == "__main__":

    #create synthetic data
    matrix = create_matrix()
    print(matrix)

    #1. Statistical analysis
    statistical_analysis(matrix)

    #2. Slicing Operations
    slicing_operations(matrix)

    #3. Arithmetic Operations
    arithmetic_operation(matrix)

    #4. Power Functions
    power_functions(matrix)

    #5. Copy Operations
    copy_operations_shallow(matrix)
    copy_operations_deep(matrix)

    #6. Filtering with Conditions 
    filtering_with_conditions(matrix)
