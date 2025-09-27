import numpy as np
import pandas as pd
from CSVHandler import CSVHandler

class DataAnalyzer(CSVHandler):
    def __init__(self, file_path):
        super().__init__(file_path)

    def summarize_data(self, column_name):
        ''' 1. Display total confirmed, death, and recovered cases for each region.'''
        df  = self.load_data()
        # dynamically pass column name to groupby function
        return df.groupby(column_name)[['Confirmed', 'Deaths', 'Recovered']].sum().reset_index().sort_values(by='Confirmed', ascending=False)

    def filter_data(self, column_name='Confirmed', threshold=10):
        ''' 2. Exclude entries where confirmed cases are < 10.'''
        df  = self.load_data()
        return df[df[column_name] > threshold] 
    
    def sort_data(self, column_name='Confirmed', ascending=True):
        ''' 4. Sort Data by Confirmed Cases and Save sorted dataset into a new CSV file.'''
        df  = self.load_data()
        return df.sort_values(by=column_name, ascending=ascending)
        

    def get_top_n(self, n=5, column_name='Confirmed'):
        ''' 5. Top 5 Countries by Case Count '''
        df  = self.load_data()
        return df.sort_values(by=column_name, ascending=False).head(n)
    
    def get_bottom_n(self, n=5, column_name='Deaths'):
        ''' 6. Region with Lowest Death Count '''
        df  = self.load_data()
        return df.sort_values(column_name, ascending=True).head(n)
    
    def calculate_mortality_rate(self, ascending=False):
        ''' 8. Calculate Mortality Rate by Region '''
        df  = self.load_data()
        df['Mortality Rate'] = (df['Deaths'] / df['Confirmed']) * 100
        return df[['Country/Region', 'WHO Region', 'Confirmed', 'Deaths', 'Mortality Rate']].sort_values(by='Mortality Rate', ascending=ascending)
    
    def calculate_recovery_rate(self, ascending=False):
        ''' 9. Compare Recovery Rates Across Regions '''
        df  = self.load_data()
        df['Recovery Rate'] = (df['Recovered'] / df['Confirmed']) * 100
        return df[['Country/Region', 'WHO Region', 'Confirmed', 'Recovered', 'Recovery Rate']].sort_values(by='Recovery Rate', ascending=ascending)
    
    def detect_outliers(self, column_name='Confirmed'):
        ''' 10. Detect Outliers in Case Counts and Use mean ± 2*std deviation.'''
        df  = self.load_data()
        mean = df[column_name].mean()
        std_dev = df[column_name].std()
        lower_bound = mean - 2 * std_dev
        upper_bound = mean + 2 * std_dev
        outliers = df[(df[column_name] < lower_bound) | (df[column_name] > upper_bound)]
        return outliers
    

    def group_data(self, group_by_columns, ascending=False):
        ''' Group Data by Country and Region '''
        df  = self.load_data()
        return df.groupby(group_by_columns)[['Confirmed', 'Deaths', 'Recovered']].sum().sort_values(by='Confirmed', ascending=ascending).reset_index()

    def identify_zero_recovered(self, column_name='Recovered'):
        ''' Identify Regions with Zero Recovered Cases '''
        df  = self.load_data()
        return df[df[column_name] == 0]