# AI Engineer Exercise

A comprehensive Python-based data analysis and visualization project focused on COVID-19 data analysis, demonstrating core data science workflows including ETL, statistical analysis, exploratory data analysis (EDA), and data visualization.

## 🎯 Project Overview

This project showcases end-to-end data analysis capabilities using real-world COVID-19 datasets, implementing professional data science practices and reusable code architecture.

## 🚀 Key Functionalities

### **1. Data Processing & Analysis**
- **CSV Data Handling**: Robust CSV reading, writing, and transformation capabilities
- **Data Cleaning**: Handling missing values, data type conversions, and data validation
- **Statistical Analysis**: Computation of mean, median, variance, standard deviation, and correlation matrices
- **Data Aggregation**: Grouping and summarizing data by regions and countries

### **2. Data Quality & Preprocessing**
- **Outlier Detection**: IQR (Interquartile Range) method for identifying and removing outliers
- **Data Normalization**: StandardScaler implementation for feature scaling (mean=0, std=1)
- **Data Filtering**: Dynamic column selection and data subsetting
- **Index Management**: Sequential index resetting after data transformations

### **3. Data Visualization**
- **Statistical Plots**: 
  - Histograms with KDE (Kernel Density Estimation) curves
  - Box plots for distribution analysis
  - Scatter plots for correlation analysis
- **Comparative Visualizations**:
  - Bar charts (top countries by metrics)
  - Line charts (trend comparisons)
  - Stacked bar charts (multi-metric analysis)
  - Pie charts (distribution by regions)
- **Correlation Analysis**:
  - Heatmaps for correlation matrices
  - Before/after normalization comparisons

### **4. Exploratory Data Analysis (EDA)**
- Comprehensive statistical summaries
- Distribution analysis (before and after normalization)
- Correlation studies between variables
- Visual representation of data patterns
- Bell curve visualization with normalization

### **5. Code Architecture**
- **Reusable Modules**: Organized package structure (`python_script`)
- **Object-Oriented Design**: Class-based implementation with inheritance
- **Dynamic Path Management**: Automatic directory detection for outputs
- **Error Handling**: Robust validation and error messages
- **Type Hints**: Modern Python typing for better code clarity

## 📊 Data Pipeline

```
Raw Data (CSV) → Data Loading → Cleaning & Validation → Statistical Analysis
                                                       ↓
                                    ← Visualization ← Normalization ← Outlier Removal
```

## 🛠️ Technical Stack

- **Python 3.12+/3.14+**
- **pandas**: Data manipulation and analysis
- **numpy**: Numerical computations
- **matplotlib**: Base plotting library
- **seaborn**: Statistical data visualization
- **scikit-learn**: Machine learning preprocessing (StandardScaler)

## 📁 Project Structure

```
ai-engineer-exercise/
├── python_script/          # Reusable analysis modules
│   ├── covid_analysis/     # Core data analysis classes
│   └── plot_images.py      # Dynamic plotting utilities
├── resources/              # Centralized data storage
├── week*-assignment/       # Weekly assignments with outputs
│   ├── python/            # Analysis scripts
│   ├── plot_images/       # Generated visualizations
│   └── assignment/        # Output CSV files
└── requirements.txt        # Python dependencies
```

## 🔧 Quick Setup

```bash
# Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install project in editable mode
pip install -e .
```

## ▶️ Usage Examples

```bash
# Run COVID-19 data analysis
python week4-assignment/python/CoronaDataAnalysis.py

# Generate visualizations
python week5-assignment/python/DataVisualisationAndEDA.py

# Perform EDA with normalization
python week6-assignment/python/CovidEDA.py
```

## 📈 Output Examples

- **CSV Files**: Cleaned and sorted datasets
- **Visualizations**: High-resolution PNG images (200 DPI)
- **Statistical Reports**: Console output with formatted metrics

## 🧹 Maintenance

```bash
# Clean Python cache files
make clean-pyc

# Remove generated images
rm -rf week*/plot_images/
```

## 📝 Key Features

- ✅ Modular and reusable code architecture
- ✅ Dynamic path resolution for cross-platform compatibility
- ✅ Comprehensive error handling and validation
- ✅ Professional visualization with customizable styling
- ✅ Efficient data processing with pandas
- ✅ Statistical rigor with proper normalization techniques
- ✅ Clean separation of concerns (ETL, Analysis, Visualization)

## 🔍 Troubleshooting

- **ModuleNotFoundError**: Ensure virtual environment is active and run `pip install -e .`
- **Data not found**: Verify `resources/country_wise_latest.csv` exists
- **Import errors**: Check that `python_script` package is properly installed

## 📚 Dependencies

See `requirements.txt` for complete list:
- numpy==2.3.3
- pandas==2.3.2
- matplotlib==3.10.6
- seaborn==0.13.2
- scikit-learn==1.6.1

---

**Note**: This project demonstrates professional data science workflows suitable for real-world COVID-19 data analysis and can be extended for other datasets with similar structure.
