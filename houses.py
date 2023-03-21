import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as ticker


file_path = '/Users/jakewatembach/Desktop/houseprices/Real_Estate_Sales_2001-2020_GL.csv'
data = pd.read_csv(file_path, low_memory=False)


try:
    data['Date Recorded'] = pd.to_datetime(data['Date Recorded'], format='%m/%d/%y')
except ValueError:
    data['Date Recorded'] = pd.to_datetime(data['Date Recorded'], format='%m/%d/%Y')


grouped_data = data.groupby(data['Date Recorded'].dt.year).agg({'Assessed Value': 'mean', 'Sale Amount': 'mean'}).reset_index()

# Calculate the average appreciation over time
grouped_data['Appreciation'] = grouped_data['Sale Amount'] - grouped_data['Assessed Value']

# Create the chart
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(grouped_data['Date Recorded'], grouped_data['Appreciation'], marker='o', linestyle='-', linewidth=2)


ax.set_title('Average House Appreciation in Connecticut Over Time')
ax.set_xlabel('Year')
ax.set_ylabel('Average Appreciation ($)')


ax.xaxis.set_major_locator(ticker.MaxNLocator(integer=True))
formatter = ticker.FuncFormatter(lambda x, pos: '${:,.0f}'.format(x))
ax.yaxis.set_major_formatter(formatter)


plt.grid(True)
plt.tight_layout()

plt.savefig('house_appreciation_chart.png')

plt.show()
