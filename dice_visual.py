from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# Create a D6 and a D10.
die_1 = Die(8)
die_2 = Die(8)

# Numver of dice
die_count = 2

# Make some rolls, and store results in a list.
results = []
results = [(die_1.roll() + die_2.roll()) for roll_num in range(500_000)]
print(results)

# Aanlyze the results.
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
frequencies = [results.count(value) for value in range(2, max_result+1)]
print(frequencies)

# Visualize the results.
x_values = list(range(die_count, max_result+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of rolling a D6 and a D10 dice 50000 times' , xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d8_d8.html')

print(frequencies)