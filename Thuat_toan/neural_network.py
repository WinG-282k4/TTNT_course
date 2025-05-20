import numpy as np

def neural_network(X, y, hidden_size, epochs=1000, lr=0.01):
    """
    Đầu vào:
        - X: Ma trận dữ liệu đầu vào (numpy array), mỗi hàng là một mẫu.
        - y: Ma trận nhãn đầu ra (numpy array), mỗi hàng là nhãn của mẫu tương ứng.
        - hidden_size: Số nơ-ron trong lớp ẩn (số nguyên dương).
        - epochs: Số vòng lặp huấn luyện (mặc định: 1000).
        - lr: Tốc độ học (learning rate, mặc định: 0.01).
    Đầu ra:
        - W1, b1, W2, b2: Trọng số và bias của lớp ẩn và lớp đầu ra sau huấn luyện.
    Thuật toán:
        1. Khởi tạo ngẫu nhiên trọng số (W1, W2) và bias (b1, b2) cho mạng nơ-ron.
        2. Lặp lại trong epochs lần:
           - Lan truyền thuận: Tính toán đầu ra qua lớp ẩn (hàm tanh) và lớp đầu ra (hàm sigmoid).
           - Lan truyền ngược: Tính gradient và cập nhật trọng số/bias bằng gradient descent.
        3. Trả về trọng số và bias đã huấn luyện.
    """
    input_size = X.shape[1]
    output_size = y.shape[1]
    
    # Khởi tạo trọng số
    W1 = np.random.randn(input_size, hidden_size)
    b1 = np.zeros((1, hidden_size))
    W2 = np.random.randn(hidden_size, output_size)
    b2 = np.zeros((1, output_size))
    
    for _ in range(epochs):
        # Lan truyền thuận
        Z1 = X @ W1 + b1
        A1 = np.tanh(Z1)
        Z2 = A1 @ W2 + b2
        A2 = 1 / (1 + np.exp(-Z2))  # Sigmoid
        
        # Lan truyền ngược
        dZ2 = A2 - y
        dW2 = A1.T @ dZ2
        db2 = np.sum(dZ2, axis=0, keepdims=True)
        dA1 = dZ2 @ W2.T
        dZ1 = dA1 * (1 - np.tanh(Z1)**2)
        dW1 = X.T @ dZ1
        db1 = np.sum(dZ1, axis=0, keepdims=True)
        
        # Cập nhật trọng số
        W1 -= lr * dW1
        b1 -= lr * db1
        W2 -= lr * dW2
        b2 -= lr * db2
    
    return W1, b1, W2, b2