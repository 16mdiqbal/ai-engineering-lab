from collections.abc import Sequence

import numpy as np
import pandas as pd
from CSVHandler import CSVHandler

class DataAnalyzer(CSVHandler):
    def __init__(self, file_path):
        super().__init__(file_path)

    def summarize_data(self, column_name: str='WHO Region', sort_by: str='Confirmed'):
        """ 1. Display total confirmed, death, and recovered cases for each region."""
        df  = self.load_data()

        required_columns = ['Confirmed', 'Deaths', 'Recovered']
        for column in required_columns:
            if column not in df.columns:
                raise ValueError(f"Column '{column}' not found in the dataset.")

        # dynamically pass column name to groupby function
        return (
            df.groupby(column_name)[required_columns]
                .sum()
                .reset_index()
                .sort_values(by=sort_by, ascending=False)
        )

    def filter_data(self, column_name='Confirmed', threshold=10):
        """ 2. Exclude entries where confirmed cases are < 10."""
        df  = self.load_data()
        if column_name not in df.columns:
            raise ValueError(f"Column '{column_name}' not found in the dataset.")

        return df[df[column_name] > threshold] 
    
    def sort_data(self, column_name='Confirmed', ascending=True):
        """ 4. Sort Data by Confirmed Cases and Save sorted dataset into a new CSV file."""
        df  = self.load_data()
        if column_name not in df.columns:
            raise ValueError(f"Column '{column_name}' not found in the dataset.")

        return df.sort_values(by=column_name, ascending=ascending)
        

    def get_top_n(self, n=5, column_name='Confirmed'):
        """ 5. Top 5 Countries by Case Count """
        df  = self.load_data()
        return df.sort_values(by=column_name, ascending=False).head(n)
    
    def get_bottom_n(self, n=5, column_name='Deaths'):
        """ 6. Region with Lowest Death Count """
        df  = self.load_data()
        return df.sort_values(column_name, ascending=True).head(n)
    
    def calculate_mortality_recovery_rates(self, sort_by_column='Mortality Rate', ascending=False):
        """ Calculate both Mortality and Recovery Rates by Region """
        df  = self.load_data(copy=True)

        required_columns = ['Country/Region', 'WHO Region', 'Confirmed', 'Deaths', 'Recovered', 'Mortality Rate', 'Recovery Rate']
        for column in required_columns:
            # Check if columns exist in the DataFrame and 'Mortality Rate', 'Recovery Rate' are new columns to be created
            if column not in df.columns and column not in ['Mortality Rate', 'Recovery Rate']:
                raise ValueError(f"Column '{column}' not found in the dataset.")

        df['Mortality Rate'] = (df['Deaths'] / df['Confirmed']) * 100
        df['Recovery Rate'] = (df['Recovered'] / df['Confirmed']) * 100

        return (
            df[required_columns]
            .sort_values(by=sort_by_column, ascending=ascending)
        )


    def detect_outliers(self, column_name='Confirmed', z: float = 2.0):
        """ 10. Detect Outliers in Case Counts and Use mean ± 2*std deviation."""
        df  = self.load_data()

        if column_name not in df.columns:
            raise ValueError(f"Column '{column_name}' not found in the dataset.")

        col = df[column_name].astype(float)
        mean = df[column_name].mean()
        std_dev = df[column_name].std()
        lower_bound = mean - z * std_dev
        upper_bound = mean + z * std_dev
        outliers = df[(col < lower_bound) | (col > upper_bound)]
        return outliers
    

    def group_data(self, group_by_columns: Sequence[str], ascending=False):
        """ Group Data by Country and Region """
        df  = self.load_data()

        for column in group_by_columns:
            if column not in df.columns:
                raise ValueError(f"Column '{column}' not found in the dataset.")

        group_data = (
            df.groupby(group_by_columns)[['Confirmed', 'Deaths', 'Recovered']]
            .sum()
            .sort_values(by='Confirmed', ascending=ascending)
            .reset_index()
        )

        return group_data

    def identify_zero_recovered(self, column_name:str='Recovered'):
        """ Identify Regions with Zero Recovered Cases """
        df  = self.load_data()
        if column_name not in df.columns:
            raise ValueError(f"Column '{column_name}' not found in the dataset.")

        zero_recovered =  df[df[column_name] == 0]
        return zero_recovered

    def fetch_data_by_country_by_column(self, country_names: Sequence[str],
                                        column_names: Sequence[str],
                                        filter_by: str='Country/Region'):
        """ Fetch data for a specific country """
        df  = self.load_data()

        for column in column_names:
            if column not in df.columns:
                raise ValueError(f"Column '{column}' not found in the dataset.")

        data_based_on_country = df.loc[df[filter_by].isin(country_names), column_names]
        return data_based_on_country
