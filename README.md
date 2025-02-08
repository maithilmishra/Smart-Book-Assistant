# Smart Book Assistant 📚❓

A **Small Language Model (SLM)** that answers questions based on a book or text. Built with Python, Hugging Face Transformers, and FAISS, this project is designed to help you extract information from large texts quickly and accurately.

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)

---

## Features ✨
- **Preprocess** books into clean, manageable chunks.
- **Retrieve** relevant text using semantic search (FAISS).
- **Answer questions** using DistilBERT (Hugging Face).
- **Evaluate** accuracy with Exact Match (EM) and F1 scores.

---

## Table of Contents 📑
1. [Quick Start](#quick-start-)
2. [How to Use the Model](#how-to-use-the-model-)
3. [Project Structure](#project-structure-)
4. [Documentation](#documentation-)
   - [Approach](#approach)
   - [Model Architecture](#model-architecture)
   - [Preprocessing Techniques](#preprocessing-techniques)
   - [Evaluation](#evaluation)
5. [Key Learnings](#key-learnings-)
6. [Future Improvements](#future-improvements-)

---

## Quick Start 🚀

### 1. Clone the Repository
```bash
git clone https://github.com/maithilmishra/Smart-Book-Assistant.git
cd Smart-Book-Assistant
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Prepare Your Data
. Add your book text to book.txt.
. Add test questions to test_questions.json (example below).

### 4. Run the System
```bash
# Interactive mode (ask questions by index)
python -m src.main

# Evaluate accuracy
python -m src.evaluate
```

## How to Use the Model 🖥️
### Step 1: Add Your Book
 - Place your book text in book.txt.
   Example:
   ```txt
   In the small town of Willow Creek, there lived a brilliant scientist named Professor Waldo...
   ```
### Step 2: Add Test Questions
 1. Add questions and answers to test_questions.json.
    Example:
    ```json
    [
       {
         "question": "Who discovered the secret formula?",
         "answer": "Professor Waldo" 
       }
    ]
    ```
### Step 3: Run the System
   1. Interactive Mode:
   ```bash
   python -m src.main
   ```
   - The system will display available questions.
   - Enter the index of the question you want to ask.

   2. Evaluation Mode:
   ```bash
   python -m src.evaluate
   ```
   - This will test the system’s accuracy on the questions in test_questions.json.
## Project Structure 🗂️
```
Smart-Book-Assistant/   
├── src/
│   ├── preprocess.py          # Text cleaning/chunking
│   ├── retrieval.py           # FAISS-based retrieval
│   ├── qa_model.py            # Answer generation
│   ├── main.py                # Interactive pipeline
│   |── evaluate.py            # Accuracy testing
|   ├── book.txt               # Your input book text
|   └── test_questions.json    # Test questions/answers
├── requirements.txt           # Dependencies
├── README.md                  # Project documentation
```
## Observations 🔍
### What Worked Well ✅
 - Chunking Strategy:
      -- Breaking the book into smaller sections (e.g., paragraphs) improved answer precision.
      -- Larger chunks made it harder to find specific information.

 - FAISS for Retrieval:
      -- FAISS was incredibly fast at finding relevant chunks, even for large books.
      -- Semantic search worked better than keyword-based approaches.

 - DistilBERT for Answers:
      -- The pre-trained model provided accurate answers for straightforward questions.
      -- Fine-tuning on SQuAD made it well-suited for question answering.

### Challenges ❌
 - Ambiguous Questions:
      -- The system struggled with questions requiring context across multiple chunks.
      -- Example: "Why did the protagonist leave the city?" often resulted in incomplete answers.

 - Long Answers:
      -- For questions with detailed answers, the system sometimes misses key details.

 - Preprocessing:
      -- Cleaning and chunking the text required careful tuning to ensure optimal performance.

### Insights 💡
 - Trade-offs:
      -- Smaller models (like DistilBERT) are faster but may sacrifice some accuracy compared to larger models.
      -- Balancing chunk size and retrieval accuracy is critical.

 - Evaluation:
      -- Metrics like Exact Match (EM) and F1 Score provided a good baseline, but human review was essential for identifying edge cases.

## Key Learnings 🔑
   - Smaller text chunks improve answer precision.
   - FAISS enables fast retrieval even for large books.
   - Trade-offs exist between model size (speed) and accuracy.

## Future Improvements 🚀
   - Multi-Hop Reasoning: Answer questions requiring information from multiple chunks.
   - User Interface: Build a web or mobile app for easier interaction.
   - Larger Models: Experiment with larger models (e.g., BERT-large) for better accuracy.

## Contributors 👥
   - [Maithil Mishra](https://github.com/maithilmishra)

