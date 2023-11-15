def solve_maze(maze, start, end):
    def is_valid_move(x, y):
        # Verificar si la posición es válida y no es una pared.
        if 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] == 0:
            return True
        return False

    def backtrack(x, y):
        # Marcar la celda actual como visitada.
        maze[x][y] = 2

        # Caso base: hemos llegado al destino.
        if (x, y) == end:
            return True

        # Movimientos posibles: arriba, abajo, izquierda, derecha.
        moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for dx, dy in moves:
            new_x, new_y = x + dx, y + dy
            if is_valid_move(new_x, new_y):
                if backtrack(new_x, new_y):
                    return True

        # Si no se encuentra una solución desde esta celda, retroceder.
        maze[x][y] = 0
        return False

    return backtrack(start[0], start[1])

# Ejemplo de uso:
maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0]
]

start = (0, 0)
end = (4, 4)

if solve_maze(maze, start, end):
    print("Se encontró un camino.")
else:
    print("No hay camino disponible.")
