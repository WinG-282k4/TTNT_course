import heapq

def ucs(graph, start, goal):
    """
    Đầu vào:
        - graph: Đồ thị dạng danh sách kề (dict), khóa là nút, giá trị là danh sách (neighbor, cost).
        - start: Nút bắt đầu (hashable).
        - goal: Nút đích (hashable).
    Đầu ra:
        - path: Danh sách các nút từ start đến goal (hoặc None nếu không tìm thấy đường đi).
    Thuật toán:
        1. Khởi tạo hàng đợi ưu tiên với (cost=0, start, [start]) và tập visited.
        2. Lặp lại khi hàng đợi không rỗng:
           - Lấy trạng thái có chi phí thấp nhất từ hàng đợi.
           - Nếu nút đã thăm, bỏ qua.
           - Nếu nút là goal, trả về path.
           - Thêm các láng giềng chưa thăm vào hàng đợi với chi phí tích lũy.
        3. Trả về None nếu không tìm thấy đường đi.
    """
    queue = [(0, start, [start])]  # (cost, node, path)
    visited = set()
    
    while queue:
        cost, node, path = heapq.heappop(queue)
        if node in visited:
            continue
        visited.add(node)
        if node == goal:
            return path
        for neighbor, edge_cost in graph[node]:
            if neighbor not in visited:
                heapq.heappush(queue, (cost + edge_cost, neighbor, path + [neighbor]))
    return None