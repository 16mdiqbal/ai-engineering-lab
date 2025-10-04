import numpy as np
import pandas as pd
from pathlib import Path
from DataAnalyser import DataAnalyzer

# Inherit DataAnalyzer class to perform specific analysis on Corona data

class CoronaDataAnalysis(DataAnalyzer):

    def run_testcases(self):
        # 1. Display total confirmed, death, and recovered cases for each region.
        print("1. Summarizing data by WHO Region.")
        summary = self.summarize_data('WHO Region')
        print(summary)

        print("\n" + "="*50 + "\n")

        # 2. Exclude entries where confirmed cases are < 10.
        print("2. Filtering data to exclude entries with confirmed cases < 10.")
        filtered = self.filter_data('Confirmed', 10)
        print(filtered)

        print("\n" + "="*50 + "\n")

        # 3. Identify Region with Highest Confirmed Cases
        print("3. Identifying region with highest confirmed cases.")
        highest_region = summary.iloc[0]
        print(f"Region with highest confirmed cases: {highest_region['WHO Region']} with {highest_region['Confirmed']} cases.")

        print("\n" + "="*50 + "\n")

        # 4. Sort Data by Confirmed Cases and Save sorted dataset into a new CSV file.
        print("4. Sorting data by confirmed cases and saving to a new CSV file.")
        summary_sorted = self.sort_data('Confirmed', ascending=True)
        output_file_path = Path(__file__).resolve().parent.parent / 'assignment' / 'country_wise_sorted.csv'
        output_file_path.parent.mkdir(parents=True, exist_ok=True)
        self.export_data(summary_sorted, output_file_path)

        print("\n" + "="*50 + "\n")

        # 5. Top 5 Countries by Case Count
        print("5. Top 5 countries by confirmed cases:")
        top_5_countries = self.get_top_n(5, 'Confirmed')
        print(f"Top 5 countries by confirmed cases:\n{ top_5_countries[['Country/Region', 'Confirmed']] }")

        print("\n" + "="*50 + "\n")

        # 6. Region with Lowest Death Count
        print("6. Identifying region with lowest death count.")
        lowest_death_region = self.get_bottom_n(5, 'Deaths')
        print(f"Regions with lowest death count (bottom 5 by Deaths):\n{lowest_death_region[['Country/Region','Deaths']]}")

        print("\n" + "="*50 + "\n")

        # 7. India’s Case Summary (as of snapshot date)
        print("7. India's case summary:")
        india_data = self.load_data()
        india_summary = india_data[india_data['Country/Region'] == 'India']
        if india_summary.empty:
            print("No data found for India.")
        else:
            print(india_summary)

        print("\n" + "="*50 + "\n")

        # 8. Calculate Mortality Rate by Region
        print("8. Calculating mortality rate by region.")
        mortality_rates = self.calculate_mortality_recovery_rates(sort_by_column='Mortality Rate', ascending=False)
        print(mortality_rates[['Country/Region','WHO Region','Mortality Rate']].head(10))

        print("\n" + "="*50 + "\n")

        # 9. Compare Recovery Rates Across Regions
        print("9. Comparing recovery rates across regions.")
        recovery_rates = self.calculate_mortality_recovery_rates(sort_by_column='Recovery Rate', ascending=False)
        print(recovery_rates[['Country/Region','WHO Region','Recovery Rate']].head(10))

        print("\n" + "="*50 + "\n")

        # 10. Detect Outliers in Case Counts
        print("10. Detecting outliers in case counts.")
        outliers = self.detect_outliers('Confirmed')
        if outliers.empty:
            print("No outliers detected using mean ± 2*std.")
        else:
            print(outliers[['Country/Region','Confirmed']])

        print("\n" + "="*50 + "\n")

        # 11. Group Data by Region
        print("11. Grouping data by WHO Region.")
        grouped = self.group_data(['WHO Region'])
        print(grouped.head())

        print("\n" + "="*50 + "\n")

        # 12. Identify Regions with Zero Recovered Cases
        print("12. Identifying rows with zero recovered cases.")
        zero_recovered = self.identify_zero_recovered('Recovered')
        if zero_recovered.empty:
            print("No rows with zero recovered cases.")
        else:
            print(zero_recovered[['Country/Region','WHO Region','Recovered']])

        # Return a dictionary for potential programmatic use
        return {
            'summary': summary,
            'filtered': filtered,
            'highest_region': highest_region,
            'top_5_countries': top_5_countries,
            'lowest_death_region': lowest_death_region,
            'india_summary': india_summary,
            'mortality_rates': mortality_rates,
            'recovery_rates': recovery_rates,
            'outliers': outliers,
            'grouped': grouped,
            'zero_recovered': zero_recovered
        }



if __name__ == "__main__":
    file_path = Path(__file__).resolve().parent.parent / 'assignment' / 'country_wise_latest.csv'
    analysis = CoronaDataAnalysis(str(file_path))
    results = analysis.run_testcases()
