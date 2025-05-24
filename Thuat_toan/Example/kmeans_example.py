# Hàm từ kmeans.py (đã cung cấp trước đó)
def euclidean_distance(point1, point2):
    return sum((point1[i] - point2[i])**2 for i in range(len(point1)))**0.5

# Dữ liệu mẫu (4 điểm 2D)
data = [[1, 2], [2, 1], [10, 12], [12, 10]]

# Phân cụm
from kmeans import kmeans  # Giả sử kmeans.py chứa hàm
labels = kmeans(data, k=2, max_iters=100)
print("Nhãn cụm:", labels)  # Ví dụ: [0, 0, 1, 1]

# Hiển thị kết quả
for i, point in enumerate(data):
    print(f"Điểm {point} thuộc cụm {labels[i]}")