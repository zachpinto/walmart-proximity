.. _eda:

Exploratory Data Analysis (EDA)
===============================

The EDA phase of the project involved a series of Jupyter notebooks that facilitated the exploration and understanding of the processed dataframes, relationships between variables, and the distribution of various features within the data.

10_eda
------

- Explored processed dataframes.
- Created a feature representing the number of people per Walmart store.
- Investigated the relationship between the number of people per Walmart store and the state.
- Analyzed the distribution of Walmart store openings by year and cumulative openings over time.
- Examined the distribution of median household incomes.
- Explored the distribution of median household incomes by state.
- Determined the number of ZIP codes by RUCA classification.
- Visualized state-wise population distribution by RUCA classification.

11_eda
------

- Calculated the sample size needed for a 95% confidence interval and a margin of error of 5%, which was determined to be 380. However, the final sample size was slightly lower due to NaN values encountered during sampling.

12_eda
------

- Integrated with the GEOCODIO API to geocode Walmart addresses and ZIP codes.

13_eda
------

- Calculated the total number of elements required for GEOCODIO API calls and the associated cost. The total elements amounted to 4,057, leading to a cost of $8.

14_eda
------

- Connected to the Distance Matrix API to obtain real driving time distances between Walmart stores and ZIP codes within the same state for the sampled data.
- Compiled the results into a new sample called `distance_sample`.

15_eda
------

- Utilized the `geopy` library to calculate the great circle distance between the geocoded pairs of Walmart stores and ZIP codes.
- Appended the great circle distance data to the `distance_sample`.

Each notebook contributed to building a comprehensive understanding of the dataset, which was critical for the feature engineering and modeling phases. The EDA stage provided valuable insights into the data, informing the direction and scope of subsequent analyses.

.. note:: The documents and visualizations created during the EDA phase are available in the respective notebooks and can be accessed for a detailed view of the exploratory process and findings.
