import heapq

def manhattan_to_exit(i, j, n):
    """Tính hàm h(x) - khoảng cách Manhattan đến cửa ra gần nhất"""
    return min(i, n-1-i, j, n-1-j)

def is_exit(i, j, n):
    """Kiểm tra xem ô (i, j) có phải là cửa ra (rìa lâu đài)"""
    return i == 0 or i == n-1 or j == 0 or j == n-1

def a_star(grid, start, n):
    """Thuật toán A* để tìm đường thoát hiểm"""
    # Hướng di chuyển: lên, xuống, trái, phải
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # Hàng đợi ưu tiên cho A*
    open_list = []
    heapq.heappush(open_list, (0, start, [start]))  # (f(x), (i, j), path)
    
    # Lưu chi phí g(x) và đường đi
    g = {start: 0}
    visited = set()
    
    while open_list:
        f, (i, j), path = heapq.heappop(open_list)
        
        if (i, j) in visited:
            continue
            
        visited.add((i, j))
        
        # Kiểm tra nếu ô hiện tại là cửa ra
        if is_exit(i, j, n):
            return path
        
        # Duyệt các ô kề
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < n and grid[ni][nj] == 1 and (ni, nj) not in visited:
                new_g = g[(i, j)] + 1  # Chi phí từ điểm xuất phát đến ô kề
                if (ni, nj) not in g or new_g < g[(ni, nj)]:
                    g[(ni, nj)] = new_g
                    h = manhattan_to_exit(ni, nj, n)
                    f = new_g + h
                    new_path = path + [(ni, nj)]
                    heapq.heappush(open_list, (f, (ni, nj), new_path))
    
    return None  # Không tìm được đường thoát

def solve_escape_tunnel():
    # Đọc dữ liệu từ file
    with open("A_in.csv", "r") as f:
        n, D, C = map(int, f.readline().strip().split(','))
        grid = [list(map(int, f.readline().strip().split(','))) for _ in range(n)]
    
    # Tìm đường thoát bằng A*
    start = (D, C)
    path = a_star(grid, start, n)
    
    # Ghi kết quả ra file A_out.csv
    with open("A_out.csv", "w") as f:
        if path is None:
            f.write("-1\n")
        else:
            f.write(f"{len(path)}\n")
            for i, j in path:
                f.write(f"{i} {j}\n")

# Thực thi chương trình
solve_escape_tunnel()