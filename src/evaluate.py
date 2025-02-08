import json
from main import BookQA


def evaluate(test_file="test_questions.json"):
    with open(test_file) as f:
        test_data = json.load(f)

    qa_system = BookQA("book.txt")
    results = []

    for item in test_data:
        answer = qa_system.ask_question(item['question'])
        results.append({
            'question': item['question'],
            'expected': item['answer'],
            'predicted': answer
        })

    # Calculate accuracy
    exact_matches = sum(1 for r in results if r['expected'].lower() in r['predicted'].lower())
    print(f"Exact Match Accuracy: {exact_matches / len(results) * 100:.2f}%")
    return results


evaluate()
