import pandas as pd
import matplotlib.pyplot as plt
from mplfinance.original_flavor import candlestick_ohlc
import matplotlib.dates as mdates
from matplotlib.ticker import FuncFormatter

# Read the CSV file 
df = pd.read_csv('VIC (1).csv') # thay tên file để vẽ biểu đồ 

# Convert Date/Time column to datetime
df['Date/Time'] = pd.to_datetime(df['Date/Time'])

# Set Date/Time as index
df.set_index('Date/Time', inplace=True)

# Create a new DataFrame with OHLC data
ohlc = df[['Open', 'High', 'Low', 'Close']].resample('D').agg({
    'Open': 'first',
    'High': 'max',
    'Low': 'min',
    'Close': 'last'
}).dropna()  # Drop rows with NaN values

# Reset index to get Date as a column
ohlc.reset_index(inplace=True)

# Convert Date to number for plotting
ohlc['Date_num'] = mdates.date2num(ohlc['Date/Time'])

# Create the main figure and axis
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8), sharex=True, gridspec_kw={'height_ratios': [3, 1]})

# Plot candlestick chart
candlestick_ohlc(ax1, ohlc[['Date_num', 'Open', 'High', 'Low', 'Close']].values, width=0.6, colorup='g', colordown='r')

# Set x-axis format
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
ax1.xaxis.set_major_locator(mdates.AutoDateLocator())

# Rotate x-axis labels
plt.setp(ax1.xaxis.get_majorticklabels(), rotation=45, ha='right')

# Set labels and title for candlestick chart
ax1.set_ylabel('Price')
ax1.set_title('VIC Stock Price')

# Plot volume bar chart
volume = df['Volume'].resample('D').sum()
ax2.bar(volume.index, volume.values, color='b', alpha=0.5)

# Set y-axis limits for volume chart
max_volume = volume.max()
ax2.set_ylim(0, max_volume * 1.1)  # Increase upper limit by 10%

# Format y-axis labels to millions
def millions(x, pos):
    return f'{x/1e6:.1f}M'

ax2.yaxis.set_major_formatter(FuncFormatter(millions))

# Set labels for volume chart
ax2.set_ylabel('Volume (Millions)')
ax2.set_xlabel('Date')

# Adjust layout and display the plot
plt.tight_layout()
plt.show()