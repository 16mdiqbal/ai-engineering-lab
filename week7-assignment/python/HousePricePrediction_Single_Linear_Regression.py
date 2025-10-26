from pathlib import Path

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
from scipy import stats
from pandas.core.interchange.dataframe_protocol import DataFrame
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from python_script.covid_analysis import CSVHandler
from python_script.plot_images import PlotImages


class HousePricePrediction_Single_Linear_Regression(CSVHandler, PlotImages):

    def __init__(self, file_path: str|Path, figure_dir: str|Path | None = None):
        CSVHandler.__init__(self, file_path)
        PlotImages.__init__(self, figure_dir)  # PlotImages handles dynamic path

    def feature_target_selection(self, df: DataFrame, feature_col: str, target_col: str):
        X = df[[feature_col]]  # Independent variable
        y = df[target_col]    # Dependent variable
        return X, y

    def train_test_split_data_set(self, X: DataFrame, y: DataFrame, test_size: float = 0.2, random_state: int = 42):
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)
        return X_train, X_test, y_train, y_test

    def train_model(self, X, y):
        model = LinearRegression()

        model.fit(X, y)
        return model

    def predict_price(self, model, X_new):
        return model.predict(X_new)

    def format_prediction_output(self, predicted_price, square_footage, lower_bound, upper_bound,
                                 margin_of_error, train_min, train_max, rmse=None):
        """Format and display the prediction output in a nicely formatted box.

        Args:
            predicted_price: The predicted house price
            square_footage: Input square footage
            lower_bound: Lower bound of confidence interval
            upper_bound: Upper bound of confidence interval
            margin_of_error: Margin of error for the prediction
            train_min: Minimum value in training data
            train_max: Maximum value in training data
            rmse: Root Mean Squared Error (optional)
        """
        box_width = 70

        # Helper function to pad line correctly
        def format_line(text, color_code="", end_code="\033[0m"):
            """Format a line with color and proper padding"""
            visible_length = len(text)
            padding_needed = box_width - visible_length - 1  # -1 for the space after │
            if color_code:
                return f"│ {color_code}{text}{end_code}{' ' * padding_needed}│"
            else:
                return f"│ {text}{' ' * padding_needed}│"

        # Print box header
        print("\n" + "┌" + "─" * box_width + "┐")

        # Format prediction lines
        line1 = f"✓ Predicted Price: ${predicted_price:,.2f}"
        line2 = f"Square Footage: {square_footage:.0f} sqft"

        print(format_line(line1, "\033[1;32m"))
        print(format_line(line2, "\033[1m"))

        # Show confidence interval
        if rmse is not None:
            line3 = f"95% Confidence Interval: ${lower_bound:,.2f} - ${upper_bound:,.2f}"
            interval_width_pct = ((upper_bound - lower_bound) / predicted_price) * 100
            line4 = f"Interval Width: {margin_of_error:,.2f} ({interval_width_pct:.1f}% of prediction)"

            print(format_line(line3, "\033[0;36m"))
            print(format_line(line4, "\033[2m"))

            # Show data range context
            within_range = train_min <= square_footage <= train_max
            if not within_range:
                warning_text = "⚠ Warning: Below training range" if square_footage < train_min else "⚠ Warning: Above training range"
                line5 = f"Training range: {train_min:.0f} - {train_max:.0f} sqft"

                print(format_line(warning_text, "\033[1;33m"))
                print(format_line(line5, "\033[2m"))
            else:
                line5 = f"✓ Within training range ({train_min:.0f} - {train_max:.0f} sqft)"
                print(format_line(line5, "\033[1;32m"))

        # Print box footer
        print("└" + "─" * box_width + "┘")

    def predict_from_user_input(self, model, X_train, rmse=None, r2=None):
        """Interactive loop to predict house prices based on user input square footage.

        Args:
            model: Trained LinearRegression model
            X_train: Training data DataFrame (used to calculate prediction intervals)
            rmse: Root Mean Squared Error from model evaluation (optional)
            r2: R² score from model evaluation (optional)
        """

        # Calculate training data statistics for prediction intervals
        X_mean = X_train.values.mean()
        X_std = X_train.values.std()
        n = len(X_train)
        train_min = X_train.values.min()
        train_max = X_train.values.max()

        # t-value for 95% confidence interval (df = n-2 for simple linear regression)
        t_value = stats.t.ppf(0.975, n - 2)

        while True:
            try:
                user_input = input("\nEnter the square footage of the house (or 'q' to quit): ")
                if user_input.lower() == 'q':
                    print("Exiting prediction mode.")
                    break

                square_footage = float(user_input)
                if square_footage <= 0:
                    print("Please enter a positive number for square footage.")
                    continue

                # Create DataFrame with proper column name to avoid sklearn warning
                new_square_footage = pd.DataFrame([[square_footage]], columns=['Square_Footage'])
                predicted_price = self.predict_price(model, new_square_footage)

                # Calculate prediction interval based on distance from training mean
                # Formula: PI = ŷ ± t * RMSE * sqrt(1 + 1/n + (x - x̄)²/(n * s²))
                distance_from_mean = (square_footage - X_mean) ** 2
                variance_factor = np.sqrt(1 + 1/n + distance_from_mean / (n * X_std ** 2))
                margin_of_error = t_value * rmse * variance_factor

                lower_bound = predicted_price[0] - margin_of_error
                upper_bound = predicted_price[0] + margin_of_error

                # Display formatted prediction output
                self.format_prediction_output(
                    predicted_price=predicted_price[0],
                    square_footage=square_footage,
                    lower_bound=lower_bound,
                    upper_bound=upper_bound,
                    margin_of_error=margin_of_error,
                    train_min=train_min,
                    train_max=train_max,
                    rmse=rmse
                )

            except ValueError:
                print("Invalid input. Please enter a valid number or 'q' to quit.")
            except KeyboardInterrupt:
                print("\n\nExiting prediction mode.")
                break

    def main(self):
        #1. Load the Dataset
        #o Load the provided dataset using Pandas.
        #o Retain only the columns "Square Footage" and "Price# for model building.

        df = self.load_data()
        df = df[['Square_Footage', 'House_Price']].dropna()


        #2. Exploratory Data Analysis (EDA)
        # o Display the first few rows of the dataset.
        print(df.head())

        # o Check for missing or null values and handle them appropriately.
        print(f"Missing values : \n {df.isnull().sum()} \n")

        #o Visualize the relationship between Square Footage and Price using a scatter
        fig_eda = self.plot_scatter(df, 'Square_Footage', 'House_Price')
        self.save_figure(fig_eda, fig_eda.axes[0], 'scatter_square_footage_price.png')

        # 3. Feature and Target Selection
        #o Assign Square Footage as the independent variable(X).
        #o Assign Price as the dependent variable(Y).
        X, y = self.feature_target_selection(df, 'Square_Footage', 'House_Price')

        # 4. Train - Test Split
        # o Split the dataset into training and testing sets using an 80 - 20 ratio
        X_train, X_test, y_train, y_test = self.train_test_split_data_set(X, y, test_size=0.2, random_state=42)

        # 5. Model Building
        # o Create a Linear Regression model using LinearRegression from sklearn.linear_model.
        # o Fit the model on the training data.
        model = self.train_model(X_train, y_train)

        # o Display the intercept (b₀) and coefficient (b₁) of the regression line.
        print(f"Model Intercept (b0): {model.intercept_}")
        print(f"Model Coefficient (b1): {model.coef_[0]}")

        # 6. Prediction and Evaluation
        # o Predict the house prices for the test set.

        y_pred = self.predict_price(model, X_test)

        # o Calculate and print the following evaluation metrics:
        #  Mean Squared Error (MSE)
        #  Root Mean Squared Error (RMSE)
        #  R² Score (Coefficient of Determination)
        mse_val = mean_squared_error(y_test, y_pred)
        rmse_val = np.sqrt(mse_val)
        r2_val = r2_score(y_test, y_pred)

        print(f"Mean Squared Error (MSE): {mse_val}")
        print(f"Root Mean Squared Error (RMSE): {rmse_val}")
        print(f"R^2 Score: {r2_val}")


        # Enhanced performance metrics display
        print(f"\n📊 Model Performance Metrics:")
        if r2_val >= 0.95:
            print(f"   • Model Quality: \033[1;32mExcellent\033[0m ✓")
        elif r2_val >= 0.85:
            print(f"   • Model Quality: \033[1;33mGood\033[0m")
        else:
            print(f"   • Model Quality: \033[1;31mNeeds Improvement\033[0m")
        print()

        # 7. Visualization
        # o Combine both visualizations into a single figure with subplots
        fig, axes = plt.subplots(1, 2, figsize=(16, 6))
        ax1, ax2 = axes

        # Left subplot: training data + regression line
        sns.scatterplot(x=X_train['Square_Footage'], y=y_train, color='blue', label='Training Data', ax=ax1)
        # Sort X_train for smooth line and ensure it's a DataFrame with proper column names
        X_train_sorted = X_train.sort_values('Square_Footage')
        ax1.plot(X_train_sorted['Square_Footage'], model.predict(X_train_sorted), color='red', label='Regression Line')
        ax1.set_title("Regression Line: Price vs Square Footage")
        ax1.set_xlabel("Square Footage")
        ax1.set_ylabel("Price")
        ax1.legend()
        ax1.grid(True, alpha=0.3)


        # Right subplot: Actual vs Predicted with diagonal reference
        sns.scatterplot(x=y_test, y=y_pred, color='green', ax=ax2)

        # Add regression line (best-fit line for predictions)
        min_val = min(y_test.min(), np.min(y_pred))
        max_val = max(y_test.max(), np.max(y_pred))
        # Plot the perfect prediction diagonal explicitly with numeric x and y arrays
        ax2.plot([min_val, max_val], [min_val, max_val], color='blue', linestyle='--', label='Perfect Prediction')

        ax2.set_title("Actual vs Predicted House Prices")
        ax2.set_xlabel("Actual Prices")
        ax2.set_ylabel("Predicted Prices")
        ax2.legend()
        ax2.grid(True, alpha=0.3)
        plt.tight_layout()


        # save figure
        self.save_figure(fig, axes[0], 'regression_actual_vs_predicted.png')
        plt.close(fig)  # Close the figure to avoid popup
        plt.close(fig_eda)  # Close the EDA figure as well

        # 8. Prediction on New Data
        # o Predict the price of a house with a specified square footage from user input
        print("\n" + "=" * 52)
        print("House Price Prediction for User Input Square Footage")
        print("=" * 52)
        self.predict_from_user_input(model, X_train, rmse=rmse_val, r2=r2_val)

if __name__ == '__main__':
    # Use the centralized resources folder for the COVID dataset
    file_path = Path(__file__).resolve().parents[2] / 'resources' / 'house_price_regression_dataset.csv'

    if not file_path.exists():
        raise FileNotFoundError(f"Dataset file not found: {file_path}")

    house_price_prediction = HousePricePrediction_Single_Linear_Regression(file_path)
    house_price_prediction.main()
