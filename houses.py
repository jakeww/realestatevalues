import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as ticker

# Read the .csv file
file_path = '/Users/jakewatembach/Desktop/houseprices/Real_Estate_Sales_2001-2020_GL.csv'
data = pd.read_csv(file_path, low_memory=False)

# Fix the year component of the Date Recorded column
try:
    data['Date Recorded'] = pd.to_datetime(data['Date Recorded'], format='%m/%d/%y')
except ValueError:
    data['Date Recorded'] = pd.to_datetime(data['Date Recorded'], format='%m/%d/%Y')

# Group by year and calculate the average assessed value and sale amount
grouped_data = data.groupby(data['Date Recorded'].dt.year).agg({'Assessed Value': 'mean', 'Sale Amount': 'mean'}).reset_index()

# Calculate the average appreciation over time
grouped_data['Appreciation'] = grouped_data['Sale Amount'] - grouped_data['Assessed Value']

# Create the chart
fig, ax = plt.subplots(figsize=(12, 8))

# Set the background color of the chart
ax.set_facecolor('#2c2c2c')
fig.set_facecolor('#2c2c2c')

# Plot the line with a colorful appearance
ax.plot(grouped_data['Date Recorded'], grouped_data['Appreciation'], marker='o', linestyle='-', linewidth=2, markersize=8, color='#2ca02c')

# Set chart title, labels, and format the date on x-axis
ax.set_title('Average House Appreciation in Connecticut Over Time', fontsize=18, fontweight='bold', color='white')
ax.set_xlabel('Year', fontsize=14, color='white')
ax.set_ylabel('Average Appreciation ($)', fontsize=14, color='white')

# Set x-axis to display each year and set its color
ax.xaxis.set_major_locator(ticker.MaxNLocator(integer=True))
ax.tick_params(axis='x', colors='white')

# Format y-axis as dollars with thousands separator and set its color
formatter = ticker.FuncFormatter(lambda x, pos: '${:,.0f}'.format(x))
ax.yaxis.set_major_formatter(formatter)
ax.tick_params(axis='y', colors='white')

# Customize grid lines
ax.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.7)

# Add data labels to the points and adjust their positions based on y-values
#for i, (x, y) in enumerate(zip(grouped_data['Date Recorded'], grouped_data['Appreciation'])):
 #   label_offset = 0.02 * (i % 2)  # Alternate between 0 and 0.02 for label positions
  #  ax.text(x, y + label_offset * y, '${:,.0f}'.format(y), fontsize=12, ha='center', va='bottom', color='white')

# Make the chart visually appealing
plt.tight_layout()

# Save the chart as an image file
plt.savefig('house_appreciation_chart.png', facecolor=fig.get_facecolor())

# Display the chart
plt.show()
