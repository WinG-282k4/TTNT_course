def hill_climbing(graph, start, evaluate):
    """
    Đầu vào:
        - graph: Đồ thị dạng danh sách kề (dict), khóa là nút, giá trị là danh sách các nút láng giềng.
        - start: Nút bắt đầu (hashable).
        - evaluate: Hàm đánh giá h(u) trả về giá trị số của trạng thái u (giá trị nhỏ hơn là tốt hơn).
    Đầu ra:
        - current: Trạng thái cục bộ tối ưu (hoặc None nếu không có láng giềng).
    Thuật toán:
        1. Bắt đầu từ trạng thái start.
        2. Lặp lại:
           - Tìm láng giềng có giá trị evaluate tốt nhất.
           - Nếu láng giềng không tốt hơn trạng thái hiện tại, trả về trạng thái hiện tại.
           - Cập nhật trạng thái hiện tại thành láng giềng tốt nhất.
        3. Trả về None nếu không có láng giềng.
    """
    current = start
    while True:
        neighbors = graph[current]
        if not neighbors:
            return current
        next_node = min(neighbors, key=evaluate)
        if evaluate(next_node) >= evaluate(current):
            return current
        current = next_node
    return None