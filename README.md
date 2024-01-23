# Walmart Proximity Analysis

This project explores the proximity of populations to Walmart locations, integrating geospatial data and statistical analysis.
=============================

## Introduction
- **Background**:
    - Walmart claims that over 90% of Americans live within 10 miles of a Walmart location.
- **Objectives**:
    - To analyze the correlation between Walmart proximity and factors such as median household income and (RUCA) rural-urban classifications.
    - Develop models to predict driving distances and driving times to Walmart locations.
- **Research Questions**:
    - Can we accurately predict driving time and distance to Walmarts for different populations?
    - How does the proximity of Walmarts vary with various economic predictor variables?


## Data 
- **Data Sources**:
    - Scraped Walmart location data from the Walmart [store locator webpage](https://www.walmart.com/store-finder)
    - Sourced zip code and RUCA classification from the USDA [RUCA Codes](https://www.ers.usda.gov/data-products/rural-urban-commuting-area-codes/)
    - Geospatial coordinates for Walmart stores and zip code areas were integrated for proximity analysis using the GeoPy library for python
- **Data Attributes**:
    - Analyzed attributes include zip code populations, median household incomes, and geospatial data for Walmarts and zip code areas.

## Methodology
- **Data Processing**:
    - Data from the sources were cleaned, merged, and transformed for analysis.
    - RUCA codes were encoded, and great circle distances were calculated for proximity analysis.
- **Geospatial Analysis**:
    - Utilized geospatial data to assess the proximity of populations to Walmart stores.
    - The general assumption is that great circle distance serves a generally strong predictor of actual driving distance/time distance.
    - Created visualizations to explore spatial relationships and distributions.
- **Statistical Analysis**:
    - Developed linear regression models to predict driving distances and times using great cirlce distance
    - Conducted correlation and descriptive analyses to understand pfdcitor impacts on Walmart accessibility.
- **User Interface**:
    - Leveraged Tableau for dynamic visualizations and interactive data exploration.

## Analysis
- **Descriptive Analysis**:
    - Examined demographic distributions and Walmart locations to identify trends and patterns.
- **Proximity Analysis**:
    - Analyzed the physical distance of populations to Walmart stores.
- **Correlation Analysis**:
    - Investigated the relationship between socio-economic factors and the number of Walmarts within a 10-mile radius.

## Results
- **Findings**:
    - Walmart's own research claims that 90% of Americans live within 10 miles of a Walmart store
    - My findings show that between 79% and 86% of Americans live within 10 miles of a Walmart store
    - According to the model
- **Visualizations**
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
