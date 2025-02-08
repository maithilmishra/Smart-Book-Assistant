import json
from preprocess import TextPreprocessor
from retrieval import VectorRetriever
from qa_model import QAModel


class BookQA:
    def __init__(self, book_path):
        self.book_path = book_path
        self.preprocessor = TextPreprocessor()
        self.retriever = VectorRetriever()
        self.qa_model = QAModel()

        self._prepare_book()

    def _prepare_book(self):
        with open(self.book_path, 'r', encoding='utf-8') as f:
            text = f.read()

        cleaned_text = self.preprocessor.clean_text(text)
        self.chunks = self.preprocessor.chunk_text(cleaned_text)
        embeddings = self.preprocessor.get_embeddings(self.chunks)

        self.retriever.chunks = self.chunks
        self.retriever.build_index(embeddings)

    def ask_question(self, question):
        question_embedding = self.preprocessor.embedding_model.encode([question])

        context_chunks = self.retriever.retrieve(question_embedding)
        context = ' '.join(context_chunks)

        return self.qa_model.answer_question(question, context)


def load_test_questions(test_file):
    with open(test_file, 'r') as f:
        return json.load(f)


def main():
    qa_system = BookQA("book.txt")

    test_questions = load_test_questions("test_questions.json")

    print("Available Questions:")
    for i, item in enumerate(test_questions):
        print(f"{i}: {item['question']}")

    try:
        index = int(input("Enter the index of the question you want to ask: "))
        if index < 0 or index >= len(test_questions):
            print("Invalid index. Please enter a valid index.")
            return

        question = test_questions[index]['question']
        print(f"\nQuestion: {question}")

        answer = qa_system.ask_question(question)
        print(f"Answer: {answer}")

    except ValueError:
        print("Invalid input. Please enter a valid integer index.")


if __name__ == "__main__":
    main()
