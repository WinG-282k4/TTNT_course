def dfs(graph, start, goal, visited=None, path=None):
    """
    Đầu vào:
        - graph: Đồ thị dạng danh sách kề (dict), khóa là nút, giá trị là danh sách các nút láng giềng.
        - start: Nút bắt đầu (hashable).
        - goal: Nút đích (hashable).
        - visited: Tập các nút đã thăm (mặc định: None, sẽ được khởi tạo).
        - path: Danh sách đường đi hiện tại (mặc định: None, sẽ được khởi tạo).
    Đầu ra:
        - path: Danh sách các nút từ start đến goal (hoặc None nếu không tìm thấy đường đi).
    Thuật toán:
        1. Khởi tạo tập visited và path nếu chưa có.
        2. Thêm start vào visited và path.
        3. Nếu start là goal, trả về path.
        4. Đệ quy duyệt từng láng giềng chưa thăm của start, cập nhật path.
        5. Trả về None nếu không tìm thấy đường đi.
    """
    if visited is None:
        visited = set()
    if path is None:
        path = [start]
    visited.add(start)
    
    if start == goal:
        return path
    for neighbor in graph[start]:
        if neighbor not in visited:
            new_path = dfs(graph, neighbor, goal, visited, path + [neighbor])
            if new_path:
                return new_path
    return None