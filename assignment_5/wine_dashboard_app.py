# ==========================================
# Wine Dataset Dashboard App
# Student Name: Amar Kumar
# Student ID: MA24M002
# ==========================================

# --- Part 1: Setup and Basic Structure ---
# TODO: Import necessary libraries (5 Marks - for ensuring all needed imports are present)
import importlib
import subprocess
import sys

def import_or_install(package_name, import_name=None):
    try:
        return importlib.import_module(import_name or package_name)
    except ModuleNotFoundError:
        print(f" '{package_name}' not found. Installing...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])
        return importlib.import_module(import_name or package_name)

# --- Imports ---
st = import_or_install("streamlit")
pd = import_or_install("pandas")
np = import_or_install("numpy")
px = import_or_install("plotly.express", "plotly.express")
sklearn_datasets = import_or_install("scikit-learn", "sklearn.datasets")
sklearn_tree = import_or_install("scikit-learn", "sklearn.tree")
import plotly.express as px
from sklearn.datasets import load_wine
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split



# TODO: Add a title for the Streamlit app (Included in 10 Marks for Framework)
st.title("Wine Dataset Interactive Dashboard")

# TODO: Add introductory text (Included in 10 Marks for Framework)
st.markdown("""
Welcome to the interactive dashboard built with **Streamlit** and **Plotly**!
Explore the wine dataset, visualize patterns between features, and try out a simple machine learning model to classify wine types based on chemical characteristics.
""")


# --- Part 2: Data Loading, Validation, and Display (20 Marks) ---

# TODO: Load the wine dataset into a DataFrame 'df_wine' (5 Marks)
#       Combine data and target, using feature_names for columns and adding a 'target' column.
wine = load_wine()
df_wine = pd.DataFrame(data=wine.data, columns=wine.feature_names)
df_wine["target"] = wine.target
# Map target numbers to class names for better readability
df_wine["target_name"] = df_wine["target"].apply(lambda x: wine.target_names[x])


# Data Overview
st.subheader("Dataset Preview")
st.write(df_wine.head())

# Missing Values Check
st.subheader("Missing Values")
st.write(df_wine.isnull().sum())

# Summary Stats
st.subheader("Summary Statistics")
st.write(df_wine.describe())

# --- Part 3: Interactive Visualization with Plotly (30 Marks) ---
st.sidebar.header("Filter Options")
selected_classes = st.sidebar.multiselect(
    "Select wine class(es) to display:",
    options=wine.target_names,
    default=list(wine.target_names)
)

filtered_df = df_wine[df_wine["target_name"].isin(selected_classes)]

# Scatter plot
st.subheader("Scatter Plot of Two Features")
x_axis = st.selectbox("Select X-axis:", wine.feature_names, index=0)
y_axis = st.selectbox("Select Y-axis:", wine.feature_names, index=1)

fig = px.scatter(
    filtered_df,
    x=x_axis,
    y=y_axis,
    color="target_name",
    title=f"{x_axis} vs {y_axis}",
    labels={"target_name": "Wine Class"}
)
st.plotly_chart(fig)

# --- Part 4: Integrating a Simple Predictive Model (25 Marks) ---
# Features and labels
X = df_wine[wine.feature_names]
y = df_wine["target"]

# Train model
model = DecisionTreeClassifier()
model.fit(X, y)

st.sidebar.header("Predict Wine Class")

# Select two key features for input (e.g., 'alcohol' and 'malic_acid')
input_alcohol = st.sidebar.slider(
    "Alcohol", float(X["alcohol"].min()), float(X["alcohol"].max()), float(X["alcohol"].mean())
)
input_malic = st.sidebar.slider(
    "Malic Acid", float(X["malic_acid"].min()), float(X["malic_acid"].max()), float(X["malic_acid"].mean())
)

# Create prediction input
input_features = X.mean().to_dict()
input_features["alcohol"] = input_alcohol
input_features["malic_acid"] = input_malic

input_df = pd.DataFrame([input_features])[X.columns]  # Ensure order

# Predict
prediction = model.predict(input_df)[0]
predicted_class = wine.target_names[prediction]

# Display prediction
st.subheader("Prediction Based on Sidebar Inputs")
st.write(f"**Input Values:** Alcohol = {input_alcohol}, Malic Acid = {input_malic}")
st.write(f"**Predicted Wine Class:** {predicted_class}")

# --- Part 5: Code Quality and App Presentation (10 Marks) ---
# Clear structure, inline comments, and intuitive layout above.
