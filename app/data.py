from flask import Flask, render_template
import pandas as pd
import plotly.express as px
import json

app = Flask(__name__, template_folder=r"C:\\Users\\Ev\\Desktop\\HeartDisease\\templates")

# Load your DataFrame
file_path = r"C:\\Users\\Ev\\Desktop\\HeartDisease\\heart_disease.csv"
df = pd.read_csv(file_path)

# Query using pandas instead of pandasql
# Filter for smokers with high blood pressure
filtered_df_smokers_high_bp = df[(df["Smoking"] == "Yes") & (df["High Blood Pressure"] == "Yes")]

# Aggregate the data by 'Age' and 'Gender' to avoid clutter
aggregated_df = filtered_df_smokers_high_bp.groupby(['Age', 'Gender'], as_index=False).agg({'Blood Pressure': 'mean'})

# Calculate the overall average blood pressure by age (across genders)
avg_bp_by_age = filtered_df_smokers_high_bp.groupby('Age', as_index=False).agg({'Blood Pressure': 'mean'})

# Create Plotly figure function with markers and aggregated data
def create_plot(dataframe, avg_data, title, x_col, y_col):
    fig = px.line(dataframe, x=x_col, y=y_col, color="Gender", markers=True, title=title)

    # Add average blood pressure by age for Male
    fig.add_scatter(x=avg_data['Age'], y=avg_data['Blood Pressure'], mode='lines', name='Average BP by Age (All)', line=dict(color='blue'))

    # Add average blood pressure by age for Female
    fig.add_scatter(x=avg_data['Age'], y=avg_data['Blood Pressure'], mode='lines', name='Average BP by Age (Female)', line=dict(color='red'))
    return fig.to_json()

# Flask route
@app.route("/")
def home():
    # Create plots for each query
    plot1 = create_plot(aggregated_df, avg_bp_by_age, "Blood Pressure by Age (Smokers with High Blood Pressure)", "Age", "Blood Pressure")
    
    # Get the first 5 rows of the filtered DataFrame for preview
    preview_df_smokers_high_bp = filtered_df_smokers_high_bp.head()
    preview_html_smokers_high_bp = preview_df_smokers_high_bp.to_html(classes='table table-striped')

    # Render the template with the plot and preview data
    return render_template("index.html", plot1=plot1, preview_html_smokers_high_bp=preview_html_smokers_high_bp)

@app.route("/bmi_by_age")
def bmi_by_age():
    # Filter data for smokers with high blood pressure
    filtered_df_bmi = df[(df["Smoking"] == "Yes") & (df["High Blood Pressure"] == "Yes")]
    
    # Aggregate the data by Age and Gender to calculate the average BMI
    aggregated_bmi_df = filtered_df_bmi.groupby(['Age', 'Gender'], as_index=False).agg({'BMI': 'mean'})
    
    # Create the line chart
    bmi_plot = px.line(aggregated_bmi_df, x="Age", y="BMI", color="Gender", markers=True, title="Average BMI by Age (Smokers with High Blood Pressure)")

    # Convert the Plotly figure to JSON for rendering in HTML
    bmi_plot_json = bmi_plot.to_json()

    # Get the first 5 rows of the filtered DataFrame for preview
    preview_df_bmi = filtered_df_bmi.head()
    preview_html_bmi = preview_df_bmi.to_html(classes='table table-striped')

    # Render the template with the plot and preview data
    return render_template("bmi_by_age.html", bmi_plot_json=bmi_plot_json, preview_html_bmi=preview_html_bmi)

if __name__ == "__main__":
    app.run(debug=True)
