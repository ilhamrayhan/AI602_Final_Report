# analyze_results.py

import os
import pandas as pd

def analyze_results(file_path):
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return

    df = pd.read_csv(file_path)
    print(f"\nSummary for {file_path}:")

    if 'judge_decision' in df.columns:
        df['judge_decision'] = df['judge_decision'].str.strip().str.lower()
        decision_counts = df['judge_decision'].value_counts()
        print("Judge Decisions:")
        print(decision_counts)
    else:
        print("No 'judge_decision' column found in this file.")

    if 'elo_score_first' in df.columns and 'elo_score_second' in df.columns:
        avg_first = df['elo_score_first'].mean()
        avg_second = df['elo_score_second'].mean()
        print(f"Average Elo Score (First Speaker): {avg_first:.2f}")
        print(f"Average Elo Score (Second Speaker): {avg_second:.2f}")
    else:
        print("No Elo score columns found in this file.")

def main():
    results_dir = "../results"
    files = [
        "consultancy_results.csv",
        "debate_results.csv",
        "improvement_results.csv"
    ]

    for filename in files:
        file_path = os.path.join(results_dir, filename)
        analyze_results(file_path)

if __name__ == "__main__":
    main()
