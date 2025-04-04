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

first_text = """
The pricing algorithms that individual hotels use on Booking.com illustrate the case of algorithm orchestration:
"""

text = """
Let’s go back to 1960. Imagine the competition between hotels prior to any such centralized platform like Booking.com. Involving substantial search costs and with a lot of informational frictions, individual guests would check availabilities and compare prices across hotels, probably by telephone, and decide to book the one that faired best after cost-benefit analysis. Between two equally attractive hotels, the customer would reserve a room at the cheaper one.

In the mid 1990s, all major hotels and hotel chains begin to offer online booking tools. Immediately afterwards, the first booking platforms emerge (e.g. Expedia). Now a lot of the informational frictions and search costs disappear. Frictionless competition finally has arrived. Guests check and compare prices easily, and decide to book the best deals. While matching clients and hotels quite efficiently, hotels probably actually dislike the platforms somehow for the high fees they charge and the price fight they accelerate.

Now, in 2025, these platforms have become even more central in the game, and hotels seems to have made peace with them. So what changed in between? The main innovation are the platforms own “pricing algorithms.” These are tools that hotels plug in with their booking engines to automatically update prices as per algorithm suggestion. The platforms discourage the hotels to offer better rates off-platform. If one imagined an algorithm built for one hotel, to maximize that hotels gains individually, then one would get something like an optimal undercutter that, given the prices charged by all competitors, at any time undercuts optimally to attract the maximal demand. If all hotels were to use such tools, then there would be a tremendous price competition, and the result would probably be very low prices and great deals for guests.

However, when all prices are orchestrated by algorithms issued by the same platform, as is the case, or worse still when all prices are orchestrated by the same central algorithm, one clearly would not expect such price fight. Taking the case of two hotels in such a situation one would instead imagine a profit-maximizing monopoly price being charged on average with some fluctuations between the two, so that half of the time one is cheaper, and the other half the other. Each party could individually improve by undercutting the other hotel at any moment, but both would be much worse off if they both started doing so. Sticking with the recommended prices instead guarantees prices on the Pareto frontier, that is, as profitable as it gets.

Check out some of the prices we have been finding on Booking.com?

What does it look like to you? Competition or Orchestration?
"""

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
        st.markdown(first_text)

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
            fig.update_layout(height=600, autosize=True)

            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("No valid price data available for the selected filters")

        st.markdown(text)

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
# if st.sidebar.button("Refresh Data"):
#     st.experimental_rerun()

# Add information about the data
st.sidebar.info("""
    This dashboard displays hotel price data scraped from Booking.com.
    The data is updated hourly and shows next-day prices for selected hotels.
""")