from ssrd_core import compute_similarity_matrix, avg_similarity_per_client, kmeans_detection, print_detection_results
import numpy as np

print("\n--- Simulating Clients ---")

# Simulated embeddings: 3 benign, 3 attacks
embeddings = [
    np.random.normal(loc=1, scale=0.1, size=128),  # Client 0 (benign)
    np.random.normal(loc=1, scale=0.1, size=128),  # Client 1 (benign)
    np.random.normal(loc=1, scale=0.1, size=128),  # Client 2 (benign)
    np.random.normal(loc=0, scale=0.5, size=128),  # Client 3 (ddos)
    np.random.normal(loc=0, scale=0.6, size=128),  # Client 4 (mitm)
    np.random.normal(loc=0, scale=0.7, size=128),  # Client 5 (spoofing)
]

attack_types = ['benign', 'benign', 'benign', 'ddos', 'mitm', 'spoofing']

# Compute similarity matrix and average similarities
sim_matrix = compute_similarity_matrix(embeddings)

print("\n--- Cosine Similarity Matrix ---")
n = len(sim_matrix)
for i in range(n):
    for j in range(i + 1, n):
        print(f"Client{i} ↔ Client{j}: {sim_matrix[i][j]:.4f}")

avg_similarities = avg_similarity_per_client(sim_matrix)

# Run KMeans-based detection
detected = kmeans_detection(avg_similarities)

# Show results
print_detection_results(avg_similarities, attack_types, detected)
