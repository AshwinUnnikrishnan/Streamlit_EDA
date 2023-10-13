# Streamlit_EDA

Problem Statement : It is very tedious process to check each dataset for missing values and perform an initial exploratory data analysis, and generate a baseline model.

Solution : Created an AUTOML website, that is a one place solution.

How it works :

            1. Upload the csv file that you have to work with which contains the Independent variables and dependent variable.
            2. In the next section we can visualize the data, and drop columns if needed. And then once perform EDA is clicked 
               it provides the results from pandas_profiling
                1. Overview:
                    - Number of variables
                    - Number of observations
                    - Total missing cells
                    - Missing cells per variable
                    - Duplicate rows
                    - Duplicate rows per variable
                2. Variables:
                    - Variable type (categorical, numerical, date, etc.)
                    - Distinct count
                    - Missing values
                    - Count of unique values
                    - Most frequent values
                    - Frequency of the most frequent value
                    - Histogram for numerical variables
                    - Common values for categorical variables
                3. Quantiles, Deciles, and Percentiles:
                    - Summary statistics including mean, median, and standard deviation
                4. Correlations:
                    - Correlation matrix for numerical variables
                    - Heatmap of the correlation matrix
                5. Sample:
                    - A sample of rows from the dataset
                6. Missing Values:
                    - Matrix of missing values
                7. Text Analysis:
                    - Word cloud for text columns
                    - Character and word distribution for text columns
                8. Interactions:
                    - Scatterplot matrix for numerical variables
                    - Correlation plot
                9. File and Data Information:
                    - File information (size, creation date)
                    - Data information (number of variables, observations, memory usage)
                10. Warnings:
                    - A section for warnings, such as high cardinality, constant variables, etc.
            3. In Modelling page the columns are show that do not have missing values, from these you can choose target       
                variable.
            4. The best model can be downloade.


site : https://eda-data-9d79aa8caa61.herokuapp.com/
