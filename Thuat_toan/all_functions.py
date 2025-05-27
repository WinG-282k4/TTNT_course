import numpy as np
import math

# Hàm khoảng cách (Lesson 11 KNN.pdf, trang 19)
def manhattan_distance(x, y):
    """Tính khoảng cách Manhattan"""
    return sum(abs(a - b) for a, b in zip(x, y))

def euclidean_distance(x, y):
    """Tính khoảng cách Euclidean"""
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(x, y)))

def minkowski_distance(x, y, p=2):
    """Tính khoảng cách Minkowski"""
    return sum(abs(a - b) ** p for a, b in zip(x, y)) ** (1 / p)

# Hàm mất mát (Lesson 13 ANN 1.pdf)
def cross_entropy_loss(y_true, y_pred):
    """Tính mất mát cross-entropy (trang 20-22)"""
    n_samples = len(y_true)
    y_pred = np.clip(y_pred, 1e-15, 1 - 1e-15)  # Tránh log(0)
    loss = -np.sum(y_true * np.log(y_pred)) / n_samples
    return loss

def mean_squared_error(y_true, y_pred):
    """Tính mất mát MSE (trang 5, ngầm định)"""
    n_samples = len(y_true)
    return np.sum((y_true - y_pred) ** 2) / n_samples

# Hàm kích hoạt và Softmax (Lesson 13 ANN 1.pdf)
def softmax(z):
    """Tính hàm Softmax (trang 20)"""
    exp_z = np.exp(z - np.max(z, axis=1, keepdims=True))  # Tránh tràn số
    return exp_z / np.sum(exp_z, axis=1, keepdims=True)

def relu(x):
    """Tính hàm ReLU (trang 19)"""
    return np.maximum(0, x)

def sigmoid(x):
    """Tính hàm Sigmoid (trang 5, ngầm định)"""
    return 1 / (1 + np.exp(-np.clip(x, -500, 500)))

def tanh(x):
    """Tính hàm Tanh (trang 5, ngầm định)"""
    return np.tanh(x)

# Hàm demo
if __name__ == "__main__":
    # Demo khoảng cách
    x = [1, 2, 3, 4]
    y = [2, 3, 4, 5]
    print(f"Manhattan distance: {manhattan_distance(x, y)}")
    print(f"Euclidean distance: {euclidean_distance(x, y)}")
    print(f"Minkowski distance (p=3): {minkowski_distance(x, y, p=3)}")
    
    # Demo mất mát
    y_true = np.array([[1, 0, 0], [0, 1, 0]])
    y_pred = np.array([[0.7, 0.2, 0.1], [0.1, 0.8, 0.1]])
    print(f"Cross-entropy loss: {cross_entropy_loss(y_true, y_pred)}")
    
    y_true_reg = np.array([1, 2, 3])
    y_pred_reg = np.array([1.1, 2.2, 2.8])
    print(f"MSE loss: {mean_squared_error(y_true_reg, y_pred_reg)}")
    
    # Demo Softmax và kích hoạt
    z = np.array([[1, 2, 3], [4, 5, 6]])
    print(f"Softmax: {softmax(z)}")
    
    x = np.array([-1, 0, 1])
    print(f"ReLU: {relu(x)}")
    print(f"Sigmoid: {sigmoid(x)}")
    print(f"Tanh: {tanh(x)}")