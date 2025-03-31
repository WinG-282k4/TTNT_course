import math

# Hàm Minimax với cắt tỉa Alpha-Beta
def minimax(depth, node_index, is_max, values, alpha, beta):
    # Giới hạn độ sâu của cây (nếu đạt lá, trả về giá trị của nút đó)
    if depth == math.log2(len(values)):
        return values[node_index]

    if is_max:  # Nếu là lượt của Max
        best = -math.inf

        # Duyệt qua 2 con của nút hiện tại
        for i in range(2):
            val = minimax(depth + 1, node_index * 2 + i, False, values, alpha, beta)
            best = max(best, val)  # Max chọn giá trị lớn nhất
            alpha = max(alpha, best)  # Cập nhật Alpha

            # Cắt tỉa nếu Alpha >= Beta
            if alpha >= beta:
                break  # Dừng duyệt sớm
        return best

    else:  # Nếu là lượt của Min
        best = math.inf

        # Duyệt qua 2 con của nút hiện tại
        for i in range(2):
            val = minimax(depth + 1, node_index * 2 + i, True, values, alpha, beta)
            best = min(best, val)  # Min chọn giá trị nhỏ nhất
            beta = min(beta, best)  # Cập nhật Beta

            # Cắt tỉa nếu Alpha >= Beta
            if alpha >= beta:
                break  # Dừng duyệt sớm
        return best

# Giá trị của các nút lá
values = [3, 5, 6, 9, 1, 2, 0, -1]

# Gọi Minimax từ gốc (depth = 0, node_index = 0, Max đi trước)
best_score = minimax(0, 0, True, values, -math.inf, math.inf)
print("Giá trị tối ưu của Minimax với Alpha-Beta:", best_score)
