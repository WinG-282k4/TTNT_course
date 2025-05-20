import heapq

def astar(graph, start, goal, heuristic):
    """
    Đầu vào:
        - graph: Đồ thị dạng danh sách kề (dict), khóa là nút, giá trị là danh sách (neighbor, cost).
        - start: Nút bắt đầu (hashable).
        - goal: Nút đích (hashable).
        - heuristic: Hàm heuristic h(u) ước lượng chi phí từ nút u đến goal (phải chấp nhận được).
    Đầu ra:
        - path: Danh sách các nút từ start đến goal (hoặc None nếu không tìm thấy đường đi).
    Thuật toán:
        1. Khởi tạo hàng đợi ưu tiên với (f_score=heuristic(start), g_score=0, start, [start]).
        2. Lặp lại khi hàng đợi không rỗng:
           - Lấy trạng thái có f_score thấp nhất (f = g + h, g là chi phí từ start, h là heuristic).
           - Nếu nút đã thăm, bỏ qua.
           - Nếu nút là goal, trả về path.
           - Thêm các láng giềng chưa thăm vào hàng đợi với f_score mới.
        3. Trả về None nếu không tìm thấy đường đi.
    """
    queue = [(0 + heuristic(start, goal), 0, start, [start])]  # (f_score, g_score, node, path)
    visited = set()
    
    while queue:
        _, g_score, node, path = heapq.heappop(queue)
        if node in visited:
            continue
        visited.add(node)
        if node == goal:
            return path
        for neighbor, cost in graph[node]:
            if neighbor not in visited:
                new_g = g_score + cost
                heapq.heappush(queue, (new_g + heuristic(neighbor, goal), new_g, neighbor, path + [neighbor]))
    return None