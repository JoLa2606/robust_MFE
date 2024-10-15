# Use sortData.py first

# Creates the graphs for the optimal policy

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from fractions import Fraction

# Set global font size for ticks, axis labels, and legends
plt.rc('font', size=14)  # Default text size
plt.rc('axes', titlesize=14, labelsize=14)  # Axis titles and labels
plt.rc('xtick', labelsize=12)  # X-tick labels
plt.rc('ytick', labelsize=12)  # Y-tick labels
plt.rc('legend', fontsize=12)  # Legend text size

# Define line styles to avoid overlap
line_styles = ['-', '--', '-.', ':']

dimX = 5
lmbdRange = 5

for t in range(2):
    for x in range(dimX):
        X = x

        # Read data from text file without header
        data = pd.read_csv(f'output_wpi{t}.txt', delim_whitespace=True, header=None)

        # Select rows based on the range
        u = lmbdRange * x
        o = lmbdRange * (x + 1)
        data = data.iloc[u:o, :]

        # Drop unnecessary columns
        data = data.drop(columns=[1])

        # Assign column names manually
        data.columns = ['Lambda', 'a = -1', 'a = 0', 'a = 1']

        # Display the DataFrame to ensure it's loaded correctly
        print(data)

        # Create an artificial equidistant x-axis
        equidistant_x = np.arange(len(data))

        # Generate custom tick labels in the form of fractions
        tick_labels = [Fraction(1, len(data) - i) for i in equidistant_x]
        tick_labels[0] = 0

        # Plot each column against the equidistant x-axis
        for i, column in enumerate(data.columns[1:]):
            plt.plot(equidistant_x, data[column], label=column, marker='o', linestyle=line_styles[i % len(line_styles)])

        # Set custom x-ticks and labels using fractions
        plt.xticks(ticks=equidistant_x, labels=tick_labels)

        # Add labels and title
        plt.xlabel('$\lambda$ (Level of Uncertainty)')
        plt.ylabel(f'Weights of $\pi_{{{t}}}$')
        plt.title(f'Weights of $\pi_{{{t}}}(\cdot \mid {X})$ for different Levels of Uncertainty $\lambda$')
        plt.legend()

        # Adjust layout to prevent overlap
        plt.tight_layout()

        # Save plot as PDF
        plt.savefig(f'graph_wpi{t}_{X}.pdf', format='pdf', dpi=300)

        # Clear the plot for the next iteration
        plt.clf()