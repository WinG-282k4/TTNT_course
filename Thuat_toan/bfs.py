from collections import deque

def bfs(graph, start, goal):
    """
    Đầu vào:
        - graph: Đồ thị dạng danh sách kề (dict), khóa là nút, giá trị là danh sách các nút láng giềng.
        - start: Nút bắt đầu (hashable, ví dụ: string hoặc int).
        - goal: Nút đích (hashable, ví dụ: string hoặc int).
    Đầu ra:
        - path: Danh sách các nút từ start đến goal (hoặc None nếu không tìm thấy đường đi).
    Thuật toán:
        1. Khởi tạo hàng đợi với trạng thái (start, [start]) và tập visited chứa start.
        2. Lặp lại khi hàng đợi không rỗng:
           - Lấy nút đầu tiên từ hàng đợi.
           - Nếu nút là goal, trả về đường đi.
           - Thêm các láng giềng chưa thăm vào hàng đợi và tập visited.
        3. Trả về None nếu không tìm thấy đường đi.
    """
    queue = deque([(start, [start])])
    visited = set([start])
    
    while queue:
        node, path = queue.popleft()
        if node == goal:
            return path
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    return None