def minimax(state, depth, is_max, evaluate, get_moves, game_over):
    """
    Đầu vào:
        - state: Trạng thái hiện tại của trò chơi.
        - depth: Độ sâu tìm kiếm tối đa (số nguyên dương).
        - is_max: True nếu là lượt của người chơi Max, False nếu là Min.
        - evaluate: Hàm đánh giá giá trị trạng thái (trả về số).
        - get_moves: Hàm trả về danh sách các nước đi hợp lệ từ trạng thái.
        - game_over: Hàm kiểm tra trạng thái có phải trạng thái kết thúc.
    Đầu ra:
        - value: Giá trị tối ưu của trạng thái (Max tối đa hóa, Min tối thiểu hóa).
    Thuật toán:
        1. Nếu độ sâu bằng 0 hoặc trạng thái là kết thúc, trả về giá trị evaluate(state).
        2. Nếu là lượt Max:
           - Khởi tạo best_value là -∞.
           - Với mỗi nước đi, đệ quy gọi minimax với lượt Min, cập nhật best_value tối đa.
        3. Nếu là lượt Min:
           - Khởi tạo best_value là +∞.
           - Với mỗi nước đi, đệ quy gọi minimax với lượt Max, cập nhật best_value tối thiểu.
        4. Trả về best_value.
    """
    if depth == 0 or game_over(state):
        return evaluate(state)
    
    if is_max:
        best_value = float('-inf')
        for move in get_moves(state):
            new_state = move(state)
            value = minimax(new_state, depth - 1, False, evaluate, get_moves, game_over)
            best_value = max(best_value, value)
        return best_value
    else:
        best_value = float('inf')
        for move in get_moves(state):
            new_state = move(state)
            value = minimax(new_state, depth - 1, True, evaluate, get_moves, game_over)
            best_value = min(best_value, value)
        return best_value