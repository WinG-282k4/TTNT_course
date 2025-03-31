import numpy as np
import pandas as pd
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score, accuracy_score
import matplotlib.pyplot as plt

# Load Wine dataset
wine = load_wine()
X = wine.data
y = wine.target

print("Dataset Information:")
print(f"Number of samples: {X.shape[0]}")
print(f"Number of features: {X.shape[1]}")
print("\nFeatures:")
for feature in wine.feature_names:
    print(f"- {feature}")

print("\nOriginal Class Distribution:")
print(pd.Series(y).value_counts().sort_index())

# Thêm một class mới bằng cách chia class 2 thành 2 nhóm
# để có tổng cộng 4 class theo yêu cầu
mask_class2 = y == 2
X_class2 = X[mask_class2]
y_class2 = y[mask_class2]

# Chia class 2 thành 2 nhóm dựa trên một feature (ví dụ: alcohol content)
median = np.median(X_class2[:, 0])  # Sử dụng feature đầu tiên
y_class2_new = np.where(X_class2[:, 0] > median, 3, 2)

# Gộp lại dataset
X_new = np.vstack([X[~mask_class2], X_class2])
y_new = np.hstack([y[~mask_class2], y_class2_new])

print("\nNew Class Distribution (after splitting class 2):")
print(pd.Series(y_new).value_counts().sort_index())

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_new, y_new, test_size=0.2, random_state=42)

# Scale the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Create and train Linear Regression model
model = LinearRegression()
model.fit(X_train_scaled, y_train)

# Make predictions
y_pred = model.predict(X_test_scaled)

# Round predictions to nearest integer and clip to valid class range
y_pred_rounded = np.round(y_pred).clip(0, 3).astype(int)

# Calculate performance metrics
mse = mean_squared_error(y_test, y_pred_rounded)
r2 = r2_score(y_test, y_pred_rounded)
accuracy = accuracy_score(y_test, y_pred_rounded)

print("\nModel Performance Metrics:")
print(f"Mean Squared Error: {mse:.4f}")
print(f"R-squared Score: {r2:.4f}")
print(f"Accuracy: {accuracy:.4f}")

# Print feature importance
feature_importance = pd.DataFrame({
    'Feature': wine.feature_names,
    'Coefficient': model.coef_
})
print("\nFeature Importance:")
print(feature_importance.sort_values(by='Coefficient', ascending=False))

# Visualize một số dự đoán
fig, axes = plt.subplots(2, 4, figsize=(10, 5))
for i, ax in enumerate(axes.ravel()):
    if i < len(X_test):
        ax.imshow(X_test[i].reshape(13, 1), cmap='binary')
        ax.set_title(f'True: {y_test[i]}\nPred: {y_pred_rounded[i]}')
        ax.axis('off')
plt.suptitle('Example predictions')
plt.show() 