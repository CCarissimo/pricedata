import streamlit as st
import pandas as pd
import plotly.express as px
import json
import os
from datetime import datetime
import glob

# Set page title and layout
st.set_page_config(page_title="Hotel Price Tracker", layout="wide")
st.title("New York Hotel Price Trends")


# Function to load the latest data
@st.cache_data(ttl=3600)  # Cache for 1 hour
def load_data(data_path="/media/data/pricedata_cesare/data/"):
    # Get list of all JSON files in the directory
    json_files = glob.glob(os.path.join(data_path, "*.json"))

    if not json_files:
        st.error("No data files found")
        return None

    # Sort files by modification time to get the latest ones first
    json_files.sort(key=os.path.getmtime, reverse=True)

    # Load all data files
    all_data = []
    for file in json_files:
        # try:
            with open(file, 'r') as f:
                data = json.load(f)
                # Extract date from filename
                filename = os.path.basename(file)
                date_str = filename.split('.')[0]  # Remove file extension
                date = datetime.strptime(date_str, "%Y-%m-%d_%H")

                # Process the data
                for hotel, value in data.items():
                    # Clean price data
                    if type(value) is dict:
                        price = value["price"]
                    else:
                        price = value

                    if price != "nan":
                        # Extract numeric value from price string (e.g., "$150" -> 150)
                        numeric_price = ''.join(filter(lambda x: x.isdigit() or x == '.', price))
                        try:
                            numeric_price = float(numeric_price)
                        except:
                            numeric_price = None
                    else:
                        numeric_price = None

                    all_data.append({
                        "hotel": hotel,
                        "price": numeric_price,
                        "date": date,
                        "raw_price": price
                    })
        # except Exception as e:
        #     st.warning(f"Error loading file {file}: {e}")

    # Convert to DataFrame
    df = pd.DataFrame(all_data)

    # Sort the dataframe by 'date'
    df = df.sort_values(by="date", ascending=True)

    return df


# Load data
df = load_data("./data/")

if df is not None and not df.empty:
    # Add sidebar filters
    st.sidebar.header("Filters")

    # Date range filter
    min_date = df['date'].min().date()
    max_date = df['date'].max().date()
    date_range = st.sidebar.date_input(
        "Select Date Range",
        value=(min_date, max_date),
        min_value=min_date,
        max_value=max_date
    )

    if len(date_range) == 2:
        start_date, end_date = date_range
        df_filtered = df[(df['date'].dt.date >= start_date) & (df['date'].dt.date <= end_date)]
    else:
        df_filtered = df

    # Hotel selection
    hotels = sorted(df['hotel'].unique())
    selected_hotels = st.sidebar.multiselect(
        "Select Hotels",
        options=hotels,
        default= ["iroquois", "margaritaville"] #hotels[:5]  # Default to showing first 5 hotels
    )

    if selected_hotels:
        df_filtered = df_filtered[df_filtered['hotel'].isin(selected_hotels)]

    # Create visualizations
    with st.container():
        # st.subheader("Price Trends Over Time")

        # Check if there's valid data to plot
        if not df_filtered.empty and df_filtered['price'].notna().any():
            fig = px.line(
                df_filtered,
                x="date",
                y="price",
                color="hotel",
                # title="Hotel Price Trends",
                labels={"date": "Date", "price": "Price (USD)", "hotel": "Hotel"},
                hover_data=["raw_price"]
            )

            # Adjust the height of the plot (e.g., 700 pixels)
            fig.update_layout(height=900, autosize=True)

            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("No valid price data available for the selected filters")

        # st.subheader("Current Price Comparison")

        # Get the latest date data
        # latest_date = df_filtered['date'].max()
        # latest_data = df_filtered[df_filtered['date'] == latest_date]
        #
        # if not latest_data.empty and latest_data['price'].notna().any():
        #     fig = px.bar(
        #         latest_data.sort_values('price', ascending=False),
        #         x="hotel",
        #         y="price",
        #         title=f"Latest Prices ({latest_date.strftime('%Y-%m-%d %H:%M')})",
        #         labels={"hotel": "Hotel", "price": "Price (USD)"},
        #         color="hotel",
        #         text_auto=True
        #     )
        #     fig.update_layout(showlegend=False)
        #     st.plotly_chart(fig, use_container_width=True)
        # else:
        #     st.info("No valid price data available for the latest date")

    # Show raw data if requested
    if st.sidebar.checkbox("Show Raw Data"):
        st.subheader("Raw Data")
        st.dataframe(df_filtered.sort_values(by=['date', 'hotel'], ascending=[False, True]))
else:
    st.error("No data available to display")

# Add refresh button
if st.sidebar.button("Refresh Data"):
    st.experimental_rerun()

# Add information about the data
st.sidebar.info("""
    This dashboard displays hotel price data scraped from Booking.com.
    The data is updated daily and shows next-day prices for selected hotels.
""")