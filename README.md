# 📚 Book Pricing & Semantic Search Microservice (FastAPI + ML)

A lightweight machine learning + semantic search microservice that powers intelligent features for the Book Inventory System.
This service suggests book prices based on metadata (page count, genre, author popularity, release year) and provides semantic similarity search using SentenceTransformers.

It also includes:

In-memory caching for faster repeated predictions/searches

RabbitMQ consumer for background event processing (e.g., syncing metadata, reacting to low-stock events)

This service is part of a larger distributed system built with React (UI), Spring Boot (Core Backend), RabbitMQ (messaging), and Python (AI/NLP).
---

## 🚀 Features

ML-Powered Price Prediction
  - Predicts a suggested price for a book based on structured metadata
  - Custom-trained Linear Regression model (scikit-learn)
  - Exposes a POST /predict_price FastAPI endpoint

Semantic Search
   - Uses SentenceTransformers to generate embeddings for book data
   - Supports semantic similarity queries (e.g., “books about wizard schools”, “mystery novels with detectives”)
   - Exposes a POST /semantic_search_books endpoint for vector-based search
   - Provides more intelligent results than keyword matching

In-Memory Caching
  - Caches book data and frequently queried embeddings
  - Significantly improves latency for repeated requests

RabbitMQ Background Consumer
  - Continuously listens for messages from Spring Boot services
  - Syncs book metadata updates (title, description, genre) for semantic embedding refresh
  - Designed for distributed, event-driven workflows
---

## 🧱 Tech Stack

- **Python 3.9+**
- **FastAPI** — for REST API
- **scikit-learn** — for training the ML model
- **pandas, numpy** — for data preprocessing
- **joblib** — for model persistence
- **RabbitMQ + pika** — message consumer

---

## 🧪 How it Works
1. Price Prediction Pipeline
   - Trains a regression model using a sample dataset (`Books.csv`) with features like:`pageCount`, `releasedYear`, and `author popularity`
   - Serves predictions via a FastAPI endpoint: `/predict_price` – POST request with book features
2. Semantic Search Workflow
   - Generate embeddings using SentenceTransformers
   - Store vectors in memory for fast similarity lookup
   - On new book events (via RabbitMQ), embeddings auto-refresh
3. Event driven
   - A RabbitMQ consumer runs in the background.
   - Listens for book.added / book.updated / book.deleted events
   - Rebuilds embeddings for semantic search keeping Python and Java in sync about the book data.
---

## 📦 Setup Instructions
### 1. Clone the repo

```bash
git clone https://github.com/yourusername/book-pricing-service.git
cd book-pricing-service
```
### 2. Create Virtual environment
```
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

### 3. Install dependencies
``` pip install -r requirements.txt ```

### 4. Train the model
``` python train_model.py ```

### 5. Start the API server
``` uvicorn main:app --reload ```

## API Usage 
Endpoint: POST /predict_price
Request Body:
```
{
  "pageCount": 350,
  "releasedYear": 2007,
  "author": "JK Rowling",
  "genre": "Fantasy"
}
```

Response:
```
{
  "suggested_price": 14.87
}
```

End point : POST /semantic_search_books
Request Body: 
```
{
  "query": "magic school adventure",
}
```

Response:
```
{
   [
    { "title": "...", "score": 0.82 },
    { "title": "...", "score": 0.79 }
  ]
}

```

---

## Connected Repos 
🔗 Spring Boot Backend Repository

The backend API for Book Inventory CRUD Operations and many more is built using Spring Boot and can be found here:

👉 [Spring Boot Book Inventory API] https://github.com/divyaviz1511/book-inventory-api

🔗 React Front Repository

The Frontend for Book Inventory is built using React/Bootstrap with Axios :

👉  [React Book Inventory UI] https://github.com/divyaviz1511/bookstore-ui-react



## 🧠 Future Enhancements

- Use real-world datasets (Google Books API, Goodreads)
- Explore more advanced models (e.g., Random Forest or NLP-based regressors) for better pricing predictions
- SentenceTransformer fine-tuning based on book categories
- Full-text + embedding hybrid search
- NLP-powered assistant (Q&A, recommendations, keyword extraction)



