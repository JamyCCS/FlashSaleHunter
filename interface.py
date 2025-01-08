import tkinter as tk  # Import the tkinter library for GUI
from tkinter import ttk  # Import the ttk module for themed widgets
from tkinter import PhotoImage  # Import the PhotoImage module for image handling
from tkinter import messagebox  # Import the messagebox module for dialog boxes
import datafinder as d  # Import the datafinder module for data handling
from PIL import Image, ImageTk  # Import the PIL library for image handling

# Load the CSV file and get unique categories
data = d.load_csv("sales_data.csv")  # Load the sales data from a CSV file

# Check if data is empty
if data.empty:  # Check if the data is empty
    messagebox.showerror("Error", "No data found. Please check the file path.")  # Show an error message 
    exit()  # Exit the program

unique_categories = d.get_unique_categories(data)  # Get unique categories from the data

# Ensure unique_categories is a list
if not isinstance(unique_categories, list):  # Check if unique_categories is a list
    messagebox.warning("Warning","No Unique Categories")
    unique_categories = []  # If not, set it to an empty list

# Create the main window
root = tk.Tk()  # Create the main window
root.title("Flash Sale Tracker")  # Set the title of the window
root.iconphoto(False, PhotoImage(file='amazon_PNG5.png'))

# bg_image = Image.open("bg.jpg")
# resized_image=bg_image.resize((600,100)) #fill the image to the size of the window
# final_image= ImageTk.PhotoImage(resized_image)
# image_label=tk.Label(root,image=final_image)
# image_label.place(relwidth=1, relheight=1 )  # Place the label to cover the entire window


# Create a frame for the dropdown menus
frame = tk.Frame(root)  # Create a frame to hold the dropdown menus
frame.pack(pady=10)  # Add padding around the frame

# Label for "Filter by"
filter_label = tk.Label(frame, text="Filter by:")  # Create a label for "Filter by"
filter_label.grid(row=0, column=0, padx=5)  # Place the label in the grid

# Dropdown for Category
category_var = tk.StringVar(value="All")  # Create a variable to store the selected category
category_label = tk.Label(frame, text="Category:")  # Create a label for the category dropdown
category_label.grid(row=0, column=1, padx=5)  # Place the label in the grid
category_menu = ttk.Combobox(frame, textvariable=category_var, values=["All"] + unique_categories)  # Create the category dropdown
category_menu.grid(row=0, column=2, padx=5)  # Place the dropdown in the grid

# Dropdown for Actual Price
actual_price_var = tk.StringVar(value="None")  # Create a variable to store the selected actual price sorting option
actual_price_label = tk.Label(frame, text="Actual Price:")  # Create a label for the actual price dropdown
actual_price_label.grid(row=0, column=3, padx=5)  # Place the label in the grid
actual_price_menu = ttk.Combobox(frame, textvariable=actual_price_var, values=["None", "Ascending", "Descending"])  # Create the actual price dropdown
actual_price_menu.grid(row=0, column=4, padx=5)  # Place the dropdown in the grid

# Dropdown for Discounted Price
discounted_price_var = tk.StringVar(value="None")  # Create a variable to store the selected discounted price sorting option
discounted_price_label = tk.Label(frame, text="Discounted Price:")  # Create a label for the discounted price dropdown
discounted_price_label.grid(row=1, column=1, padx=5)  # Place the label in the grid
discounted_price_menu = ttk.Combobox(frame, textvariable=discounted_price_var, values=["None", "Ascending", "Descending"])  # Create the discounted price dropdown
discounted_price_menu.grid(row=1, column=2, padx=5)  # Place the dropdown in the grid

# Dropdown for Discount Percentage
discount_percentage_var = tk.StringVar(value="None")  # Create a variable to store the selected discount percentage sorting option
discount_percentage_label = tk.Label(frame, text="Discount Percentage:")  # Create a label for the discount percentage dropdown
discount_percentage_label.grid(row=1, column=3, padx=5)  # Place the label in the grid
discount_percentage_menu = ttk.Combobox(frame, textvariable=discount_percentage_var, values=["None", "Ascending", "Descending"])  # Create the discount percentage dropdown
discount_percentage_menu.grid(row=1, column=4, padx=5)  # Place the dropdown in the grid

# Dropdown for Number of Results
num_results_var = tk.StringVar(value="10")  # Create a variable to store the selected number of results
num_results_label = tk.Label(frame, text="Number of Results:")  # Create a label for the number of results dropdown
num_results_label.grid(row=2, column=1, padx=5)  # Place the label in the grid
num_results_menu = ttk.Combobox(frame, textvariable=num_results_var, values=["All", "10", "20", "50", "100"])  # Create the number of results dropdown
num_results_menu.grid(row=2, column=2, padx=5)  # Place the dropdown in the grid

# Function to filter data based on user input
def filter_data():
    category = category_var.get()  # Get the selected category
    sort_actual_price = actual_price_var.get().lower()  # Get the selected actual price sorting option
    sort_discounted_price = discounted_price_var.get().lower()  # Get the selected discounted price sorting option
    sort_discount_percentage = discount_percentage_var.get().lower()  # Get the selected discount percentage sorting option
    num_results = num_results_var.get()  # Get the selected number of results

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
    output_text.delete(1.0, tk.END)  # Clear the output text box
    if filtered_data.empty:  # Check if the filtered data is empty
        messagebox.showerror("Error", "No results match your filters.")  # Show an error message 
        output_text.insert(tk.END, "No results match your filters.\n")  # Display a message if no results match
    else:
        # Format headers with bold styling and spacing
        headers = "  ".join([f"{col:^20}" for col in filtered_data.columns])  # Format the headers
        output_text.insert(tk.END, headers + "\n")  # Insert the headers into the text box
        output_text.insert(tk.END, "-" * len(headers) + "\n\n")  # Add a separator and line gap
        messagebox.showinfo("Done","Result is ready")

        # Format each row with equal spacing
        for _, row in filtered_data.iterrows():  # Iterate through the filtered data rows
            row_str = "  ".join([f"{str(value):^20}" for value in row])  # Format each row
            output_text.insert(tk.END, row_str + "\n")  # Insert the row into the text box

# Button to apply filter
filter_button = tk.Button(root, text="Apply Filter", command=filter_data)  # Create a button to apply the filter
filter_button.pack(pady=10)  # Add padding around the button

# Output display
output_text = tk.Text(root, wrap=tk.WORD, width=110, height=20)  # Create a text box to display the output
output_text.pack(pady=10)  # Add padding around the text box

root.mainloop()  # Run the main loop to display the window
