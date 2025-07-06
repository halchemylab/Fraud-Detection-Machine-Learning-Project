import pandas as pd

def get_average_transaction_values(csv_path, nrows=10000):
    # Only load a sample for performance
    df = pd.read_csv(csv_path, nrows=nrows)
    # Only use relevant columns
    cols = ['amount', 'oldbalanceOrg', 'newbalanceOrig', 'oldbalanceDest', 'newbalanceDest']
    avg = df[cols].mean().to_dict()
    return avg
