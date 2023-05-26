import matplotlib.pyplot as plt
import numpy as np

# Read dataset from file
dataset_file = "Assets/dataset_2.txt"

dataset = []
with open(dataset_file, 'r') as file:
    # Skip the header
    next(file)
    for line in file:
        date, visitors = line.strip().split(',')
        dataset.append([date, float(visitors) if visitors != 'Nan' else float('nan')])

# Perform linear interpolation
interpolated_dataset = []
for i in range(len(dataset)):
    if not np.isnan(dataset[i][1]):
        interpolated_dataset.append(dataset[i])
    else:
        j = i - 1
        while np.isnan(dataset[j][1]):
            j -= 1
        start_date = np.datetime64(dataset[j][0])
        start_visitors = dataset[j][1]
        end_date = np.datetime64(dataset[i + 1][0])
        end_visitors = dataset[i + 1][1]
        days = (end_date - start_date).astype('timedelta64[D]').astype(int)
        interpolated_values = np.linspace(start_visitors, end_visitors, days + 2)[1:-1]
        interpolated_dates = np.arange(start_date + np.timedelta64(1, 'D'), end_date, dtype='datetime64[D]')
        interpolated_dates = interpolated_dates.astype(str)
        interpolated_dataset.extend(zip(interpolated_dates, interpolated_values))

dates = [entry[0] for entry in interpolated_dataset]
visitors = [entry[1] for entry in interpolated_dataset]

# Plot the data
plt.plot(dates, visitors, label='Interpolated Data')
plt.xlabel('Date')
plt.ylabel('Visitors')
plt.title('Visitor Analysis')
plt.xticks(rotation=45)
plt.legend()
plt.show()
