"""
generate_questions.py

Utility script to sample questions and answers fronm TruthfulQA dataset.
"""

import csv
import random

INPUT_PATH = "../data/TruthfulQA.csv"
QUESTIONS_OUTPUT = "../data/questions.csv"
ANSWERS_OUTPUT = "../data/answers.csv"
NUM_QUESTIONS = 30

def sample_questions(input_path, num_questions):
    qa_pairs = []
    with open(input_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter=',')
        for row in reader:
            question_text = row.get("Question", "").strip()
            answer_text = row.get("Best Answer", "").strip()
            if question_text and answer_text:
                qa_pairs.append({"question": question_text, "answer": answer_text})
    sampled = random.sample(qa_pairs, min(num_questions, len(qa_pairs)))
    return sampled

def save_questions_to_csv(sampled_qa, output_path):
    with open(output_path, "w", newline='', encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["question"])
        writer.writeheader()
        for item in sampled_qa:
            writer.writerow({"question": item["question"]})

def save_answers_to_csv(sampled_qa, output_path):
    with open(output_path, "w", newline='', encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["question", "answer"])
        writer.writeheader()
        for item in sampled_qa:
            writer.writerow(item)

def main():
    sampled_qa = sample_questions(INPUT_PATH, NUM_QUESTIONS)
    save_questions_to_csv(sampled_qa, QUESTIONS_OUTPUT)
    save_answers_to_csv(sampled_qa, ANSWERS_OUTPUT)
    print(f"Sampled {len(sampled_qa)} questions saved to {QUESTIONS_OUTPUT}")
    print(f"Corresponding answers saved to {ANSWERS_OUTPUT}")

if __name__ == "__main__":
    main()