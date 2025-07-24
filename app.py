import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objs as go

st.title("📈 Stock Price Visualizer")

# User input for ticker symbol
ticker = st.text_input("Enter Stock Ticker Symbol (e.g., AAPL)", "AAPL")

# Date range selection
start_date = st.date_input("Start Date", pd.to_datetime("2020-01-01"))
end_date = st.date_input("End Date", pd.to_datetime("2023-01-01"))

# Initialize session state for data
if 'data' not in st.session_state:
    st.session_state.data = None
if 'ticker_fetched' not in st.session_state:
    st.session_state.ticker_fetched = None

# Fetch data button
if st.button("Fetch Data"):
    try:
        data = yf.download(ticker, start=start_date, end=end_date)
        if not data.empty:
            st.session_state.data = data
            st.session_state.ticker_fetched = ticker
            st.success(f"Data fetched successfully for {ticker} with {len(data)} rows.")
        else:
            st.error("No data found. Please check the ticker symbol and date range.")
            st.session_state.data = None
            st.session_state.ticker_fetched = None
    except Exception as e:
        st.error(f"Error fetching data: {str(e)}")
        st.session_state.data = None
        st.session_state.ticker_fetched = None

# Process and display data if available
if st.session_state.data is not None:
    data = st.session_state.data.copy()
    ticker_name = st.session_state.ticker_fetched
    
    # Determine maximum allowable MA window
    max_window = len(data)
    
    if max_window < 2:
        st.error("Not enough data to perform analysis. Try a wider date range.")
    else:
        # Moving average window input
        ma_window = st.number_input(
            "Moving Average Window (days)",
            min_value=1,
            max_value=max_window,
            value=min(20, max_window),
            key="ma_window"
        )
        
        # Only proceed if we have a valid ma_window value
        if ma_window and ma_window > 0:
            # Compute moving average and percent return
            ma_column_name = f"MA{ma_window}"
            data[ma_column_name] = data['Close'].rolling(window=ma_window).mean()
            data['Percent Return'] = data['Close'].pct_change() * 100
            
            st.subheader(f"Showing data for {ticker_name}")
            st.dataframe(data)
            
            # Plot Close Price and Moving Average
            # Check if we have enough data points for the moving average
            valid_ma_data = data[ma_column_name].dropna()
            
            if len(valid_ma_data) > 0:
                # Create plot data by dropping rows where MA is NaN
                plot_data = data[data[ma_column_name].notna()].copy()
                
                if len(plot_data) > 0:
                    fig_price = go.Figure()
                    fig_price.add_trace(go.Scatter(
                        x=plot_data.index, 
                        y=plot_data['Close'], 
                        mode='lines', 
                        name='Close Price'
                    ))
                    fig_price.add_trace(go.Scatter(
                        x=plot_data.index, 
                        y=plot_data[ma_column_name], 
                        mode='lines', 
                        name=f"MA{ma_window}"
                    ))
                    fig_price.update_layout(
                        title=f"{ticker_name} Price & {ma_window}-Day Moving Average",
                        xaxis_title="Date",
                        yaxis_title="Price (USD)"
                    )
                    st.plotly_chart(fig_price)
                else:
                    st.warning(f"No valid data points for {ma_window}-day moving average plot.")
            else:
                st.warning(f"Not enough data to compute a {ma_window}-day moving average.")
            
            # Plot percent returns if data is long enough
            if len(data) >= 2:
                returns_data = data['Percent Return'].dropna()
                if len(returns_data) > 0:
                    fig_returns = go.Figure()
                    fig_returns.add_trace(go.Scatter(
                        x=returns_data.index, 
                        y=returns_data, 
                        mode='lines', 
                        name='Percent Return'
                    ))
                    fig_returns.update_layout(
                        title=f"{ticker_name} Daily Percent Returns",
                        xaxis_title="Date",
                        yaxis_title="Percent Return (%)"
                    )
                    st.plotly_chart(fig_returns)