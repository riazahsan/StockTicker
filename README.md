# StockVisualizer

A simple and interactive web application to visualize historical stock prices, moving averages, and daily percent returns using Streamlit, yfinance, and Plotly.

## Features

- 📈 Visualize historical stock price data for any ticker symbol (e.g., AAPL, MSFT, TSLA)
- 📅 Select custom date ranges for analysis
- 🧮 Calculate and plot moving averages with adjustable window size
- 🔄 View daily percent returns
- 🖥️ Interactive charts powered by Plotly

## Demo

![StockVisualizer Demo](#) <!-- Optionally add a screenshot or GIF here -->

## Requirements

- Python 3.7+
- [Streamlit](https://streamlit.io/)
- [yfinance](https://github.com/ranaroussi/yfinance)
- [pandas](https://pandas.pydata.org/)
- [plotly](https://plotly.com/python/)

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/StockVisualizer.git
   cd StockVisualizer
   ```

2. **(Optional) Create and activate a virtual environment:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies:**

   ```bash
   pip install streamlit yfinance pandas plotly
   ```

## Usage

1. **Run the Streamlit app:**

   ```bash
   streamlit run app.py
   ```

2. **Open your browser:**
   - Go to the local URL provided by Streamlit (usually http://localhost:8501)

3. **Interact with the app:**
   - Enter a stock ticker symbol (e.g., AAPL)
   - Select the start and end dates
   - Click "Fetch Data"
   - Adjust the moving average window as desired
   - View the data table and interactive charts

## File Structure

```
StockVisualizer/
  app.py         # Main Streamlit application
  README.md      # Project documentation
  venv/          # (Optional) Virtual environment
```

## Notes
- Data is fetched using Yahoo Finance via the `yfinance` library.
- Moving average and percent return calculations are performed on the closing price.
- The app handles invalid tickers and empty data gracefully.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

## Acknowledgements
- [Streamlit](https://streamlit.io/)
- [yfinance](https://github.com/ranaroussi/yfinance)
- [Plotly](https://plotly.com/python/)
- [pandas](https://pandas.pydata.org/)
