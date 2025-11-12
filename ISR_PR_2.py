from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import os

# --- Step 1: Read multiple text files ---
folder = "docs"   # Folder containing text files
documents = []
filenames = []

for file in os.listdir(folder):
    if file.endswith(".txt"):
        with open(os.path.join(folder, file), 'r', encoding='utf-8') as f:
            documents.append(f.read())
            filenames.append(file)

print("Files read:", filenames)
print("-" * 80)

# --- Step 2: Convert documents to TF-IDF vectors ---
vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = vectorizer.fit_transform(documents)

# --- Step 3: Define threshold for similarity ---
THRESHOLD = 0.02   # Adjust as needed

# --- Step 4: Single-Pass Clustering Algorithm ---
clusters = []    
cluster_centroids = []    

for i, doc_vector in enumerate(tfidf_matrix):
    assigned = False
    for j, centroid in enumerate(cluster_centroids):
        sim = cosine_similarity(doc_vector, centroid)[0][0]
        if sim >= THRESHOLD:
            clusters[j].append(filenames[i])
            # Update centroid (average of all vectors in cluster)
            cluster_centroids[j] = (cluster_centroids[j] + doc_vector) / 2
            assigned = True
            break


    if not assigned:
        clusters.append([filenames[i]])
        cluster_centroids.append(doc_vector)

# --- Step 5: Display cluster results ---
print("Clusters formed:")
for i, cluster in enumerate(clusters):
    print(f"Cluster {i+1}: {cluster}")
