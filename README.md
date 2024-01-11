# Title
==============================

## Demo

## Introduction
- **Background**:
    - This project explores the proximity of populations to Walmart locations, integrating geospatial data and statistical analysis.
    - A comprehensive study on accessibility, socio-economic factors, and demographic analysis.
- **Objectives**:
    - To analyze the correlation between Walmart proximity and socio-economic factors like median household income and rural-urban classifications.
    - Develop models to predict driving distances and times to Walmart locations.
- **Research Questions**:
    - How does the proximity of Walmarts vary with socio-economic and demographic factors?
    - Can we accurately predict driving time and distance to Walmarts for different populations?

## Data 
- **Data Sources**:
    - Utilized datasets include Walmart locations, zip code demographics, and RUCA (Rural-Urban Commuting Area) classifications.
    - Geospatial coordinates for Walmart stores and zip code areas were integrated for proximity analysis.
- **Data Attributes**:
    - Analyzed attributes include zip code populations, median household incomes, and geospatial data for Walmarts and zip code areas.

## Methodology
- **Data Processing**:
    - Data from various sources were cleaned, merged, and transformed for analysis.
    - RUCA codes were encoded, and great circle distances were calculated for proximity analysis.
- **Geospatial Analysis**:
    - Utilized geospatial data to assess the proximity of populations to Walmart stores.
    - Created visualizations to explore spatial relationships and distributions.
- **Statistical Analysis**:
    - Developed linear regression models to predict driving distances and times.
    - Conducted correlation and descriptive analyses to understand socio-economic impacts on Walmart accessibility.
- **User Interface**:
    - Leveraged Tableau for dynamic visualizations and interactive data exploration.

## Analysis
- **Descriptive Analysis**:
    - Examined demographic distributions and Walmart locations to identify trends and patterns.
- **Proximity Analysis**:
    - Analyzed the physical distance of populations to Walmart stores.
    - Highlighted areas with limited accessibility.
- **Correlation Analysis**:
    - Investigated the relationship between socio-economic factors and the number of Walmarts within a 10-mile radius.

## Results
- **Findings**:
    - Identified key socio-economic factors influencing Walmart accessibility.
    - Determined areas with high and low Walmart accessibility.
- **Visualizations**:
    - Created comprehensive charts and maps to illustrate findings and support insights.

## Discussion
- **Interpretation**:
    - Discussed the implications of Walmart accessibility on various communities.
    - Highlighted the importance of location in retail strategies.
- **Limitations**:
    - Acknowledged data limitations and potential biases.
    - Addressed the constraints of the predictive models used.
- **Future Work**:
    - Proposed further studies with additional variables and refined models.
    - Recommended exploring other retail chains for comparative analysis.

## Appendix
- **Technical Details**:
    - Detailed the methodologies and tools used in data processing and analysis.
- **References**:
    - Cited all data sources, research papers, and other materials referenced in the project.

## Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data
