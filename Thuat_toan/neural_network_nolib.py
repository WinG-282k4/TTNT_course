def matrix_multiply(A, B):
    """Nhân hai ma trận A và B."""
    rows_A, cols_A = len(A), len(A[0])
    rows_B, cols_B = len(B), len(B[0])
    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]
    return result

def matrix_add(A, B):
    """Cộng hai ma trận A và B."""
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def matrix_subtract(A, B):
    """Trừ hai ma trận A và B."""
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def matrix_transpose(A):
    """Chuyển vị ma trận A."""
    return [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]

def scalar_multiply(scalar, A):
    """Nhân ma trận A với một số vô hướng."""
    return [[scalar * A[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def tanh(x):
    """Hàm kích hoạt tanh."""
    import math
    return (math.exp(x) - math.exp(-x)) / (math.exp(x) + math.exp(-x))

def sigmoid(x):
    """Hàm kích hoạt sigmoid."""
    import math
    return 1 / (1 + math.exp(-x))

def neural_network(X, y, hidden_size, epochs=1000, lr=0.01):
    """
    Đầu vào:
        - X: Ma trận dữ liệu đầu vào, mỗi hàng là một mẫu.
        - y: Ma trận nhãn đầu ra, mỗi hàng là nhãn của mẫu tương ứng.
        - hidden_size: Số nơ-ron trong lớp ẩn.
        - epochs: Số vòng lặp huấn luyện.
        - lr: Tốc độ học.
    Đầu ra:
        - W1, b1, W2, b2: Trọng số và bias của lớp ẩn và lớp đầu ra.
    """
    import random
    input_size = len(X[0])
    output_size = len(y[0])
    
    # Khởi tạo ngẫu nhiên trọng số và bias
    W1 = [[random.gauss(0, 1) for _ in range(hidden_size)] for _ in range(input_size)]
    b1 = [[0 for _ in range(hidden_size)]]
    W2 = [[random.gauss(0, 1) for _ in range(output_size)] for _ in range(hidden_size)]
    b2 = [[0 for _ in range(output_size)]]
    
    for _ in range(epochs):
        # Lan truyền thuận
        Z1 = matrix_add(matrix_multiply(X, W1), b1 * len(X))
        A1 = [[tanh(Z1[i][j]) for j in range(len(Z1[0]))] for i in range(len(Z1))]
        Z2 = matrix_add(matrix_multiply(A1, W2), b2 * len(A1))
        A2 = [[sigmoid(Z2[i][j]) for j in range(len(Z2[0]))] for i in range(len(Z2))]
        
        # Lan truyền ngược
        dZ2 = matrix_subtract(A2, y)
        dW2 = matrix_multiply(matrix_transpose(A1), dZ2)
        db2 = [[sum(dZ2[i][j] for i in range(len(dZ2))) for j in range(len(dZ2[0]))]]
        dA1 = matrix_multiply(dZ2, matrix_transpose(W2))
        dZ1 = [[dA1[i][j] * (1 - tanh(Z1[i][j])**2) for j in range(len(dA1[0]))] for i in range(len(dA1))]
        dW1 = matrix_multiply(matrix_transpose(X), dZ1)
        db1 = [[sum(dZ1[i][j] for i in range(len(dZ1))) for j in range(len(dZ1[0]))]]
        
        # Cập nhật trọng số
        W1 = matrix_subtract(W1, scalar_multiply(lr, dW1))
        b1 = matrix_subtract(b1, scalar_multiply(lr, db1))
        W2 = matrix_subtract(W2, scalar_multiply(lr, dW2))
        b2 = matrix_subtract(b2, scalar_multiply(lr, db2))
    
    return W1, b1, W2, b2