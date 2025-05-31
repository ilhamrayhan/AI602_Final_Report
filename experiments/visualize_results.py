# visualize_results.py

import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def load_results(file_path):
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return None

    df = pd.read_csv(file_path)

    # Mock judge decisions and Elo scores if USE_MOCK is set
    if os.environ.get('USE_MOCK', '').lower() == 'true':
        np.random.seed(42)
        n_rows = len(df)
        df['judge_decision'] = np.random.choice(['answer 1', 'answer 2'], size=n_rows)
        df['elo_score_first'] = np.random.uniform(1200, 1600, size=n_rows)
        df['elo_score_second'] = np.random.uniform(1200, 1600, size=n_rows)

    return df

def plot_decision_counts(df, title, output_file):
    if 'judge_decision' not in df.columns:
        print(f"No 'judge_decision' column found in the dataset: {output_file}")
        return

    df['judge_decision'] = df['judge_decision'].str.strip().str.lower()
    counts = df['judge_decision'].value_counts()
    counts = counts.reindex(['answer 1', 'answer 2'], fill_value=0)

    print(f"Counts for {title}:")
    print(counts)

    counts.plot(kind='bar', color=['#66c2a5', '#fc8d62'])
    plt.title(f"{title} - Judge Decisions")
    plt.ylabel('Count')
    plt.xlabel('Decision')
    plt.ylim(0, max(counts.max() * 1.2, 1))
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.savefig(output_file)
    print(f"Plot saved to {output_file}")
    plt.close()

def plot_elo_scores(df, title, output_file):
    if 'elo_score_first' not in df.columns or 'elo_score_second' not in df.columns:
        print(f"No Elo score columns found in the dataset: {output_file}")
        return

    avg_first = df['elo_score_first'].mean()
    avg_second = df['elo_score_second'].mean()

    labels = ['First Speaker', 'Second Speaker']
    scores = [avg_first, avg_second]

    plt.bar(labels, scores, color=['#8da0cb', '#fc8d62'])
    plt.title(f"{title} - Average Elo Scores")
    plt.ylabel('Average Elo Score')
    plt.ylim(1100, 1700)
    plt.tight_layout()
    plt.savefig(output_file)
    print(f"Plot saved to {output_file}")
    plt.close()

def main():
    results_dir = "../results"
    files = [
        ("consultancy_results.csv", "Consultancy Results"),
        ("debate_results.csv", "Debate Results"),
        ("improvement_results.csv", "Improved Debate Results")
    ]

    for filename, title in files:
        file_path = os.path.join(results_dir, filename)
        df = load_results(file_path)
        if df is not None:
            decision_output = os.path.join(results_dir, f"{filename.replace('.csv', '_decisions_plot.png')}")
            plot_decision_counts(df, title, decision_output)

            elo_output = os.path.join(results_dir, f"{filename.replace('.csv', '_elo_plot.png')}")
            plot_elo_scores(df, title, elo_output)

if __name__ == "__main__":
    main()
