import pandas as pd

# Function to load CSV file into a DataFrame
def load_csv(file_path="sales_data.csv"):
    return pd.read_csv(file_path)

# Function to filter the DataFrame based on user input
def filter_dataframe(df):
    # Take user inputs
    num_results = int(input("\nHow many results would you like to display? (5, 10, 50, 100): "))
    
    # Show available categories
    unique_categories = df['Category'].dropna().unique()
    print("\nAvailable Categories:")
    for category in unique_categories:
        print(f"- {category}")

    
    category = input("Enter category (Leave blank for no category filter): ").strip()

    # Process the DataFrame
    df = df.dropna()

    # Apply category filter if provided
    if category:
        df = df[df['Category'].str.contains(category, case=False, na=False)]


    sort_discounted_price = input("Sort by discounted price (ascending/descending/blank): ").strip().lower()
    if sort_discounted_price == "ascending":
        df = df.sort_values(by="Discounted Price", ascending=True)
    elif sort_discounted_price == "descending":
        df = df.sort_values(by="Discounted Price", ascending=False)


    sort_price = input("Sort by price (ascending/descending/blank): ").strip().lower()
    if sort_price == "ascending":
        df = df.sort_values(by="Price", ascending=True)
    elif sort_price == "descending":
        df = df.sort_values(by="Price", ascending=False)

    sort_discount_percentage = input("Sort by discount percentage (ascending/descending/blank): ").strip().lower()
    if sort_discount_percentage == "ascending":
        df = df.sort_values(by="Discount Percentage", ascending=True)
    elif sort_discount_percentage == "descending":
        df = df.sort_values(by="Discount Percentage", ascending=False)

    # Return the top 'num_results' rows
    return df.head(num_results)

# Main function to load CSV, apply filters, and show results
def main():
    try:
        df = load_csv()
    except FileNotFoundError:
        print("Error: CSV file not found.")
        return

    # Filter and display the DataFrame based on user input
    filtered_df = filter_dataframe(df)
    if filtered_df.empty:
        print("No results match your filters.")
    else:
        print("\nFiltered results:")
        print(filtered_df)

if __name__ == "__main__":
    main()
