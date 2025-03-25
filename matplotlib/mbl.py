import matplotlib as mpl
import matplotlib.pyplot as plt

# Create some data
x = [1, 2, 3, 4, 5, 6]
y = [2, 3, 5, 7, 11, 1]

# Create a figure and axis
plt.plot(x, y, marker='o', linestyle='--', color='r', label='Prime Numbers')
plt.legend()

# Add grid for better readability
plt.grid(True)

# Set limits for x and y axes
plt.xlim(0, 7)
plt.ylim(0, 12)

# Set ticks for x and y axes
plt.xticks(x, ['1978', '1979', '1980', '1981', '1982', '1983'])
plt.yticks(range(0, 12, 2), ['$0M', '$2M', '$4M', '$6M', '$8M', '$10M'])

# Add annotations for each point
for i, txt in enumerate(y):
    plt.annotate(txt, (x[i], y[i]), textcoords="offset points", xytext=(0,10), ha='center')

# Add a title
plt.title('Money Over the Years')
plt.xlabel('Years')
plt.ylabel('Money')

# Show the plot
plt.show()  