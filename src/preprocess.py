import re
import nltk
from nltk.tokenize import sent_tokenize
from sentence_transformers import SentenceTransformer

nltk.download('punkt_tab')


class TextPreprocessor:
    def __init__(self, chunk_size=300):
        self.chunk_size = chunk_size
        self.embedding_model = SentenceTransformer('all-MiniLM-L6-v2')

    def clean_text(self, text):
        text = re.sub(r'\s+', ' ', text)  # Remove extra whitespace
        text = re.sub(r'[^a-zA-Z0-9.,!? ]', '', text)  # Remove special chars
        return text

    def chunk_text(self, text):
        sentences = sent_tokenize(text)
        chunks = []
        current_chunk = []

        for sentence in sentences:
            if len(current_chunk) + len(sentence.split()) <= self.chunk_size:
                current_chunk.append(sentence)
            else:
                chunks.append(' '.join(current_chunk))
                current_chunk = [sentence]
        if current_chunk:
            chunks.append(' '.join(current_chunk))
        return chunks

    def get_embeddings(self, chunks):
        return self.embedding_model.encode(chunks)