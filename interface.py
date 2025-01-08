import tkinter as tk
from tkinter import ttk
import datafinder as d

# Load the CSV file and get unique categories
data = d.load_csv("sales_data.csv")
unique_categories = d.get_unique_categories(data)

# Ensure unique_categories is a list
if not isinstance(unique_categories, list):
    unique_categories = []

# Create the main window
root = tk.Tk()
root.title("Flash Sale Tracker")

# Create a frame for the dropdown menus
frame = tk.Frame(root)
frame.pack(pady=10)

# Label for "Filter by"
filter_label = tk.Label(frame, text="Filter by:")
filter_label.grid(row=0, column=0, padx=5)

# Dropdown for Category
category_var = tk.StringVar(value="All")
category_label = tk.Label(frame, text="Category:")
category_label.grid(row=0, column=1, padx=5)
category_menu = ttk.Combobox(frame, textvariable=category_var, values=["All"] + unique_categories)
category_menu.grid(row=0, column=2, padx=5)

# Dropdown for Actual Price
actual_price_var = tk.StringVar(value="None")
actual_price_label = tk.Label(frame, text="Actual Price:")
actual_price_label.grid(row=0, column=3, padx=5)
actual_price_menu = ttk.Combobox(frame, textvariable=actual_price_var, values=["None", "Ascending", "Descending"])
actual_price_menu.grid(row=0, column=4, padx=5)

# Dropdown for Discounted Price
discounted_price_var = tk.StringVar(value="None")
discounted_price_label = tk.Label(frame, text="Discounted Price:")
discounted_price_label.grid(row=1, column=1, padx=5)
discounted_price_menu = ttk.Combobox(frame, textvariable=discounted_price_var, values=["None", "Ascending", "Descending"])
discounted_price_menu.grid(row=1, column=2, padx=5)

# Dropdown for Discount Percentage
discount_percentage_var = tk.StringVar(value="None")
discount_percentage_label = tk.Label(frame, text="Discount Percentage:")
discount_percentage_label.grid(row=1, column=3, padx=5)
discount_percentage_menu = ttk.Combobox(frame, textvariable=discount_percentage_var, values=["None", "Ascending", "Descending"])
discount_percentage_menu.grid(row=1, column=4, padx=5)

# Dropdown for Number of Results
num_results_var = tk.StringVar(value="10")
num_results_label = tk.Label(frame, text="Number of Results:")
num_results_label.grid(row=2, column=1, padx=5)
num_results_menu = ttk.Combobox(frame, textvariable=num_results_var, values=["10", "20", "50", "100"])
num_results_menu.grid(row=2, column=2, padx=5)

# Function to filter data based on user input
def filter_data():
    category = category_var.get()
    sort_actual_price = actual_price_var.get().lower()
    sort_discounted_price = discounted_price_var.get().lower()
    sort_discount_percentage = discount_percentage_var.get().lower()
    num_results = int(num_results_var.get())

    # Call the updated filter_dataframe function
    filtered_data = d.filter_dataframe(
        data,
        category=category,
        sort_actual_price=sort_actual_price,
        sort_discounted_price=sort_discounted_price,
        sort_discount_percentage=sort_discount_percentage,
        num_results=num_results,
    )

    # Display the filtered data
    output_text.delete(1.0, tk.END)
    if filtered_data.empty:
        output_text.insert(tk.END, "No results match your filters.\n")
    else:
        output_text.insert(tk.END, filtered_data.to_string(index=False))
        
# Button to apply filter
filter_button = tk.Button(root, text="Apply Filter", command=filter_data)
filter_button.pack(pady=10)

# Output display
output_text = tk.Text(root, wrap=tk.WORD, width=100, height=20)
output_text.pack(pady=10)

root.mainloop()