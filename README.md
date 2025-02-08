# Smart Book Assistant 📚❓

A **Small Language Model (SLM)** that answers questions based on a book or text. Built with Python, Hugging Face Transformers, and FAISS, this project is designed to help you extract information from large texts quickly and accurately.

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

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
7. [License](#license-)

---

## Quick Start 🚀

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/Book-QA-SLM.git
cd Book-QA-SLM
