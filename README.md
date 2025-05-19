# Mini_Research_Assignment
# Lightweight Misalignment Detection for Network-Induced Anomalies in Federated Learning using SSRD-inspired Embedding Similarity

This project simulates and analyzes client behaviors in a federated learning environment to detect network-based attacks such as DDoS, MITM, and Spoofing using cosine similarity and clustering techniques.

## 🔧 Files Overview

- `simulate.py`: Simulates client embeddings representing benign and adversarial updates
- `analyze.py`: Computes similarity scores, builds the similarity matrix, calculates average similarity, and applies KMeans/dynamic threshold detection to flag anomalies
- `ssd_core.py`: Contains core utility functions including cosine similarity computation and detection logic (modularized for reuse)

## 📦 Requirements

- Python 3.8+
- `numpy`
- `scikit-learn`
- `matplotlib` *(optional, for plotting)*

Install dependencies with:

```bash
pip install numpy scikit-learn matplotlib

