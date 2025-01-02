from flask import Flask, render_template
import pandas as pd
import pandasql
import plotly.express as px
import plotly.io as pio
import json

app = Flask(__name__, template_folder=r"C:\\Users\\Ev\\Desktop\\HeartDisease\\templates")

# Load your DataFrame
file_path = r"C:\\Users\\Ev\\Desktop\\HeartDisease\\heart_disease.csv"
df = pd.read_csv(file_path)

# Example SQL query to filter for smokers with high blood pressure
query = """
SELECT * 
FROM df
WHERE "Smoking" = 'Yes' AND "High Blood Pressure" = 'Yes'
"""

# Execute the query on the DataFrame
filtered_df_smokers_high_bp = pandasql.sqldf(query, locals())

# Execute the query on the DataFrame
filtered_df_smokers_high_bp = pandasql.sqldf(query, locals())

# Aggregate the data by 'Age' and 'Gender' to avoid clutter
aggregated_df = filtered_df_smokers_high_bp.groupby(['Age', 'Gender'], as_index=False).agg({'Blood Pressure': 'mean'})

# Create Plotly figure function with markers and aggregated data
def create_plot(dataframe, title, x_col, y_col):
    fig = px.line(dataframe, x=x_col, y=y_col, color="Gender", markers=True, title=title)
    return fig.to_json()

# Flask route
@app.route("/")
def home():
    # Create plots for each query
    plot1 = create_plot(aggregated_df, "Blood Pressure by Age (Smokers with High Blood Pressure)", "Age", "Blood Pressure")
    
    # Get the first 5 rows of the filtered DataFrame for preview
    preview_df_smokers_high_bp = filtered_df_smokers_high_bp.head()
    preview_html_smokers_high_bp = preview_df_smokers_high_bp.to_html(classes='table table-striped')

    # Render the template with the plot and preview data
    return render_template("index.html", plot1=plot1, preview_html_smokers_high_bp=preview_html_smokers_high_bp)

if __name__ == "__main__":
    app.run(debug=True)