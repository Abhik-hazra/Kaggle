def dataframe_details(df):
    """
    Function to display details of a pandas DataFrame.
    
    Parameters:
        df (DataFrame): The DataFrame for which details are to be displayed.
        
    Returns:
        None
    """
    print("Details of the dataframe: ")
    print("-"*20)
    # Display shape of the DataFrame
    print("DataFrame Shape:")
    print(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")
    print("-" * 20)
    
    # Display column names
    print("Column Names:")
    for col in df.columns:
        print(col)
    print("-" * 20)
    
    # Display null values of each column
    print("Null Values:")
    null_counts = df.isnull().sum()
    if null_counts.sum() == 0:
        print("No null values found.")
    else:
        for col, null_count in null_counts.items():
            if null_count > 0:
                print(f"{col}: {null_count} null values")
    print("-" * 20)
    
    # Display data types of each column
    print("Data Types:")
    print(df.dtypes)
    print("-" * 20)
