# Script để kiểm tra tính hợp lệ của đường đi tìm được
def verify_path():
    # Đọc dữ liệu input
    with open("A_in.csv", "r") as f:
        n, D, C = map(int, f.readline().strip().split(','))
        grid = [list(map(int, f.readline().strip().split(','))) for _ in range(n)]
    
    print(f"Kích thước grid: {n}x{n}")
    print(f"Điểm bắt đầu: ({D}, {C})")
    print(f"Giá trị tại điểm bắt đầu: {grid[D][C]}")
    print()
    
    # In ra grid để visualize
    print("Grid (0=không đi được, 1=đi được):")
    for i in range(n):
        for j in range(n):
            print(grid[i][j], end=" ")
        print()
    print()
    
    # Đọc kết quả output
    with open("A_out.csv", "r") as f:
        num_steps = int(f.readline().strip())
        if num_steps == -1:
            print("Kết quả: Không tìm được đường đi")
            return
        
        path = []
        for _ in range(num_steps):
            i, j = map(int, f.readline().strip().split())
            path.append((i, j))
    
    print(f"Đường đi tìm được có {num_steps} bước:")
    for step, (i, j) in enumerate(path):
        print(f"Bước {step + 1}: ({i}, {j}) - Giá trị: {grid[i][j]}")
    print()
    
    # Kiểm tra tính hợp lệ của đường đi
    errors = []
    
    # 1. Kiểm tra điểm bắt đầu
    if path[0] != (D, C):
        errors.append(f"Điểm bắt đầu không đúng! Mong đợi: ({D}, {C}), thực tế: {path[0]}")
    
    # 2. Kiểm tra tất cả các ô trong đường đi có giá trị = 1
    for i, (x, y) in enumerate(path):
        if x < 0 or x >= n or y < 0 or y >= n:
            errors.append(f"Bước {i+1}: Tọa độ ({x}, {y}) nằm ngoài grid")
        elif grid[x][y] != 1:
            errors.append(f"Bước {i+1}: Ô ({x}, {y}) có giá trị {grid[x][y]}, không thể đi qua")
    
    # 3. Kiểm tra các bước di chuyển liền kề
    for i in range(1, len(path)):
        prev_x, prev_y = path[i-1]
        curr_x, curr_y = path[i]
        
        dx = abs(curr_x - prev_x)
        dy = abs(curr_y - prev_y)
        
        # Chỉ được di chuyển 1 bước theo chiều ngang hoặc dọc
        if (dx == 1 and dy == 0) or (dx == 0 and dy == 1):
            continue
        else:
            errors.append(f"Bước {i}: Di chuyển từ ({prev_x}, {prev_y}) đến ({curr_x}, {curr_y}) không hợp lệ")
    
    # 4. Kiểm tra điểm cuối có phải là cửa ra không
    if path:
        last_x, last_y = path[-1]
        is_exit = last_x == 0 or last_x == n-1 or last_y == 0 or last_y == n-1
        if not is_exit:
            errors.append(f"Điểm cuối ({last_x}, {last_y}) không phải là cửa ra")
        else:
            print(f"✓ Điểm cuối ({last_x}, {last_y}) là cửa ra hợp lệ")
    
    # In kết quả kiểm tra
    if not errors:
        print("✓ ĐƯỜNG ĐI HỢP LỆ! Tất cả các bước đều đúng.")
        
        # Visualize đường đi trên grid
        print("\nVisualization đường đi ('*' = đường đi, '.' = không đi được, ' ' = đi được nhưng không dùng):")
        path_set = set(path)
        for i in range(n):
            for j in range(n):
                if (i, j) in path_set:
                    print("*", end=" ")
                elif grid[i][j] == 0:
                    print(".", end=" ")
                else:
                    print(" ", end=" ")
            print()
    else:
        print("❌ ĐƯỜNG ĐI KHÔNG HỢP LỆ!")
        for error in errors:
            print(f"- {error}")

if __name__ == "__main__":
    verify_path()
