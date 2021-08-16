import plotly.figure_factory as ff
import plotly.express as go
import statistics
import random
import pandas as pd
import csv

df = pd.read_csv("medium_data.csv")

data = df["responses"].tolist()

population_mean = statistics.mean(data)
print("Populaton mean:- ", population_mean)

# Code to find the mean of 30 data samples 1000 times 
def random_set_of_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_index = random.randint(0, len(data))
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

mean_list = []
for i in range(0,1000):
    set_of_means = random_set_of_mean(30)
    mean_list.append(set_of_means)

# Calculating mean and standard deviation of the sampling distribution
std_deviation = statistics.stdev(data)
print("Standard deviation:- ", std_deviation)
mean = statistics.mean(mean_list)
print("Mean of sampling distribution:- ", mean)

# Function to plot the mean on the graph.
def show_fig(mean_list):
    df = mean_list
    fig = ff.create_distplot([data], ["responses"], show_hist = False)
    fig.add_trace(go.Scatter(x = [mean, mean], y = [0, 1], mode = "lines", name = "MEAN"))
    fig.show()

# Function to repeat the process 100 times
def setup():
    mean_list = []
    for i in range(0, 100):
        set_of_means = random_set_of_mean(30)
        mean.list.append(set_of_means)
    show_fig(mean_list)

# Findig the standard deviation starting and ending values
first_std_deviation_start, first_std_deviation_end = mean-std_deviation, mean+std_deviation
second_std_deviation_start, second_std_deviation_end = mean-(2*std_deviation), mean+(2*std_deviation)
third_std_deviation_start, third_std_deviation_end = mean-(3*std_deviation), mean+(3*std_deviation)

# Finding the mean and plotting on graph
df = pd.read_csv("medium_data.csv")
data = df["responses"].tolist()
mean_of_sample = statistics.mean(data)
print("Mean of sample1:- ",mean_of_sample)
fig = ff.create_distplot([mean_list], ["student marks"], show_hist=False)
fig.add_trace(go.Scatter(x = [mean, mean], y = [0, 0.17], mode = "lines", name = "MEAN"))
fig.add_trace(go.Scatter(x = [mean_of_sample, mean_of_sample], y = [0, 0.17], mode = "lines", name = "MEAN OF STUDENTS WHO HAD MATH LABS"))
fig.add_trace(go.Scatter(x = [first_std_deviation_end, first_std_deviation_end], y = [0, 0.17], mode = "lines", name = "STANDARD DEVIATION 1 END"))
fig.add_trace(go.Scatter(x = [second_std_deviation_end, second_std_deviation_end], y = [0, 0.17], mode = "lines", name = "STANDARD DEVIATION 2 END"))
fig.add_trace(go.Scatter(x = [third_std_deviation_end, third_std_deviation_end], y = [0, 0.17], mode = "lines", name = "STANDARD DEVIATION 3 END"))
fig.show()

# Finding the z score using the formula
z_score = (mean - mean_of_sample)/std_deviation
print("The z score is = ",z_score)