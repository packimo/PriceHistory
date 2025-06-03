
from matplotlib import pyplot as plt
import numpy as np

# Limitations for the y-axis
LIM_Y_BOTTOM = 5
LIM_Y_TOP = 5

# Ticks for the y-axis
Y_TICKS = 5

# Draw the price history diagram
def draw_diagram(prices, data, title):
    # Name of the diagram
    plt.title(title)
    
    # Names for the x and y axis
    plt.xlabel("Date of query")
    plt.ylabel("Price in €")
    
    # Limitation for the y-axis
    plt.ylim(min(prices) - LIM_Y_BOTTOM, max(prices) + LIM_Y_TOP)
    
    # Ticks for the y-axis
    plt.yticks(np.arange(min(prices) - LIM_Y_BOTTOM, max(prices) + LIM_Y_TOP * 2, Y_TICKS))
    
    # Plot and show the diagram
    plt.plot(data, prices, "bo-")
    plt.show()
