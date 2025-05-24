# Hàm từ logistic_regression.py (đã cung cấp trước đó)
def matrix_multiply(A, B):
    rows_A, cols_A = len(A), len(A[0])
    rows_B, cols_B = len(B), len(B[0])
    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]
    return result

def sigmoid(x):
    import math
    try:
        return 1 / (1 + math.exp(-x))
    except OverflowError:
        return 0 if x < 0 else 1

# Hàm dự đoán
def predict_logistic_regression(X, w, b):
    Z = [sum(X[i][j] * w[j][0] for j in range(len(X[0]))) + b for i in range(len(X))]
    return [1 if sigmoid(z) > 0.5 else 0 for z in Z], [sigmoid(z) for z in Z]

# Dữ liệu mẫu
X = [[0, 0], [0, 1], [1, 0], [1, 1]]  # 4 mẫu, 2 đặc trưng
y = [0, 1, 1, 0]  # Nhãn nhị phân

# Huấn luyện
from logistic_regression import logistic_regression  # Giả sử logistic_regression.py chứa hàm
w, b = logistic_regression(X, y, epochs=1000, lr=0.01)

# Dự đoán trên dữ liệu mới
X_test = [[0, 1], [1, 1]]
classes, probabilities = predict_logistic_regression(X_test, w, b)
print("Dự đoán lớp:", classes)  # Ví dụ: [1, 0]
print("Xác suất lớp 1:", probabilities)  # Ví dụ: [0.75, 0.25]