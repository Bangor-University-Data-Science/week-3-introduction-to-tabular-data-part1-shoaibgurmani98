import pandas as pd

def get_numerical_df(df, numerical_features):
    # Filter the DataFrame
    numerical_df = df[numerical_features].copy()
    return numerical_df

# Test function execution and output
if __name__ == "__main__":
    filepath = "data/titanic.csv" 
    titanic_data = pd.read_csv(filepath)
    numerical_features = ['Age', 'Fare']
    numerical_df = get_numerical_df(titanic_data, numerical_features)
