Feature Engineering
===================

The feature engineering process involved developing a preliminary model to estimate driving times based on great circle distances and RUCA classifications. The model's R-squared and cross-validation scores were as follows:

.. code-block:: python

    R-squared: 0.9745
    Cross-validated R-squared scores: [0.9623, 0.9480, 0.9419, 0.9712, 0.9785]

The model was applied to the entire dataset to generate a new feature 'estimated_driving_time', which will be used in subsequent analyses.

For more details on the modeling process, refer to the notebook located at `/notebooks/20_feature.ipynb`.

Outlier Treatment
-----------------

During the exploratory data analysis, outliers with a great circle distance greater than 1250 and a driving time less than 500 were identified and removed. This treatment improved the model's performance significantly.

.. note:: Outlier removal was based on domain knowledge and exploratory analysis, ensuring that only erroneous data points were excluded.
