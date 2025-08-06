# AI-Based Table Retriever Using Natural Language and Sentence Transformers

This project uses AI (via Sentence Transformers) and a vector database (Qdrant) to retrieve the most relevant database tables based on a user's natural language input.

##  Objective

To build a system that dynamically analyzes natural language queries and returns the most relevant subset of database tables using semantic similarity.

##  Tech Stack Used

* **Backend:** FastAPI (Python)
* **AI Model:** Sentence Transformers (all-MiniLM-L6-v2)
* **Vector Database:** Qdrant
* **Frontend:** React.js (with plain CSS)
* **Containerization:** Docker & Docker Compose
* **Data Format:** JSON schema

##  Features

* Accepts a natural language description from the user
* Converts both the schema and user query to vector embeddings
* Uses Qdrant to store and retrieve table embeddings based on similarity
* Returns relevant table names and columns in JSON format
* Frontend UI built using React for easy interaction

##  Folder Structure

```bash
project-root/
├── backend/
│   ├── app.py
│   ├── schema.json
│   ├── requirements.txt
├── frontend/
│   ├── public/
│   ├── src/
│   │   └── App.js
│   ├── package.json
│   ├── Dockerfile
├── docker-compose.yml
├── README.md
```

## 📥 Installation & Setup

### 1. Clone the repository:

```bash
git clone https://github.com/your-username/ai-table-retriever.git
cd ai-table-retriever
```

### 2. Start Docker (Required for Qdrant and FastAPI):

Make sure Docker Desktop is running and Linux containers are enabled.

### 3. Build and start the containers:

```bash
docker-compose build
docker-compose up
```

### 4. Backend will be available at:

```
http://localhost:8000
```

Frontend (optional) will be available at:

```
http://localhost:3000
```

##  Sample Input (JSON)

POST to `http://localhost:8000/retrieve-tables/` with:

```json
{
  "description": "I want to see customer names and their purchases"
}
```

##  Sample Output (JSON)

```json
{
  "tables": [
    {
      "table_name": "customers",
      "columns": ["customer_id", "name", "age", "location"]
    },
    {
      "table_name": "purchases",
      "columns": ["purchase_id", "customer_id", "product", "amount"]
    }
  ]
}
```

## 📁 schema.json (Sample)

```json
[
  {
    "table_name": "customers",
    "columns": ["customer_id", "name", "age", "location"]
  },
  {
    "table_name": "purchases",
    "columns": ["purchase_id", "customer_id", "product", "amount"]
  },
  {
    "table_name": "products",
    "columns": ["product_id", "product_name", "category"]
  }
]
```

## ✅ Requirements

Inside `backend/requirements.txt`:

```txt
fastapi
uvicorn
sentence-transformers
qdrant-client
```

## 🧐 AI Model Used

* `all-MiniLM-L6-v2` by Sentence Transformers (open-source, no API key needed)

## 🔐 CORS Enabled for Frontend Integration

* Cross-origin requests are allowed from any origin for simplicity.

## 🧪 Testing

* Use Postman or any REST client to test the `/retrieve-tables/` POST route.
* The React frontend is optional but helpful for testing.

## 📅 Troubleshooting

* Make sure Docker is running
* Ensure `schema.json` is located inside the backend folder
* If Qdrant is not connecting, check port 6333 is open
* Use `docker logs backend` to debug FastAPI container

## 📄 License

This project is open-source and free to use for educational and demo purposes.
