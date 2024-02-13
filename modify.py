import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
file_path = "D:/csv files/NFLX.csv"  # Update this to your CSV file path
df = pd.read_csv(file_path)

# Select the metric to visualize - for example, 'Close' price
metric = 'Close'

# Check if the metric exists in the DataFrame
if metric in df.columns:
    # Plotting
    plt.figure(figsize=(10, 6))
    plt.plot(df['Date'], df[metric], label=metric)
    plt.xlabel('Date')
    plt.ylabel(metric)
    plt.title(f'{metric} over Time')
    plt.legend()
    plt.grid(True)
    plt.xticks(rotation=45)  # Rotate the x-axis labels for better readability
    plt.tight_layout()

    # Display the plot
    plt.show()
else:
    print(f"The metric '{metric}' does not exist in the CSV file.")
