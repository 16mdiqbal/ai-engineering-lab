import numpy as np

class ManualTester:
    def analyze(self, data: np.ndarray):
        print("Manual Tester first 5: ", data[:5])

class AutomationTester:
    def analyze(self, data):
        print("Automation Tester fastest: ", data.min())

class PerformanceTester:
    def analyze(self, data):
        print("Performance Tester 95th percentile: ", np.percentile(data, 95))


def show_analysis(tester, data):
    tester.analyze(data)


if __name__ == "__main__":
    manual_tester = ManualTester()
    automation_tester = AutomationTester()
    performance_tester = PerformanceTester()

    # array data
    execution_times = np.array([1.8, 2.1, 1.6, 2.9, 3.2, 1.4, 2.3, 2.7, 3.0, 1.9, 2.2, 2.6, 3.4])
    
    # Show analysis for Manual Tester
    show_analysis(manual_tester, execution_times)

    # SHow analysis for Automation Tester
    show_analysis(automation_tester, execution_times)

    # Show analysis for Performance Tester
    show_analysis(performance_tester, execution_times)