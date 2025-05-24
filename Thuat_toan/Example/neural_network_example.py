def matrix_multiply(A, B):
    rows_A, cols_A = len(A), len(A[0])
    rows_B, cols_B = len(B), len(B[0])
    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]
    return result

def matrix_add(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def tanh(x):
    import math
    return (math.exp(x) - math.exp(-x)) / (math.exp(x) + math.exp(-x))

def sigmoid(x):
    import math
    return 1 / (1 + math.exp(-x))

def predict_neural_network(X, W1, b1, W2, b2):
    """
    Dự đoán sử dụng mạng nơ-ron đã huấn luyện.
    Đầu vào:
        - X: Dữ liệu đầu vào (list of lists).
        - W1, b1, W2, b2: Trọng số và bias từ hàm neural_network.
    Đầu ra:
        - Dự đoán lớp (0 hoặc 1 cho mỗi đầu ra).
    """
    Z1 = matrix_add(matrix_multiply(X, W1), [b1[0]] * len(X))
    A1 = [[tanh(Z1[i][j]) for j in range(len(Z1[0]))] for i in range(len(Z1))]
    Z2 = matrix_add(matrix_multiply(A1, W2), [b2[0]] * len(A1))
    A2 = [[sigmoid(Z2[i][j]) for j in range(len(Z2[0]))] for i in range(len(Z2))]
    return [[1 if a > 0.5 else 0 for a in row] for row in A2]

# Ví dụ sử dụng
from neural_network import neural_network
X_train = [[0, 0], [0, 1], [1, 0], [1, 1]]
y_train = [[0, 1], [1, 0], [1, 0], [0, 1]]
W1, b1, W2, b2 = neural_network(X_train, y_train, hidden_size=4, epochs=1000, lr=0.01)

X_test = [[0, 1], [1, 1]]
predictions = predict_neural_network(X_test, W1, b1, W2, b2)
print("Dự đoán:", predictions)  # Ví dụ: [[1, 0], [0, 1]]