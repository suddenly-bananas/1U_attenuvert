import numpy as np
import matplotlib.pyplot as plt

# code mainly provided by duck.ai and then adjusted for personal needs

# Function to plot
def plot_graphs(start, end_values, step=0.1):
    num_plots = len(end_values)
    fig, axes = plt.subplots(num_plots, 1, figsize=(10, 2 * num_plots))

    num_columns = 2

    rows = num_plots // num_columns + num_plots % num_columns  # Calculate number of rows needed
    fig, axes = plt.subplots(rows, num_columns, figsize=(12, 2 * rows))  # 2 columns
    
    # Flatten axes for easier indexing
    axes = axes.flatten()

    for ax, end in zip(axes, end_values):
        # Generate x values
        x = np.arange(start, end, step)
        # Calculate y values
        R_in = 100 # 100k
        R_F = 100 # 100k
        R_2 = x # ranging from 0 to 10k
        R_1 = end - x # ranging from 10k to 0
        y = (R_2*R_F)/(R_in*10 + R_1*R_2)
        
        # Create the plot
        ax.set_title(f'Gain function for R_pot = {end} kOhm')
        ax.plot(x, y, label='-U_out/U_in', color='blue')
        ax.set_xlabel('Value of R_2 in kOhm')
        ax.axhline(0, color='black',linewidth=0.5, ls='--')
        ax.axvline(0, color='black',linewidth=0.5, ls='--')
        ax.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
        ax.legend()

    # Hide any empty subplots if the number of plots is less than the number of subplots
    for i in range(num_plots, len(axes)):
        fig.delaxes(axes[i])

    plt.tight_layout()  # Adjust layout to prevent overlap
    plt.show()

# Specify the range for x-input
start = 0        # Start of range
end_values = [(i+1)*10 for i in range(10)] # corresponds to 10...100 kOhms in the plot
step = 0.1      # Step size

# Call the function to plot the graph
plot_graphs(start, end_values, step)
