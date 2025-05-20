import numpy as np

def kmeans(data, k, max_iters=100):
    """
    Đầu vào:
        - data: Ma trận 2D (numpy array) chứa các điểm dữ liệu, mỗi hàng là một điểm.
        - k: Số cụm cần phân chia (số nguyên dương).
        - max_iters: Số vòng lặp tối đa (mặc định: 100).
    Đầu ra:
        - labels: Mảng 1D (numpy array) chứa nhãn cụm (từ 0 đến k-1) cho mỗi điểm dữ liệu.
    Thuật toán:
        1. Khởi tạo ngẫu nhiên k tâm cụm từ dữ liệu đầu vào.
        2. Lặp lại (tối đa max_iters lần):
           - Gán mỗi điểm dữ liệu vào cụm có tâm gần nhất (dựa trên khoảng cách Euclidean).
           - Cập nhật tâm cụm bằng cách tính trung bình các điểm trong mỗi cụm.
        3. Dừng nếu tâm cụm không thay đổi hoặc đạt max_iters.
        4. Trả về nhãn cụm cho từng điểm dữ liệu.
    """
    # Khởi tạo ngẫu nhiên k tâm cụm
    centroids = data[np.random.choice(data.shape[0], k, replace=False)]
    
    for _ in range(max_iters):
        # Gán điểm vào cụm gần nhất
        distances = np.sqrt(((data - centroids[:, np.newaxis])**2).sum(axis=2))
        labels = np.argmin(distances, axis=0)
        
        # Cập nhật tâm cụm
        new_centroids = np.array([data[labels == i].mean(axis=0) for i in range(k)])
        
        # Kiểm tra hội tụ
        if np.all(centroids == new_centroids):
            break
        centroids = new_centroids
    
    return labels