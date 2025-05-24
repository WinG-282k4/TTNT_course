def euclidean_distance(point1, point2):
    """Tính khoảng cách Euclidean giữa hai điểm."""
    return sum((point1[i] - point2[i])**2 for i in range(len(point1)))**0.5

def kmeans(data, k, max_iters=100):
    """
    Đầu vào:
        - data: Danh sách các điểm dữ liệu, mỗi điểm là một danh sách.
        - k: Số cụm cần phân chia.
        - max_iters: Số vòng lặp tối đa.
    Đầu ra:
        - labels: Danh sách nhãn cụm cho mỗi điểm dữ liệu.
    """
    import random
    n_samples = len(data)
    n_features = len(data[0])
    
    # Khởi tạo ngẫu nhiên k tâm cụm
    indices = random.sample(range(n_samples), k)
    centroids = [data[i] for i in indices]
    
    for _ in range(max_iters):
        # Gán điểm vào cụm gần nhất
        labels = []
        for point in data:
            distances = [euclidean_distance(point, centroid) for centroid in centroids]
            labels.append(distances.index(min(distances)))
        
        # Cập nhật tâm cụm
        new_centroids = [[0] * n_features for _ in range(k)]
        counts = [0] * k
        for i, point in enumerate(data):
            cluster = labels[i]
            for j in range(n_features):
                new_centroids[cluster][j] += point[j]
            counts[cluster] += 1
        
        for i in range(k):
            if counts[i] > 0:
                new_centroids[i] = [x / counts[i] for x in new_centroids[i]]
        
        # Kiểm tra hội tụ
        if all(euclidean_distance(centroids[i], new_centroids[i]) == 0 for i in range(k)):
            break
        centroids = new_centroids
    
    return labels