from pathlib import Path
import warnings

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler

from python_script.covid_analysis import DataAnalyzer
from python_script.plot_images import PlotImages

# Suppress FutureWarnings from seaborn/pandas compatibility issues
warnings.filterwarnings('ignore', category=FutureWarning, module='seaborn')


class CovidEDA(DataAnalyzer, PlotImages):
    def __init__(self, file_path: str|Path, figure_dir: str|Path | None = None):
        # Properly initialize both parent classes
        DataAnalyzer.__init__(self, file_path)
        PlotImages.__init__(self, figure_dir)  # PlotImages handles dynamic path


    def get_filtered_columns(self, columns: str|list = 'Confirmed'):
        """ Return only specified column(s) from the dataset """
        df = self.load_data()

        # Set upto display floats with 2 decimal places
        pd.options.display.float_format = '{:.2f}'.format

        if isinstance(columns, str):
            if columns not in df.columns:
                raise ValueError(f"Column '{columns}' not found in the dataset.")
            df = df.loc[:, [columns]]
            columns_list = [columns]
        elif isinstance(columns, list):
            missing_columns = [col for col in columns if col not in df.columns]
            if missing_columns:
                raise ValueError(f"Columns not found in the dataset: {missing_columns}")
            df = df.loc[:, columns]
            columns_list = columns
        else:
            raise TypeError("Parameter 'columns' must be a string or a list of strings.")

        # Clean data: drop rows with NaN in specified columns
        # Convert to numeric (in case some entries are strings)
        for col in columns_list:
            if col in df.columns:
                df.loc[:, col] = pd.to_numeric(df[col], errors='coerce')

        # Drop rows that couldn't be converted (if any)
        df.dropna(subset=columns_list, inplace=True)

        return df

    def remove_outlier_IQR(self, df: pd.DataFrame, columns: str | list):
        """ Remove outliers from DataFrame column(s) using the IQR method

        Args:
            df: Input DataFrame
            columns: Single column name (str) or list of column names to remove outliers from

        Returns:
            DataFrame with outliers removed from specified column(s)
        """
        # Convert single column to list for uniform processing
        if isinstance(columns, str):
            columns = [columns]
        elif not isinstance(columns, list):
            raise TypeError("Parameter 'columns' must be a string or a list of strings.")

        # Validate all columns exist
        missing_columns = [col for col in columns if col not in df.columns]
        if missing_columns:
            raise ValueError(f"Columns not found in the DataFrame: {missing_columns}")

        # Start with the original dataframe
        cleaned_df = df.copy()

        # Iterate through each column and remove outliers
        for column in columns:
            # Calculate IQR for current column
            Q1 = cleaned_df[column].quantile(0.25)
            Q3 = cleaned_df[column].quantile(0.75)
            IQR = Q3 - Q1

            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR

            # Filter out outliers for this column
            cleaned_df = cleaned_df[(cleaned_df[column] >= lower_bound) & (cleaned_df[column] <= upper_bound)]

        # Reset index to have sequential indices from 0 to n-1
        cleaned_df = cleaned_df.reset_index(drop=True)

        return cleaned_df


    def normalize_data_standard_Scaler(self, df: pd.DataFrame, columns: str | list):
        """ Normalize DataFrame column(s) using StandardScaler (mean=0, std=1)

        Args:
            df: Input DataFrame
            columns: Single column name (str) or list of column names to normalize

        Returns:
            DataFrame with specified column(s) normalized
        """
        # Convert single column to list for uniform processing
        if isinstance(columns, str):
            columns = [columns]
        elif not isinstance(columns, list):
            raise TypeError("Parameter 'columns' must be a string or a list of strings.")

        # Validate all columns exist
        missing_columns = [col for col in columns if col not in df.columns]
        if missing_columns:
            raise ValueError(f"Columns not found in the DataFrame: {missing_columns}")

        # Create a copy to avoid modifying the original DataFrame
        cleaned_df = df.copy()

        scaler = StandardScaler()
        # fit_transform returns numpy array, convert back to DataFrame with proper dtype
        normalized_values = scaler.fit_transform(cleaned_df[columns])
        normalized_df = pd.DataFrame(
            normalized_values,
            columns=[f"{col}_normalized" for col in columns],
            index=cleaned_df.index
        )

        return normalized_df


    def run_testcases(self):

        # 1. Keep only the columns "Confirmed" and "New cases" for analysis.
        print("1. Filtering data to keep only 'Confirmed' and 'New cases' columns.")
        filtered_df = self.get_filtered_columns(['Confirmed', 'New cases'])
        print(filtered_df.head())

        print("\n" + "=" * 50 + "\n")

        # 2. Compute Statistical Measures
        # Calculate and print Mean
        mean_values = filtered_df.mean()
        median_values = filtered_df.median()
        variance_values = filtered_df.var()
        std_values = filtered_df.std()
        corr_matrix = filtered_df.corr()

        print("Mean:\n", mean_values)
        print("\nMedian:\n", median_values)
        print("\nVariance:\n", variance_values)
        print("\nStandard Deviation:\n", std_values)
        print("\nCorrelation Matrix:\n", corr_matrix)

        print("\n" + "=" * 50 + "\n")

        # 3. Detect and Remove Outliers using IQR method and display the cleaned dataset.
        # Identify outliers in both Confirmed and New cases.
        print("3. Detecting and removing outliers using IQR method.")
        print("Shape of data before removing outliers:", filtered_df.shape)

        cleaned_df = self.remove_outlier_IQR(filtered_df, ['Confirmed', 'New cases'])
        print("Cleaned Data (after removing outliers):\n", cleaned_df)
        print("Shape of data after removing outliers:", cleaned_df.shape)

        print("Store cleaned data to 'cleaned_covid_data.csv'")
        output_file_path = Path(__file__).resolve().parent.parent / 'assignment' / 'cleaned_covid_data.csv'
        self.export_data(cleaned_df, str(output_file_path))

        print("\n" + "=" * 50 + "\n")

        # 3.1 Plot correlation heatmap for cleaned data (BEFORE normalization)
        print("3.1. Plotting correlation heatmap for cleaned data (BEFORE normalization).")
        fig = self.plot_heatmap(cleaned_df, figsize=(8, 6), annot=True, cmap='coolwarm')
        plt.suptitle('Correlation Heatmap - Original Data', fontsize=14, y=0.98)
        plt.subplots_adjust(top=0.88)
        self.save_figure(fig, fig.axes[0], "heatmap_original_data.png")
        plt.show()

        print("\n" + "=" * 50 + "\n")

        # 3.2 Plot histograms BEFORE normalization
        print("3.2. Plotting histograms for data BEFORE normalization.")
        fig = self.plot_histogram(cleaned_df, list(cleaned_df.columns), bins=30, kde=True, figsize=(12, 7))
        plt.suptitle('Histograms BEFORE Normalization', fontsize=16, y=0.98)
        plt.subplots_adjust(top=0.92)
        self.save_figure(fig, fig.axes[0], "histograms_before_normalization.png")
        plt.show()


        # 4. Normalize the "Confirmed" and "New cases" columns using StandardScaler and display the normalized dataset.
        print("\n" + "=" * 50 + "\n")
        print("4. Normalizing 'Confirmed' and 'New cases' columns using StandardScaler.")
        normalized_df = self.normalize_data_standard_Scaler(cleaned_df, ['Confirmed', 'New cases'])
        print("Normalized Data:\n", normalized_df)

        print("Mean after normalization:\n", normalized_df.mean())
        print("\nStandard Deviation after normalization:\n", normalized_df.std())

        # 5. Plot histograms for normalized data (AFTER normalization)
        print("\n" + "=" * 50 + "\n")
        print("5. Plotting histograms for data AFTER normalization.")
        fig = self.plot_histogram(normalized_df, list(normalized_df.columns), bins=30, kde=True, figsize=(12, 7))
        plt.suptitle('Histograms AFTER Normalization', fontsize=16, y=0.98)
        plt.subplots_adjust(top=0.92)
        self.save_figure(fig, fig.axes[0], "histograms_after_normalization.png")
        plt.show()

        # 6. Plot correlation heatmap for normalized data (AFTER normalization)
        print("\n" + "=" * 50 + "\n")
        print("6. Plotting correlation heatmap for normalized data (AFTER normalization).")
        fig = self.plot_heatmap(normalized_df, figsize=(8, 6), annot=True, cmap='coolwarm')
        plt.suptitle('Correlation Heatmap - Normalized Data', fontsize=14, y=0.98)
        plt.subplots_adjust(top=0.88)
        self.save_figure(fig, fig.axes[0], "heatmap_normalized_data.png")
        plt.show()


if __name__ == '__main__':
    # Use the centralized resources folder for the COVID dataset
    file_path = Path(__file__).resolve().parents[2] / 'resources' / 'country_wise_latest.csv'
    if not file_path.exists():
        print(f"Covid 19 data file not found at {file_path}. Exiting.")
        raise SystemExit(1)

    covid_eda = CovidEDA(file_path)
    covid_eda.run_testcases()