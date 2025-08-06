from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct, VectorParams, Distance
from sentence_transformers import SentenceTransformer
import json

# Initialize FastAPI app
app = FastAPI()

# Enable CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load schema from JSON
with open("/app/schema.json", "r") as f:
    schema_data = json.load(f)

# Initialize Sentence Transformers model
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

# Connect to Qdrant
qdrant_client = QdrantClient(host="qdrant", port=6333)

# Create or Recreate the collection
qdrant_client.recreate_collection(
    collection_name="tables",
    vectors_config=VectorParams(size=384, distance=Distance.COSINE)
)

# Function to generate embeddings and insert them into Qdrant
def insert_table_embeddings():
    vectors = []
    for idx, table in enumerate(schema_data):
        text_representation = f"Table: {table['table_name']}, Columns: {', '.join(table['columns'])}"
        embedding = embedding_model.encode(text_representation).tolist()
        vectors.append(PointStruct(id=idx, vector=embedding, payload=table))
    
    qdrant_client.upsert(collection_name="tables", points=vectors)
    print("✅ Schema stored in Qdrant!")

insert_table_embeddings()

# API to handle table retrieval based on a query
@app.post("/retrieve-tables/")
async def retrieve_tables(request: Request):
    body = await request.json()
    query_description = body.get("description", "")
    
    query_embedding = embedding_model.encode(query_description).tolist()
    
    results = qdrant_client.search(
        collection_name="tables",
        query_vector=query_embedding,
        limit=3
    )
    
    return {"tables": [result.payload for result in results]}
