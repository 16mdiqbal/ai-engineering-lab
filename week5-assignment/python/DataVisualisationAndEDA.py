from pathlib import Path
import warnings

import matplotlib.pyplot as plt
import seaborn as sns
from python_script.covid_analysis import DataAnalyzer
from python_script.plot_images import PlotImages

# Suppress FutureWarnings from seaborn/pandas compatibility issues
warnings.filterwarnings('ignore', category=FutureWarning, module='seaborn')

class CovidVisualization(DataAnalyzer, PlotImages):

    def __init__(self, file_path: str|Path, figure_dir: str|Path | None = None):
        super().__init__(file_path)
        if figure_dir is None:
            # Save under week5-assignment/plot_images
            project_root = Path(__file__).resolve().parents[2]
            figure_dir = project_root / 'week5-assignment' / 'plot_images'
        self.figure_dir = Path(figure_dir)
        self.figure_dir.mkdir(parents=True, exist_ok=True)


    def bar_chart_top_10_countries_by_confirmed(self):
        """ Bar Chart: Top 10 Countries by Confirmed Cases """
        top_10 = self.get_top_n(10, 'Confirmed')
        top_10 = top_10[['Country/Region', 'Confirmed']]

        print(top_10)

        fig, ax = plt.subplots(figsize=(14, 6))
        sns.barplot(
            data=top_10,
            x='Country/Region',
            y='Confirmed',
            palette='viridis',
            ax=ax,
            hue='Country/Region'
        )
        ax.set_title('Top 10 Countries by Confirmed COVID-19 Cases')
        plt.xticks(rotation=45)
        return self.save_figure(fig, ax, "bar_chart_top_10_countries_by_confirmed.png")

    def pie_chart_death_distribution_by_region(self):
        """ Pie Chart: Death Distribution by WHO Region """
        summary = self.summarize_data('WHO Region')
        death_distribution = summary[['WHO Region', 'Deaths']]

        fig, ax = plt.subplots(figsize=(8, 8))
        ax.pie(
            death_distribution['Deaths'],
            labels=death_distribution['WHO Region'],
            autopct='%1.1f%%',
            startangle=140,
            colors=sns.color_palette('pastel')
        )
        ax.set_title('Death Distribution by WHO Region')
        return self.save_figure(fig, ax, "pie_chart_death_distribution_by_region.png")

    def line_chart_comapring_confirmed_death_top5(self):
        """ Line Chart: Comparing Confirmed vs Deaths in Top 5 Countries """
        top_5 = self.get_top_n(5, 'Confirmed')
        top_5 = top_5[['Country/Region', 'Confirmed', 'Deaths']]

        fig, ax = plt.subplots(figsize=(10, 6))
        sns.lineplot(
            data=top_5.melt(id_vars='Country/Region', value_vars=['Confirmed', 'Deaths']),
            x='Country/Region',
            y='value',
            hue='variable',
            marker='o',
            ax=ax,
            palette='Set1'
        )
        ax.grid(True, linestyle='-', color='#EEEEEE', alpha=0.5)
        ax.set_title('Comparing Confirmed vs Deaths in Top 5 Countries')
        ax.ticklabel_format(axis='y', style='plain')
        ax.set_ylabel('Confirmed Cases (in Millions)', color='red', fontsize=12)
        ax.yaxis.set_major_formatter(lambda x, _: f'{x / 1_000_000:.1f}M')
        ax.legend(title='Case Type')
        plt.xticks(rotation=45)
        return self.save_figure(fig, ax, "line_chart_comparing_confirmed_death_top5.png")


    def scatter_plot_confirmed_vs_recovered(self):
        """ Scatter Plot: Confirmed vs Recovered Cases """
        # Using summarized data and fetch only relevant columns for scatter plot

        summary = self.summarize_data('WHO Region')[['WHO Region', 'Confirmed', 'Recovered']]
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.scatterplot(
            data=summary,
            x='Confirmed',
            y='Recovered',
            hue='WHO Region',
            size='Confirmed',
            sizes=(20, 200),
            alpha=0.7,
            palette='tab10',
            ax=ax
        )
        ax.set_title('Confirmed vs Recovered Cases by Region')
        ax.set_xlabel('Confirmed Cases')
        ax.set_ylabel('Recovered Cases')
        ax.yaxis.set_major_formatter(lambda x, _: f'{x / 1_000_000:.1f}M')
        ax.xaxis.set_major_formatter(lambda x, _: f'{x / 1_000_000:.1f}M')
        ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
        return self.save_figure(fig, ax, "scatter_plot_confirmed_vs_recovered.png")


    def histogram_mortality_rate_distribution(self):
        """ Histogram: Mortality Rate Distribution """
        df = self.calculate_mortality_recovery_rates(sort_by_column='Mortality Rate', ascending=False)

        fig, ax = plt.subplots(figsize=(10, 6))
        sns.histplot(
            data=df,
            x='Mortality Rate',
            hue='WHO Region',
            bins=10,
            #multiple='stack',
            kde=True,
            ax=ax
        )
        ax.set_title('Mortality Rate Distribution')
        ax.set_xlabel('Mortality Rate (%)')
        ax.set_ylabel('Frequency')
        return self.save_figure(fig, ax, "histogram_mortality_rate_distribution.png")

    def stacked_bar_plot_confirmed_death_recovered__by_country(self):
        """ Stacked Bar Plot: Confirmed, Deaths, Recovered by selected countries """
        countries = ['India', 'Japan', 'Brazil', 'Afghanistan', 'Russia']
        columns = ['Country/Region', 'Confirmed', 'Deaths', 'Recovered']

        # Use the helper defined on the parent class correctly
        data_by_country = self.fetch_data_by_country_by_column(
            country_names=countries,
            column_names=columns,
            filter_by='Country/Region'
        ).set_index('Country/Region')

        #plot_df = (data_by_country.set_index('Country/Region')[['Confirmed', 'Deaths', 'Recovered']].sort_index())

        fig, ax = plt.subplots(figsize=(14, 7))
        data_by_country.plot(
            kind='bar',
            stacked=True,
            colormap='tab20',
            ax=ax
        )
        ax.set_title('Confirmed, Deaths, Recovered by Country (Selected)')
        ax.set_ylabel('Number of Cases')
        ax.yaxis.set_major_formatter(lambda x, _: f'{x / 1_000_000:.1f}M')
        plt.xticks(rotation=45, ha='right')
        return self.save_figure(fig, ax, "stacked_bar_confirmed_death_recovered_by_country.png")

    def box_plot_confirmed_cases_by_region(self):
        """ Box Plot: Confirmed Cases by WHO Region """
        df = self.load_data()

        fig, ax = plt.subplots(figsize=(12, 6))
        sns.boxplot(
            data=df,
            x='WHO Region',
            y='Confirmed',
            hue='WHO Region',
            legend=True,
            palette='Set3',
            ax=ax
        )
        ax.set_title('Box Plot of Confirmed Cases by WHO Region')
        ax.set_ylabel('Confirmed Cases')
        ax.set_yscale('log')  # Use logarithmic scale for better visualization
        ax.yaxis.set_major_formatter(lambda x, _: f'{x / 1_000_000:.1f}M')
        ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
        plt.xticks(rotation=45)
        return self.save_figure(fig, ax, "box_plot_confirmed_cases_by_region.png")

    def trend_line_confirmed_india_vs_another_chosen_country_side_by_side(self):
        """ Trend Line: Confirmed Cases in India vs Another Chosen Country Over Time """
        countries = ['India', 'Japan']
        columns = ['Country/Region', 'Confirmed']

        # Use the helper defined on the parent class correctly
        data_by_country = self.fetch_data_by_country_by_column(
            country_names=countries,
            column_names=columns,
            filter_by='Country/Region'
        )

        fig, ax = plt.subplots(figsize=(8, 5))
        ax.bar(data_by_country.index, data_by_country.values)
        ax.set_xlabel('Country')
        ax.set_ylabel('Confirmed')
        ax.set_title(f'Confirmed Cases: India vs {countries[1]}')
        ax.grid(True, axis='y', alpha=0.3)
        return self.save_figure(fig, ax, "trend_line_confirmed_india_vs_another_chosen_country.png")



    def main(self):
        """ Generate all required visualizations """

        output = {}

        output['bar_top10'] = self.bar_chart_top_10_countries_by_confirmed()
        output['pie_top_death_by_region'] = self.pie_chart_death_distribution_by_region()
        output['line_confirmed_vs_death_top5'] = self.line_chart_comapring_confirmed_death_top5()
        output['scatter_confirmed_vs_recovered'] = self.scatter_plot_confirmed_vs_recovered()
        output['histogram_mortality_rate'] = self.histogram_mortality_rate_distribution()
        output['stacked_bar_confirmed_death_recovered'] = self.stacked_bar_plot_confirmed_death_recovered__by_country()
        output['box_plot_confirmed_cases_by_region'] = self.box_plot_confirmed_cases_by_region()

        #output['trend_line_india_vs_another'] = self.trend_line_confirmed_india_vs_another_chosen_country_side_by_side()

        return output


if __name__ == "__main__":
    # Use the centralized resources folder for the COVID dataset
    file_path = Path(__file__).resolve().parents[2] / 'resources' / 'country_wise_latest.csv'
    if not file_path.exists():
        print(f"Covid 19 data file not found at {file_path}. Exiting.")
        raise SystemExit(1)

    covid_viz = CovidVisualization(file_path)
    charts_generated = covid_viz.main()
    # Print each key:value on separate lines using repr for Axes, with commas between entries
    items = list(charts_generated.items())
    for idx, (key, value) in enumerate(items):
        comma = "," if idx < len(items) - 1 else ""
        print(f"'{key}': {value!r}{comma}")
