import csv
import pandas as pd
import numpy as np

def find_s_algorithm(csv_file):
    # Read data
    print(f"Loading dataset from {csv_file}...")
    df = pd.read_csv(csv_file)
    print("Dataset:")
    print(df)
    
    # Assuming the last column is the target
    target_col = df.columns[-1]
    features = np.array(df.iloc[:, :-1])
    target = np.array(df[target_col])
    
    print("\nStarting FIND-S Algorithm...")
    # Initialize the hypothesis to the most specific possible
    # We find the first positive example to initialize it correctly
    hypothesis = None
    for i, val in enumerate(target):
        if str(val).strip().lower() == 'yes':
            hypothesis = features[i].copy()
            break
            
    if hypothesis is None:
        print("No positive examples found in the dataset.")
        return
        
    print(f"Initial Hypothesis: {hypothesis}")
    
    # Iterate through the rows
    for i, row in enumerate(features):
        if str(target[i]).strip().lower() == 'yes':
            for j in range(len(hypothesis)):
                if row[j] != hypothesis[j]:
                    hypothesis[j] = '?'
            print(f"Hypothesis after positive example {i+1}: {hypothesis}")
        else:
            print(f"Example {i+1} is negative. Hypothesis remains unchanged: {hypothesis}")
            
    print("\nFinal Learned Hypothesis:")
    print(hypothesis)
    
    # Save the hypothesis mapping to a json file
    import json
    with open('hypothesis.json', 'w') as f:
        json.dump(list(hypothesis), f)
    print("Hypothesis saved to hypothesis.json")

if __name__ == '__main__':
    find_s_algorithm('EnjoySport.csv')
