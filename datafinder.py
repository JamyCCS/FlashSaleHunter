import pandas as pd  # Import the pandas library to work with data

# Function to load CSV file into a DataFrame
def load_csv(file_path="sales_data.csv"):
    try:
        return pd.read_csv(file_path)  # Try to read the CSV file and return it as a DataFrame
    except FileNotFoundError:
        return pd.DataFrame()  # Return an empty DataFrame if the file is not found

# Function to get unique categories from the DataFrame
def get_unique_categories(data):
    if not data.empty and "Category" in data.columns:  # Check if the DataFrame is not empty and has a "Category" column
        return data["Category"].dropna().unique().tolist()  # Get unique categories, remove missing values, and convert to a list
    return []  # Return an empty list if conditions are not met

# Function to filter the DataFrame based on user input
def filter_dataframe(data, category="All", sort_actual_price="none", sort_discounted_price="none", sort_discount_percentage="none", num_results="10"):
    if data.empty:  # Check if the DataFrame is empty
        return pd.DataFrame()  # Return an empty DataFrame if no data is available

    # Filter by category
    if category != "All":  # Check if the category is not "All"
        data = data[data["Category"].str.contains(category, case=False, na=False)]  # Filter data by category, ignoring case

    # Define sorting priorities
    sort_columns = []  # List to hold columns to sort by
    sort_ascending = []  # List to hold sorting order (True for ascending, False for descending)

    if sort_actual_price == "ascending":  # Check if sorting by actual price in ascending order
        sort_columns.append("Price")  # Add "Price" column to sort columns
        sort_ascending.append(True)  # Add True to sort ascending list
    elif sort_actual_price == "descending":  # Check if sorting by actual price in descending order
        sort_columns.append("Price")  # Add "Price" column to sort columns
        sort_ascending.append(False)  # Add False to sort ascending list

    if sort_discounted_price == "ascending":  # Check if sorting by discounted price in ascending order
        sort_columns.append("Discounted Price")  # Add "Discounted Price" column to sort columns
        sort_ascending.append(True)  # Add True to sort ascending list
    elif sort_discounted_price == "descending":  # Check if sorting by discounted price in descending order
        sort_columns.append("Discounted Price")  # Add "Discounted Price" column to sort columns
        sort_ascending.append(False)  # Add False to sort ascending list

    if sort_discount_percentage == "ascending":  # Check if sorting by discount percentage in ascending order
        sort_columns.append("Discount Percentage")  # Add "Discount Percentage" column to sort columns
        sort_ascending.append(True)  # Add True to sort ascending list
    elif sort_discount_percentage == "descending":  # Check if sorting by discount percentage in descending order
        sort_columns.append("Discount Percentage")  # Add "Discount Percentage" column to sort columns
        sort_ascending.append(False)  # Add False to sort ascending list

    # Apply sorting based on multiple criteria
    if sort_columns:  # Check if there are columns to sort by
        data = data.sort_values(by=sort_columns, ascending=sort_ascending)  # Sort data by specified columns and order

    # Apply the number of results filter
    if num_results != "All":  # Check if the number of results is not "All"
        data = data.head(int(num_results))  # Get the top 'num_results' rows from the data

    return data  # Return the filtered and sorted data
