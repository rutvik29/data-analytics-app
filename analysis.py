

import pandas as pd

def run_analysis():
    # Load data
    data = pd.read_csv('./sample.csv')
    
    # Perform analysis (e.g., calculate mean)
    mean_value = data['value'].mean()

    return {'mean': mean_value}
