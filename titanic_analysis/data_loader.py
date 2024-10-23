import pandas as pd

def load_titanic_data(filepath: str) -> pd.DataFrame:
    df = pd.read_csv(filepath)
    return df

# Test function execution
if __name__ == "__main__":
    filepath = "data/titanic.csv"  
    titanic_data = load_titanic_data(filepath)

