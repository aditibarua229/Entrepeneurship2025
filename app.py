from flask import Flask, request, jsonify
import os
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.preprocessing import normalize
import faiss

app = Flask(__name__)

model = SentenceTransformer("all-MiniLM-L6-v2")

def read_files_to_array(directory):
    file_contents = []
    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)
        if os.path.isfile(file_path):
            with open(file_path, "r", encoding="utf-8") as f:
                file_contents.append(f.read())
    return file_contents

def build_index(texts):
    embeddings = model.encode(texts)
    embeddings = normalize(embeddings)
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)
    return index, embeddings

def get_most_relevant_story(user_story, index, documents):
    query_embedding = model.encode([user_story])
    query_embedding = normalize(query_embedding)
    D, I = index.search(query_embedding, k=3)
    top_stories = [documents[i] for i in I[0]]
    return top_stories
    # return documents[I[0][0]]

@app.route("/get_story", methods=["POST"])
def get_story():
    data = request.json
    age = int(data.get("age", 30))
    user_input = data.get("input", "")

    if age <= 25:
        target_group = 'elderly'
    else:
        target_group = 'young'

    target_dir = os.path.join('stories', target_group)
    documents = read_files_to_array(target_dir)
    index, _ = build_index(documents)
    top_stories = get_most_relevant_story(user_input, index, documents)
    return jsonify({"stories": top_stories})

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5000)
