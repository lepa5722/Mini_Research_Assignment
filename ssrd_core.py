import numpy as np
from sklearn.cluster import KMeans


def compute_cosine_similarity(vec1, vec2):
    vec1, vec2 = np.array(vec1), np.array(vec2)
    norm1 = np.linalg.norm(vec1)
    norm2 = np.linalg.norm(vec2)
    if norm1 == 0 or norm2 == 0:
        return 0.0
    return np.dot(vec1, vec2) / (norm1 * norm2)


def compute_similarity_matrix(embeddings):
    n = len(embeddings)
    matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(i + 1, n):
            sim = compute_cosine_similarity(embeddings[i], embeddings[j])
            matrix[i][j] = matrix[j][i] = sim
    return matrix


def avg_similarity_per_client(similarity_matrix):
    n = len(similarity_matrix)
    return [np.mean([similarity_matrix[i][j] for j in range(n) if j != i]) for i in range(n)]


def kmeans_detection(avg_similarities):
    data = np.array(avg_similarities).reshape(-1, 1)
    kmeans = KMeans(n_clusters=2, n_init='auto', random_state=42).fit(data)
    labels = kmeans.labels_

    # Identify which cluster has lower similarity → anomaly
    cluster_means = [np.mean(data[labels == i]) for i in range(2)]
    anomaly_label = int(np.argmin(cluster_means))
    detected = labels == anomaly_label
    return detected


def print_detection_results(avg_similarities, attack_types, detected):
    print(f"\n{'Client':<10} {'Attack':<12} {'Avg Similarity':<17} {'Detected?'}")
    print("-" * 55)
    for i, (attack, sim, is_anomaly) in enumerate(zip(attack_types, avg_similarities, detected)):
        label = "Anomaly" if is_anomaly else "Benign"
        print(f"Client{i:<5} {attack:<12} {sim:<17.3f} {label}")
