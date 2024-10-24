import tkinter as tk
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

# Function to plot the pie chart
def plot_pie_chart():
    try:
        # Data for the pie chart
        labels = ["Category A", "Category B", "Category C", "Category D"]
        sizes = [25, 35, 20, 20]

        # Create a Matplotlib figure for the pie chart
        fig, ax = plt.subplots()
        ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
        ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

        # Clear previous canvas if present
        for widget in chart_frame.winfo_children():
            widget.destroy()

        # Display the chart on the Tkinter window
        canvas = FigureCanvasTkAgg(fig, master=chart_frame)
        canvas.draw()
        canvas.get_tk_widget().pack()

    except Exception as e:
        messagebox.showerror("Error", str(e))

# Create the main Tkinter window
root = tk.Tk()
root.title("Pie Chart GUI")

# Create a frame to contain the pie chart
chart_frame = tk.Frame(root)
chart_frame.pack()

# Create a button to plot the pie chart
plot_button = tk.Button(root, text="Plot Pie Chart", command=plot_pie_chart)
plot_button.pack()

# Run the Tkinter event loop
root.mainloop()
