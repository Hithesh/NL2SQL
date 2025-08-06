# NL2SQL
This project uses AI (via Sentence Transformers) and a vector database (Qdrant) to retrieve the most relevant database tables based on a user's natural language input.

#Objective
To build a system that dynamically analyzes natural language queries and returns the most relevant subset of database tables using semantic similarity.

#Tech Stack Used
Backend: FastAPI (Python)
AI Model: Sentence Transformers (all-MiniLM-L6-v2)
Vector Database: Qdrant
Frontend: React.js (with plain CSS)
Containerization: Docker & Docker Compose
Data Format: JSON schema

#Features
Accepts a natural language description from the user.
Converts both the schema and user query to vector embeddings.
Uses Qdrant to store and retrieve table embeddings based on similarity.
Returns relevant table names and columns in JSON format.
Frontend UI built using React for easy interaction.

#Folder Structure
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





