import streamlit as st
import pandas as pd
import plotly.express as px
import json

# Page setup
st.set_page_config(layout="wide")
st.title("🌾 Rainfall Deviation & Crop Yield Analysis Dashboard")
st.markdown("Compare how rainfall deviation impacts crop yields across multiple states and crops.")

# Load merged data
@st.cache_data
def load_data():
    return pd.read_csv("./data/cleaned/merged_dataset.csv")

df = load_data()

# Load GeoJSON
@st.cache_data
def load_geojson():
    with open("./data/india_district.geojson", "r", encoding="utf-8") as f:
        geojson = json.load(f)
    return geojson

geojson = load_geojson()

# Fix GeoJSON 'id' field using NAME_2
for feature in geojson['features']:
    feature['id'] = feature['properties']['NAME_2'].strip().lower()

# Sidebar: View selector
st.sidebar.header("Dashboard Controls")
view_type = st.sidebar.radio("Select View", ["Scatter: Yield vs Rainfall", "District Map"])

# Common filters
crop_list = [col.replace('_yield_(kg_per_ha)', '') for col in df.columns if '_yield_(kg_per_ha)' in col]
crops_selected = st.sidebar.multiselect("Select Crop(s)", crop_list, default=[crop_list[0]])

states = sorted(df['state_name'].dropna().unique())
states_selected = st.sidebar.multiselect("Select State(s)", states, default=[states[0]])

years = sorted(df['year'].dropna().unique())

# === SCATTER VIEW ===
if view_type == "Scatter: Yield vs Rainfall":
    year_range = st.sidebar.slider("Select Year Range", int(min(years)), int(max(years)), (2000, 2015))
    show_trendline = st.sidebar.checkbox("Show Trendline", value=True)

    yield_cols = [f"{c}_yield_(kg_per_ha)" for c in crops_selected]

    filtered_df = df[
        (df['state_name'].isin(states_selected)) &
        (df['year'].between(year_range[0], year_range[1]))
    ].copy()

    # Melt for long form
    filtered_long = filtered_df[['state_name', 'dist_name', 'year', 'rainfall_deviation'] + yield_cols].melt(
        id_vars=['state_name', 'dist_name', 'year', 'rainfall_deviation'],
        var_name='crop',
        value_name='yield_kg_per_ha'
    )
    filtered_long['crop'] = filtered_long['crop'].str.replace('_yield_\(kg_per_ha\)', '', regex=True)
    filtered_long = filtered_long.dropna(subset=['yield_kg_per_ha'])

    # Plot
    st.subheader(f"Yield vs Rainfall Deviation in Selected States ({year_range[0]}–{year_range[1]})")
    fig = px.scatter(
        filtered_long,
        x='rainfall_deviation',
        y='yield_kg_per_ha',
        color='crop',
        animation_frame='year',
        facet_col='state_name',
        labels={
            'rainfall_deviation': 'Rainfall Deviation (%)',
            'yield_kg_per_ha': 'Yield (kg/ha)',
            'state_name': 'State'
        },
        height=650
    )
    if show_trendline:
        fig.update_traces(marker=dict(opacity=0.6))

    st.plotly_chart(fig, use_container_width=True)

    # Summary stats
    st.markdown("Summary Statistics")
    summary = filtered_long.groupby(['crop', 'state_name'])[['yield_kg_per_ha', 'rainfall_deviation']].mean().round(2).reset_index()
    st.dataframe(summary, use_container_width=True)

# === MAP VIEW ===
else:
    year = st.sidebar.selectbox("Select Year", years)
    map_type = st.sidebar.radio("Map Data", ["Rainfall Deviation", "Crop Yield"])

    for state in states_selected:
        st.subheader(f"{map_type} in {state} ({year})")
        filtered_map_df = df[(df['state_name'] == state) & (df['year'] == year)].copy()
        filtered_map_df['dist_name_normalized'] = filtered_map_df['dist_name'].str.strip().str.lower()

        for crop in crops_selected:
            yield_col = f"{crop}_yield_(kg_per_ha)"
            color_col = 'rainfall_deviation' if map_type == "Rainfall Deviation" else yield_col
            color_title = "Rainfall Deviation (%)" if map_type == "Rainfall Deviation" else f"{crop.capitalize()} Yield (kg/ha)"

            if not filtered_map_df.empty:
                fig = px.choropleth(
                    filtered_map_df,
                    geojson=geojson,
                    locations="dist_name_normalized",
                    featureidkey="id",
                    color=color_col,
                    hover_name="dist_name",
                    projection="mercator",
                    height=650,
                    title=f"{color_title} - {crop.capitalize()} in {state} ({year})",
                    color_continuous_scale="YlGnBu"
                )
                fig.update_geos(fitbounds="locations", visible=False)
                st.plotly_chart(fig, use_container_width=True)
            else:
                st.warning(f"No map data for {crop} in {state}.")

# Footer
st.markdown("---")
st.markdown("Built with using Streamlit & Plotly | © Kirankumar Malothu")
