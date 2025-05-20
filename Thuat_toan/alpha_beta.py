def alpha_beta(state, depth, alpha, beta, is_max, evaluate, get_moves, game_over):
    """
    Đầu vào:
        - state: Trạng thái hiện tại của trò chơi.
        - depth: Độ sâu tìm kiếm tối đa (số nguyên dương).
        - alpha: Giá trị alpha cho cắt tỉa (ban đầu là -∞).
        - beta: Giá trị beta cho cắt tỉa (ban đầu là +∞).
        - is_max: True nếu là lượt của người chơi Max, False nếu là Min.
        - evaluate: Hàm đánh giá giá trị trạng thái (trả về số).
        - get_moves: Hàm trả về danh sách các nước đi hợp lệ từ trạng thái.
        - game_over: Hàm kiểm tra trạng thái có phải trạng thái kết thúc.
    Đầu ra:
        - value: Giá trị tối ưu của trạng thái (Max tối đa hóa, Min tối thiểu hóa).
    Thuật toán:
        1. Nếu độ sâu bằng 0 hoặc trạng thái là kết thúc, trả về giá trị evaluate(state).
        2. Nếu là lượt Max:
           - Khởi tạo value là -∞.
           - Với mỗi nước đi, đệ quy gọi alpha_beta với lượt Min, cập nhật value tối đa và alpha.
           - Nếu alpha >= beta, cắt tỉa và thoát vòng lặp.
        3. Nếu là lượt Min:
           - Khởi tạo value là +∞.
           - Với mỗi nước đi, đệ quy gọi alpha_beta với lượt Max, cập nhật value tối thiểu và beta.
           - Nếu alpha >= beta, cắt tỉa và thoát vòng lặp.
        4. Trả về value.
    """
    if depth == 0 or game_over(state):
        return evaluate(state)
    
    if is_max:
        value = float('-inf')
        for move in get_moves(state):
            new_state = move(state)
            value = max(value, alpha_beta(new_state, depth - 1, alpha, beta, False, evaluate, get_moves, game_over))
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return value
    else:
        value = float('inf')
        for move in get_moves(state):
            new_state = move(state)
            value = min(value, alpha_beta(new_state, depth - 1, alpha, beta, True, evaluate, get_moves, game_over))
            beta = min(beta, value)
            if alpha >= beta:
                break
        return value