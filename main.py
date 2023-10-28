from collections import deque


def print_labyrinth(lab: list[str], path: list[tuple[int, int]] = None):
    if path is not None:
        for line_number in range(len(lab)):
            tuple_list = [tuple for tuple in path if tuple[0] == line_number]
            for element in tuple_list:
                lab[line_number] = replace_at_index(lab[line_number], "X", element[1])
    else:
        columns_counter = len(lab[0])
        columns_counter_string = " "
        for i in range(1, columns_counter + 1):
            columns_counter_string += str(i)
            if i == columns_counter + 1:
                columns_counter_string += " "
        lab.insert(0, columns_counter_string)
        lab.append(columns_counter_string)
        for index in range(1, len(lab) - 1):
            lab[index] = str(index) + lab[index] + str(index)
    for line in lab:
        print(line)


def replace_at_index(labyrinth_line: str, replacement: str, index: int) -> str:
    return labyrinth_line[:index] + replacement + labyrinth_line[index + len(replacement):]


def prompt_integer(message: str) -> int:
    print(message)
    x = ""
    while not x.isdigit():
        x = input()
    return x


def prompt_user_for_location(name: str) -> tuple[int, int]:
    row = int(prompt_integer("Row of " + name + ": "))
    column = int(prompt_integer("Column of " + name + ": "))
    return row, column


def bfs(lab: list[str], start: tuple[int, int], end: tuple[int, int]) -> list[tuple[int, int]]:
    # check if start and end tuple exist in labyrinth:
    row_counter = len(lab) - 2
    column_counter = len(lab[0]) - 2
    if start[0] > row_counter or end[0] > row_counter or start[1] > column_counter or end[1] > column_counter:
        return []

    # check if start and end are traversable
    if not is_traversable(lab, start) or not is_traversable(lab, end):
        return []

    already_visited_set = set()
    already_visited_set.add(start)
    goal = tuple(end)
    path = deque([start])
    possible_moves = ((0, 1), (0, -1), (1, 0), (-1, 0))
    dict_of_parents = {}
    # check if deque empty
    while path:
        current = path.popleft()
        if current == end:
            solution_path = []
            current = end
            while current != start:
                solution_path.append(current)
                current = dict_of_parents[current]
            solution_path.append(start)
            solution_path.reverse()
            return solution_path
        for possible_move in possible_moves:
            possible_row = int(current[0]) + int(possible_move[0])
            possible_column = int(current[1]) + int(possible_move[1])
            neighbour = tuple((possible_row, possible_column))
            if is_traversable(lab, neighbour) and neighbour not in already_visited_set:
                path.append(neighbour)
                already_visited_set.add(neighbour)
                dict_of_parents[neighbour] = current

    # if no path could be found
    return []


def is_traversable(lab: list[str], location: tuple[int, int]) -> bool:
    row, column = location
    if lab[row][column] == chr(32):
        return True
    else:
        return False


if __name__ == '__main__':
    space = '\u0020'
    wall = '\u2588'
    labyrinth = [wall + wall + wall + space + space + space + wall + wall + wall + wall,
                 wall + wall + space + space + wall + space + space + space + wall + wall,
                 wall + wall + wall + wall + wall + space + wall + space + wall + wall,
                 wall + wall + space + space + space + space + wall + space + wall + wall,
                 wall + wall + space + wall + wall + wall + wall + space + space + wall,
                 wall + wall + space + space + space + space + space + space + space + wall,
                 wall + space + space + wall + space + wall + wall + space + wall + wall,
                 wall + space + wall + space + space + wall + space + space + wall + wall,
                 wall + space + space + wall + space + space + space + wall + wall + wall]

    print_labyrinth(labyrinth)

    start_row, start_column = prompt_user_for_location("start")
    end_row, end_column = prompt_user_for_location("end")

    res_path = bfs(labyrinth, (start_row, start_column), (end_row, end_column))

    print_labyrinth(labyrinth, res_path)
