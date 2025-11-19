# 📚 Book Price Prediction API (FastAPI + ML)

A lightweight machine learning microservice that suggests book prices based on metadata such as page count, genre, author popularity, and release year. Built with FastAPI and a custom-trained linear regression model using scikit-learn.

Part of a larger **Book Inventory System** with microservices built using React, Spring Boot, RabbitMQ, and Python.

---

## 🚀 Features

- Predicts a suggested price based on book metadata
- Trained ML model using scikit-learn (Linear Regression)
- Exposes a simple REST API using FastAPI
- Designed for integration with frontend (React) and backend (Spring Boot)

---

## 🧱 Tech Stack

- **Python 3.9+**
- **FastAPI** — for REST API
- **scikit-learn** — for training the ML model
- **pandas, numpy** — for data preprocessing
- **joblib** — for model persistence

---

## 🧪 How it Works

1. Trains a regression model using a sample dataset (`Books.csv`) with features like:
   - `pageCount`, `releasedYear`, and `author popularity`
2. Serves predictions via a FastAPI endpoint:
   - `/predict_price` – POST request with book features
3. Returns a `suggested_price` based on the trained model.

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
- Add support for additional languages and genres
- Explore more advanced models (e.g., Random Forest or NLP-based regressors) for better pricing predictions
- NLP-powered chatbot assistant to help users: Ask questions like "Show me books under $10 by Dan Brown"
- Semantic and fuzzy search using NLP techniques (e.g., tokenization, vector similarity). Enable partial matching, typo tolerance, and contextual understanding in search



