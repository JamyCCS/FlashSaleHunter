import pandas as pd

# Function to load CSV file into a DataFrame
def load_csv(file_path="sales_data.csv"):
    try:
        return pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"Error: File {file_path} not found.")
        return pd.DataFrame()

# Function to get unique categories from the DataFrame
def get_unique_categories(data):
    if not data.empty and "Category" in data.columns:
        return data["Category"].dropna().unique().tolist()
    return []

# Function to filter the DataFrame based on user input
def filter_dataframe(data, category="All", sort_actual_price="none", sort_discounted_price="none", sort_discount_percentage="none", num_results=10):
    if data.empty:
        print("No data available.")
        return pd.DataFrame()

    # Filter by category
    if category != "All":
        data = data[data["Category"].str.contains(category, case=False, na=False)]

    # Define sorting priorities
    sort_columns = []
    sort_ascending = []

    if sort_actual_price == "ascending":
        sort_columns.append("Price")
        sort_ascending.append(True)
    elif sort_actual_price == "descending":
        sort_columns.append("Price")
        sort_ascending.append(False)

    if sort_discounted_price == "ascending":
        sort_columns.append("Discounted Price")
        sort_ascending.append(True)
    elif sort_discounted_price == "descending":
        sort_columns.append("Discounted Price")
        sort_ascending.append(False)

    if sort_discount_percentage == "ascending":
        sort_columns.append("Discount Percentage")
        sort_ascending.append(True)
    elif sort_discount_percentage == "descending":
        sort_columns.append("Discount Percentage")
        sort_ascending.append(False)

    # Apply sorting based on multiple criteria
    if sort_columns:
        data = data.sort_values(by=sort_columns, ascending=sort_ascending)

    # Return the top 'num_results' rows
    return data.head(num_results)
