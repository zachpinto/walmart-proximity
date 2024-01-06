.. _preprocessing:

Data Preprocessing
==================

The Data Preprocessing phase is crucial for preparing the raw data into a format suitable for exploratory data analysis and modeling. This phase includes handling missing values, extracting and scraping necessary data, and profiling datasets to understand their structure and content.

External Data
-------------

- **`data/external/zips.csv`**:
  - This externally downloaded file contains information about ZIP codes, including RUCA classification, city, state name, population, county, and median household income.

Missing Values Imputation
-------------------------

- **`src/data/impute_missing_values.py`**:
  - A script designed to impute missing values in the `zips.csv` file. Ensures the completeness of the dataset for further analysis.

Walmart Locations Data Collection
---------------------------------

- **`src/data/walmart_locations_scraper.py`**:
  - A web scraping script that gathers Walmart store locations, city, and designation by state from the Walmart store locator, creating a raw text file.

- **`src/data/process_walmart_locations.py`**:
  - Processes the raw Walmart text file into a structured dataset with the format: Address, Designation, Store #, Open Date.

Profiling Datasets
------------------

- **`00_preprocessing`**:
  - Profiles each processed dataset using `pandas-profiling` or `ydata-profiling` to generate reports that offer an overview of the data, including distributions, missing values, and potential correlations.

Address Formatting
------------------

- **`01_preprocessing`**:
  - Combines various address-related columns into a single `Address` column for the Walmart dataset, ensuring a consistent format for geocoding purposes.

The preprocessing steps taken have laid a solid foundation for the data to be reliably used in subsequent stages of analysis. Each script and process is crafted to ensure that the data is accurate, consistent, and ready for the exploratory data analysis and modeling phases of the project.

.. note:: Detailed reports generated during the profiling of datasets are stored and can be referenced for a deeper understanding of the data characteristics.

