import numpy as np
# Percentile is used
def dynamic_threshold_detection(avg_sims, method='mean_std', k=1.0, percentile=20):
    arr = np.array(avg_sims)
    if method == 'mean_std':
        mean = arr.mean()
        std = arr.std()
        threshold = mean - k * std
    elif method == 'percentile':
        threshold = np.percentile(arr, percentile)
    else:
        raise ValueError("Unsupported method")
    detected = [sim < threshold for sim in avg_sims]
    return threshold, detected
