import os
import pandas as pd

def run_analysis():
    # Print current directory contents for debugging
    print("Current Directory:", os.getcwd())
    print("Directory Contents:", os.listdir('.'))

    # Load data
    data = pd.read_csv('./sample.csv')
    
    # Perform analysis (e.g., calculate mean)
    mean_value = data['value'].mean()

    return {'mean': mean_value}
