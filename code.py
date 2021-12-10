import pandas as pd
import statistics
import csv
import plotly.figure_factory as ff
import plotly.graph_objects as go 

df = pd.read_csv("data.csv")
data = df["reading_time"].to_list()

# calculating mean
data_mean = sum(data) / len(data)

#calculating median
data_median = statistics.median(data)

#calculating mode
data_mode = statistics.mode(data)

print("Mean, Median and Mode of data is {}, {} and {} respectively".format(data_mean, data_median,data_mode))

# standard deviation
data_std = statistics.stdev(data)

data1_std_deviation_start,data1_std_deviation_end = data_mean - data_std, data_mean + data_std
data2_std_deviation_start,data2_std_deviation_end = data_mean - (2*data_std), data_mean + (2*data_std)
data3_std_deviation_start,data3_std_deviation_end = data_mean - (3*data_std), data_mean + (3*data_std)

# plotting the chart
fig = ff.create_distplot([data], ["reading_time"], show_hist=False)
fig.add_trace(go.Scatter(x=[data_mean,data_mean], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[data1_std_deviation_end,data1_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[data2_std_deviation_end,data2_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 "))
fig.show()

# making lists
data_list_of_data_within_1_std_deviation = [result for result in data if result > data1_std_deviation_start and result < data1_std_deviation_end]
data_list_of_data_within_2_std_deviation = [result for result in data if result > data2_std_deviation_start and result < data2_std_deviation_end]
data_list_of_data_within_3_std_deviation = [result for result in data if result > data3_std_deviation_start and result < data3_std_deviation_end]

# printing the data
print("{}% of data for height lies within 1 standard deviation".format(len(data_list_of_data_within_1_std_deviation)*100.0/len(data)))
print("{}% of data for height lies within 2 standard deviation".format(len(data_list_of_data_within_2_std_deviation)*100.0/len(data)))
print("{}% of data for height lies within 3 standard deviation".format(len(data_list_of_data_within_3_std_deviation)*100.0/len(data)))
