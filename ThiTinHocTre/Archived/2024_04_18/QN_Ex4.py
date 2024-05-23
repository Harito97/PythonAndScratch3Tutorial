from collections import deque

def count_reachable_cells(matrix, start_x, start_y):
    def is_valid_move(x, y):
        return 0 <= x < rows and 0 <= y < cols
    
    def bfs(start_x, start_y):
        if matrix[start_x][start_y] == 1:
            return -1
        
        reached_cell = set([(start_x, start_y)])
        visited = set([(start_x, start_y)])
        queue = deque([(start_x, start_y)])
        visited.add((start_x, start_y))
        
        while queue:
            x, y = queue.popleft()
            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy
                if is_valid_move(new_x, new_y):
                    if matrix[new_x][new_y] == 0 and (new_x, new_y) not in visited:
                        reached_cell.add((new_x, new_y))                    
                        queue.append((new_x, new_y))
                    visited.add((new_x, new_y))
        
        return len(reached_cell), reached_cell
    
    rows, cols = len(matrix), len(matrix[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
    
    return bfs(start_x, start_y)

matrix = [
    [0, 0, 1, 0, 0],
    [0, 1, 0, 0, 1],
    [1, 0, 0, 0, 0],
    [0, 1, 0, 0, 1]
]

start_x = int(input("Nhập vào tọa độ x của ô xuất phát: "))
start_y = int(input("Nhập vào tọa độ y của ô xuất phát: "))

print("Số ô mà ô xuất phát có thể đến được là:", count_reachable_cells(matrix, start_x - 1, start_y - 1)[0])
