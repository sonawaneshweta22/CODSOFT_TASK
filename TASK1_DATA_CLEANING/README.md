# CODSOFT Task 1 - Data Cleaning & Preprocessing

## Project Overview

This project is part of the CODSOFT Data Analytics Internship.

The objective of Task 1 is to clean and preprocess a dataset using Python and Pandas. The dataset was inspected for missing values, duplicate records, inconsistent entries, and incorrect data types.

## Technologies Used

- Python
- Pandas
- CSV

## Files

- `task1_data_cleaning.py` - Python program used for data cleaning and preprocessing.
- `dataset.csv` - Original dataset containing unclean data.
- `cleaned_dataset.csv` - Final cleaned dataset.
- `README.md` - Project documentation.

## Data Cleaning Steps

The following steps were performed:

1. Imported the dataset using Pandas.
2. Inspected the dataset structure using `info()` and `shape`.
3. Identified missing values.
4. Identified duplicate records.
5. Removed duplicate records.
6. Corrected inconsistent entries such as `male` to `Male` and `pune` to `Pune`.
7. Converted Age and Marks into numeric data types.
8. Handled missing Age using the median.
9. Handled missing Marks using the mean.
10. Rounded Marks to two decimal places.
11. Saved the cleaned dataset as `cleaned_dataset.csv`.

## Dataset Summary

- Original records: 15
- Records after removing duplicates: 14
- Number of columns: 6
- Missing values after cleaning: 0
- Duplicate records after cleaning: 0

## Result

The dataset was successfully cleaned and prepared for further analysis using Pandas.
