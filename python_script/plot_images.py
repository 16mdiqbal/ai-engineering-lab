from pathlib import Path
import inspect

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


class PlotImages:
    def __init__(self, figure_dir: str | Path | None = None):
        if figure_dir is None:
            # Dynamically determine the calling file's directory
            # Get the caller's frame (the file that instantiated this class)
            caller_frame = inspect.stack()[1]
            caller_file = Path(caller_frame.filename).resolve()

            # Go up to the assignment folder (e.g., week5-assignment, week6-assignment)
            assignment_folder = caller_file.parents[1]

            # Create plot_images directory in the assignment folder
            figure_dir = assignment_folder / 'plot_images'

        self.figure_dir = Path(figure_dir)
        self.figure_dir.mkdir(parents=True, exist_ok=True)


    def plot_histogram(self, df: pd.DataFrame, columns: str|list, bins: int = 30, kde: bool = True, figsize: tuple = (12, 5)):
        """ Plot histograms for specified column(s) side by side using seaborn

        Args:
            df: Input DataFrame
            columns: Single column name (str) or list of column names to plot
            bins: Number of bins for histogram (default: 30)
            kde: Whether to show KDE curve (default: True)
            figsize: Figure size as (width, height) tuple

        Returns:
            matplotlib figure object
        """
        if isinstance(columns, str):
            columns = [columns]
        elif not isinstance(columns, list):
            raise TypeError("Parameter 'columns' must be a string or a list of strings.")

        missing_columns = [col for col in columns if col not in df.columns]
        if missing_columns:
            raise ValueError(f"Columns not found in the DataFrame: {missing_columns}")

        # Calculate number of columns for subplot layout
        n_cols = len(columns)

        # Dynamic colors for each histogram
        colors = ['orange', 'violet', 'skyblue', 'lightgreen', 'salmon', 'gold', 'pink', 'cyan']

        # Create figure with dynamic subplot layout
        fig, axes = plt.subplots(1, n_cols, figsize=figsize)

        # Handle single column case (axes is not an array)
        if n_cols == 1:
            axes = [axes]

        # Plot histogram for each column using seaborn
        for idx, column in enumerate(columns):
            ax = axes[idx]
            color = colors[idx % len(colors)]  # Cycle through colors if more columns than colors

            # Use seaborn's histplot for better styling
            sns.histplot(
                data=df,
                x=column,
                bins=bins,
                kde=kde,
                color=color,
                ax=ax,
                edgecolor='black',
                alpha=0.7
            )

            # Set title and labels
            ax.set_title(f'Histogram of {column}')
            ax.set_xlabel(column)
            ax.set_ylabel('Frequency')
            ax.grid(True, alpha=0.3)

        plt.tight_layout()
        return fig

    def plot_heatmap(self, df: pd.DataFrame, figsize: tuple = (8, 6), annot: bool = True, cmap: str = 'coolwarm'):
        """ Plot a correlation heatmap for the DataFrame using seaborn

        Args:
            df: Input DataFrame
            figsize: Figure size as (width, height) tuple
            annot: Whether to annotate cells with correlation values (default: True)
            cmap: Color map to use (default: 'coolwarm')

        Returns:
            matplotlib figure object
        """
        # Calculate correlation matrix
        corr_matrix = df.corr()

        # Create figure
        fig, ax = plt.subplots(figsize=figsize)

        # Plot heatmap using seaborn
        sns.heatmap(
            corr_matrix,
            annot=annot,
            fmt='.2f',
            cmap=cmap,
            center=0,
            square=True,
            linewidths=1,
            cbar_kws={'shrink': 0.8},
            ax=ax
        )

        # Set title
        ax.set_title('Correlation Heatmap', fontsize=14, fontweight='bold', pad=20)

        plt.tight_layout()
        return fig

    def plot_scatter(self, df: pd.DataFrame, x: str, y: str, hue: str | None = None, size: str | None = None, figsize: tuple = (8, 6), alpha: float = 0.8, palette: str | list | dict = 'deep'):
        """ Plot a scatter plot between two columns with optional hue and size.

        Args:
            df: Input DataFrame
            x: Column name for x-axis
            y: Column name for y-axis
            hue: Optional column name to use for color encoding
            size: Optional column name to use for point size encoding
            figsize: Figure size as (width, height) tuple
            alpha: Marker transparency (default: 0.8)
            palette: Color palette for hue (default: 'deep')

        Returns:
            matplotlib figure object
        """
        # Validate column arguments
        if not isinstance(x, str) or not isinstance(y, str):
            raise TypeError("Parameters 'x' and 'y' must be column name strings.")

        missing = [col for col in (x, y) if col not in df.columns]
        if missing:
            raise ValueError(f"Columns not found in the DataFrame: {missing}")

        if hue is not None and hue not in df.columns:
            raise ValueError(f"Hue column not found in the DataFrame: {hue}")

        if size is not None and size not in df.columns:
            raise ValueError(f"Size column not found in the DataFrame: {size}")

        # Create figure and axis
        fig, ax = plt.subplots(figsize=figsize)

        # Use seaborn scatterplot for styling
        # Build kwargs conditionally to avoid passing unused palette when hue is None
        scatter_kwargs = dict(
            data=df,
            x=x,
            y=y,
            alpha=alpha,
            ax=ax,
            edgecolor='w',
            linewidth=0.5,
        )

        if hue is not None:
            scatter_kwargs['hue'] = hue
            scatter_kwargs['palette'] = palette

        if size is not None:
            scatter_kwargs['size'] = size

        sns.scatterplot(**scatter_kwargs)

        # Set title and labels
        title_parts = [f'Scatter plot of {y} vs {x}']
        if hue:
            title_parts.append(f'colored by {hue}')
        if size:
            title_parts.append(f'sized by {size}')
        ax.set_title(' — '.join(title_parts), fontsize=14, fontweight='bold')
        ax.set_xlabel(x)
        ax.set_ylabel(y)

        # Improve layout and grid
        ax.grid(True, alpha=0.3)
        plt.tight_layout()
        return fig

    def save_figure(self, fig, ax, file_name: str = "covid_analysis.png"):
        """ Save the current matplotlib figure to the figure directory """
        figure_path = self.figure_dir / file_name
        fig.tight_layout()
        plt.savefig(figure_path, dpi=200, bbox_inches='tight')
        print(f"Figure saved to {figure_path.resolve()}")
        return ax

