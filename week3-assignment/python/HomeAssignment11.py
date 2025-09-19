import numpy as np

class TestReport:
    
    def __init__(self, execution_times):
        self.execution_times = np.array(execution_times)

    def average_time(self):
        return np.mean(self.execution_times)

    def max_time(self):
        return np.max(self.execution_times)

class RegressionReport(TestReport):

    def __init__(self, execution_times):
        super().__init__(execution_times)


    def slow_tests(self, threshold):
        return self.execution_times[self.execution_times > threshold]


if __name__ == "__main__":
    tc_execution_time = [5, 7, 9, 4, 12, 16, 11, 8, 9]
    report = RegressionReport(tc_execution_time)

    # display the average execution time
    average_execution_time = report.average_time()
    print(f"Average execution time: {average_execution_time} seconds")

    # display the maximum execution time
    max_execution_time = report.max_time()
    print(f"Maximum execution time: {max_execution_time} seconds")

    # display the slow tests
    threashold = 10
    slow_tests = report.slow_tests(threashold)
    print(f"Slow tests (execution time > {threashold} seconds): {slow_tests}")



    

