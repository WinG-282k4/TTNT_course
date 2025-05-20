import heapq

def greedy_best_first(graph, start, goal, heuristic):
    """
    Đầu vào:
        - graph: Đồ thị dạng danh sách kề (dict), khóa là nút, giá trị là danh sách các nút láng giềng.
        - start: Nút bắt đầu (hashable).
        - goal: Nút đích (hashable).
        - heuristic: Hàm heuristic h(u) ước lượng chi phí từ nút u đến goal.
    Đầu ra:
        - path: Danh sách các nút từ start đến goal (hoặc None nếu không tìm thấy đường đi).
    Thuật toán:
        1. Khởi tạo hàng đợi ưu tiên với (heuristic(start), start, [start]) và tập visited.
        2. Lặp lại khi hàng đợi không rỗng:
           - Lấy trạng thái có giá trị heuristic thấp nhất.
           - Nếu nút đã thăm, bỏ qua.
           - Nếu nút là goal, trả về path.
           - Thêm các láng giềng chưa thăm vào hàng đợi với giá trị heuristic.
        3. Trả về None nếu không tìm thấy đường đi.
    """
    queue = [(heuristic(start, goal), start, [start])]
    visited = set()
    
    while queue:
        _, node, path = heapq.heappop(queue)
        if node in visited:
            continue
        visited.add(node)
        if node == goal:
            return path
        for neighbor in graph[node]:
            if neighbor not in visited:
                heapq.heappush(queue, (heuristic(neighbor, goal), neighbor, path + [neighbor]))
    return None