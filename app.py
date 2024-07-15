import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
st.set_page_config(page_title="Plotly Projet", layout="wide")
@st.cache_data
def load_data():
    cont = pd.read_csv('resources/cont.csv')
    prosperty_index = pd.read_csv("resources/data.csv")
    lo = pd.read_csv("resources/latlong.csv")
    prosperty_index['Country'] = prosperty_index['Country'].str.strip()
    cont['country'] = cont['country'].str.strip()
    lo['country'] = lo['country'].str.strip()
    df = prosperty_index.merge(cont, left_on="Country", right_on="country", how="inner").merge(lo, left_on="Country",right_on="country",how="inner")
    col = ['Country', 'continent_y', 'AveragScore', 'SafetySecurity',
           'Governance', 'SocialCapital', 'InvestmentEnvironment', 'EconomicQuality',
           'LivingConditions', 'Health', 'Education', 'NaturalEnvironment', '2023 population',
           'world percentage', 'area (km²)', 'growth rate', 'latitude', 'longitude', 'rural_population',
           'urban_population']
    df = df[col]
    df.rename(columns={"continent_y": "continent", 'AveragScore': "avg_economic_score", "latitude": "lat", "longitude": "long",
                       "rural_population": "rural_pop", "urban_population": "urban_pop"}, inplace=True)
    return df

df = load_data()

# Set up Streamlit page configuration
# Convert 'growth rate' to numeric by stripping '%' and converting to float
df['growth rate'] = df['growth rate'].str.rstrip('%').astype('float')
u=['avg_economic_score', 'SafetySecurity','Governance', 'SocialCapital',
   'InvestmentEnvironment','EconomicQuality', 'LivingConditions', 'Health', 'Education',
       'NaturalEnvironment', '2023 population','area (km²)', 'rural_pop', 'urban_pop']
# Streamlit sidebar for user options
st.sidebar.title("Filter Options")
continent_filter = st.sidebar.multiselect('Select Continent(s)', options=df['continent'].unique(), default=df['continent'].unique())
metric = st.sidebar.selectbox('Select a filter Metric', options=u)

# Filter data based on sidebar options
filtered_df = df[df['continent'].isin(continent_filter)]

# Main title
st.title("World stats 2023 , Analysis Dashboard")

# Top-level metrics
st.subheader("continent-level Insights")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Countries", len(filtered_df))
col2.metric("Average Economic Score", round(filtered_df['avg_economic_score'].mean(), 2))
col3.metric("Total Population (2023)", f"{filtered_df['2023 population'].sum():,}")
col4.metric("Average Growth Rate", f"{filtered_df['growth rate'].mean():.2f}%")

# World Map
st.subheader("World Map")
fig = px.scatter_mapbox(filtered_df, lat="lat", lon='long', zoom=1, hover_name="Country",
                        hover_data=["avg_economic_score", "Health", "Education", "2023 population", 'growth rate'],
                        color="continent", size=metric, size_max=50)
fig.update_layout(mapbox_style='open-street-map', title='Country details')
st.plotly_chart(fig, use_container_width=True)

st.subheader("top and bottom 1 based upon {}".format(metric))
insight_col1, insight_col2 = st.columns(2)
with insight_col1:
    top_country = filtered_df.loc[filtered_df[metric].idxmax()]
    st.metric(f"Top Country by {metric}", top_country['Country'], f"{top_country[metric]:,.2f}")

with insight_col2:
    bottom_country = filtered_df.loc[filtered_df[metric].idxmin()]
    st.metric(f"Bottom Country by {metric}", bottom_country['Country'], f"{bottom_country[metric]:,.2f}")
# Top 5 Countries by Population Bar Chart
st.subheader("Top 5 Countries by Population")
df1 = filtered_df.set_index("Country")
df5 = df1[df1.index.isin(df1["2023 population"].sort_values(ascending=False).head().index)]
bar_fig = px.bar(df5, x=df5.index, y="2023 population", color="continent", title="Top 5 Countries in selected continents on Population")
st.plotly_chart(bar_fig, use_container_width=True)

# Histogram of a selected metric
st.write("Histogram of Selected Metric")
hist_fig = px.histogram(filtered_df, x=metric, color="continent", nbins=40, title=f'Histogram of {metric}')
st.plotly_chart(hist_fig, use_container_width=True)

# Box Plot of key metrics by continent
st.write("Box Plot of Key Metrics by Continent")
box_fig = px.box(filtered_df, x="continent", y=metric, points="all", title=f'Box Plot of {metric} by Continent')
st.plotly_chart(box_fig, use_container_width=True)

# Correlation Heatmap
st.write("Correlation Heatmap of Metrics")
corr = filtered_df.select_dtypes(include=[np.number]).corr()
heatmap_fig = go.Figure(data=go.Heatmap(z=corr.values, x=corr.index.values, y=corr.columns.values, colorscale='Viridis'))
heatmap_fig.update_layout(title='Correlation Heatmap', xaxis_nticks=36)
st.plotly_chart(heatmap_fig, use_container_width=True)
