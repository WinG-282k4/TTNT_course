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

def matrix_transpose(A):
    """Chuyển vị ma trận A."""
    return [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]

def scalar_multiply(scalar, A):
    """Nhân ma trận A với một số vô hướng."""
    return [[scalar * A[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def matrix_subtract(A, B):
    """Trừ hai ma trận A và B."""
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def sigmoid(x):
    """Hàm kích hoạt sigmoid: f(x) = 1 / (1 + e^(-x))."""
    import math
    try:
        return 1 / (1 + math.exp(-x))
    except OverflowError:
        return 0 if x < 0 else 1

def logistic_regression(X, y, epochs=1000, lr=0.01):
    """
    Hồi quy logistic cho phân loại nhị phân.
    Đầu vào:
        - X: Ma trận dữ liệu đầu vào, mỗi hàng là một mẫu (list của lists).
        - y: Danh sách nhãn (0 hoặc 1) cho mỗi mẫu (list).
        - epochs: Số vòng lặp huấn luyện (mặc định: 1000).
        - lr: Tốc độ học (mặc định: 0.01).
    Đầu ra:
        - w: Trọng số sau huấn luyện (list của lists).
        - b: Bias sau huấn luyện (số thực).
    Thuật toán:
        1. Khởi tạo ngẫu nhiên trọng số và bias.
        2. Lặp qua epochs lần:
           - Tính đầu ra dự đoán (lan truyền thuận) bằng hàm sigmoid.
           - Tính gradient của hàm mất mát cross-entropy.
           - Cập nhật trọng số và bias bằng gradient descent.
        3. Trả về trọng số và bias đã huấn luyện.
    """
    import random
    n_samples = len(X)
    n_features = len(X[0])
    
    # Khởi tạo trọng số ngẫu nhiên và bias
    w = [[random.gauss(0, 1)] for _ in range(n_features)]  # Ma trận cột
    b = 0.0
    
    for epoch in range(epochs):
        # Lan truyền thuận: Tính z = Xw + b, sau đó áp dụng sigmoid
        Z = [sum(X[i][j] * w[j][0] for j in range(n_features)) + b for i in range(n_samples)]
        A = [sigmoid(z) for z in Z]  # Dự đoán xác suất
        
        # Tính gradient (lan truyền ngược)
        dZ = [A[i] - y[i] for i in range(n_samples)]  # Gradient của hàm mất mát
        dW = matrix_multiply(matrix_transpose(X), [[dz] for dz in dZ])  # Gradient cho trọng số
        db = sum(dZ) / n_samples  # Gradient cho bias (trung bình)
        
        # Cập nhật trọng số và bias
        w = matrix_subtract(w, scalar_multiply(lr, dW))
        b -= lr * db
        
        # In tiến trình (tùy chọn, mỗi 100 epochs)
        if (epoch + 1) % 100 == 0:
            loss = -sum(y[i] * math.log(A[i] + 1e-10) + (1 - y[i]) * math.log(1 - A[i] + 1e-10) for i in range(n_samples)) / n_samples
            print(f"Epoch {epoch + 1}, Loss: {loss}")
    
    return w, b