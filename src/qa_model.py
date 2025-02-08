from transformers import pipeline


class QAModel:
    def __init__(self):
        self.model = pipeline(
            "question-answering",
            model="distilbert-base-cased-distilled-squad"
        )

    def answer_question(self, question, context):
        result = self.model(question=question, context=context)
        return result['answer']
