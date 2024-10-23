import pandas as pd

def create_feature_type_dict(df):
    feature_types = {}

    for column in df.columns:
        if pd.api.types.is_numeric_dtype(df[column]):
            if 'numerical' not in feature_types:
                feature_types['numerical'] = {'continuous': [], 'discrete': []}
                
            if len(df[column].unique()) > 20: 
                feature_types['numerical']['continuous'].append(column)
            else:
                feature_types['numerical']['discrete'].append(column)
        elif pd.api.types.is_categorical_dtype(df[column]) or df[column].dtype == 'object':
            
            if 'categorical' not in feature_types:
                feature_types['categorical'] = {'nominal': [], 'ordinal': []}
                
            if column in ['Pclass', 'Sex']:  
                feature_types['categorical']['ordinal'].append(column)
            else:
                feature_types['categorical']['nominal'].append(column)

    return feature_types

# Test function execution and output
if __name__ == "__main__":
    filepath = "data/titanic.csv" 
    titanic_data = pd.read_csv(filepath)
    feature_type_dict = create_feature_type_dict(titanic_data)
