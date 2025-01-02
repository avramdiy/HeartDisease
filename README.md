# Week 5 Data Analysis / Machine Learning Practice Focused Towards Heart Disease

## Dataset Source

- https://www.kaggle.com/datasets/oktayrdeki/heart-disease

## 1st Commit

- Loaded the heart_disease.csv file from the specified path into a pandas DataFrame.

- Used pandasql to filter data with a query that selects rows where Age is greater than 50.

- Configured a Flask app with a custom template folder, created a Plotly bar chart for Age vs. Cholesterol Level, and passed the chart data to an HTML template for rendering.

## 2nd Commit

- Modified the "/" route & index.html to display a 5 row header to understand all features in the CSV file.

- Adjusted the query to pull results that said "Yes"  to Smoking and "Yes" to High Blood Pressure.

- Loaded the blood pressure, aggregated by Age, for female & male results by separate line charts, within the same visualization.

## 3rd Commit

- Adjusted data.py to show the aggregated average blood pressure by age, through two new line plots for Male and Female respectively.

## 4th Commit

- Added new route to query and visualize a difference of BMI for High Blood Pressure AND Smoking "YES" results.

- Aggregated query data by Age & Gender.

- Created a separate line chart and separate .html file for visualization.

## 5th Commit