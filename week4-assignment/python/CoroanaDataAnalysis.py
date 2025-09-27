import numpy as np
import pandas as pd
from DataAnalyser import DataAnalyzer


class CoroanaDataAnalysis:
    
        

    if __name__ == "__main__":
        file_path = './week4-assignment/assignment/country_wise_latest.csv'
        analyzer = DataAnalyzer(file_path)

        # 1. Display total confirmed, death, and recovered cases for each region.
        print("1. Summarizing data by WHO Region.")
        summary = analyzer.summarize_data('WHO Region')
        print(summary)

        print("\n" + "="*50 + "\n")


        # 2. Exclude entries where confirmed cases are < 10.
        print("2. Filtering data to exclude entries with confirmed cases < 10.")
        filtered = analyzer.filter_data('Confirmed', 10)
        print(filtered)

        print("\n" + "="*50 + "\n")

        # 3. Identify Region with Highest Confirmed Cases
        # use the summary from step 1
        print("3. Identifying region with highest confirmed cases.")
        highest_region = summary.iloc[0]
        print(f"Region with highest confirmed cases: {highest_region['WHO Region']} with {highest_region['Confirmed']} cases.")


        print("\n" + "="*50 + "\n")


        # 4. Sort Data by Confirmed Cases and Save sorted dataset into a new CSV file.
        print("4. Sorting data by confirmed cases and saving to a new CSV file.")
        summary_sorted = analyzer.sort_data('Confirmed', ascending=True)
        analyzer.export_data(summary_sorted, './week4-assignment/assignment/country_wise_sorted.csv')

        print("\n" + "="*50 + "\n")

        # 5. Top 5 Countries by Case Count
        print("5. Top 5 countries by confirmed cases:")
        top_5_countries = analyzer.get_top_n(5, 'Confirmed')
        print(f"Top 5 countries by confirmed cases:\n{ top_5_countries[['Country/Region', 'Confirmed']] }")

        print("\n" + "="*50 + "\n")

        # 6. Region with Lowest Death Count
        print("6. Identifying region with lowest death count.")
        lowest_death_region = analyzer.get_bottom_n(5, 'Deaths')
        print(f"Region with lowest death count: {lowest_death_region}")


        print("\n" + "="*50 + "\n")


        # 7. India’s Case Summary (as of April 29, 2020)
        print("7. India's case summary:")
        india_data = analyzer.load_data()
        india_summary = india_data[india_data['Country/Region'] == 'India']
        print(india_summary)

        print("\n" + "="*50 + "\n")

        # 8. Calculate Mortality Rate by Region
        print("8. Calculating mortality rate by region.")
        mortality_rates = analyzer.calculate_mortality_rate(ascending=False)
        print(mortality_rates)

        print("\n" + "="*50 + "\n")

        # 9. Compare Recovery Rates Across Regions
        print("9. Comparing recovery rates across regions.")
        recovery_rates = analyzer.calculate_recovery_rate(ascending=False)
        print(recovery_rates)

        print("\n" + "="*50 + "\n")

        # 10. Detect Outliers in Case Counts and Use mean ± 2*std deviation.
        print("10. Detecting outliers in case counts.")
        outliers = analyzer.detect_outliers('Confirmed')
        print(outliers)

        print("\n" + "="*50 + "\n")

        # Group Data by Country and Region
        print("11. Grouping data by Country and Region.")
        grouped = analyzer.group_data(['WHO Region'])
        print(grouped)

        print("\n" + "="*50 + "\n")

        # Identify Regions with Zero Recovered Cases
        print("12. Identifying regions with zero recovered cases.")
        zero_recovered = analyzer.identify_zero_recovered('Recovered')
        print(zero_recovered)

        print("\n" + "="*50 + "\n")
