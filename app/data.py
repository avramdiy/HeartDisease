from flask import Flask, render_template
import pandas as pd
import pandasql
import plotly.express as px
import plotly.io as pio
import json

app = Flask(__name__, template_folder=r"C:\\Users\\Ev\\Desktop\\HeartDisease\\templates")

# Specify the file path
file_path = r"C:\\Users\\Ev\\Desktop\\HeartDisease\\heart_disease.csv"

# Load the CSV file into a pandas DataFrame
df = pd.read_csv(file_path)

# Use pandasql to run an SQL query on the DataFrame
query = """
SELECT * 
FROM df
WHERE "Age" > 50
"""
filtered_df = pandasql.sqldf(query, locals())

# Create a Plotly figure
def create_plot(dataframe):
    fig = px.bar(dataframe, x="Age", y="Cholesterol Level", color="Gender", title="Cholesterol Levels by Age (Age > 50)")
    return fig.to_json()

@app.route("/")
def home():
    # Generate the visualization
    plot = create_plot(filtered_df)
    return render_template("index.html", plot=plot)

if __name__ == "__main__":
    app.run(debug=True)