from collections import deque


def print_labyrinth(lab: list[str], path: list[tuple[int, int]] = None):
    if path is not None:
        for line_index, line in enumerate(lab):
            result_tuple_list = [path_tuple for path_tuple in path]
            for element in result_tuple_list:
                if element[0] == line_index:
                    line = replace_at_index(line, "X", element[1])
            print(line)
    else:
        number_of_columns = len(lab[0])
        column_label = "".join(str(i + 1) for i in range(number_of_columns))
        lab.insert(0, " " + column_label)
        lab.append(" " + column_label)
        for index, line in enumerate(lab):
            if index not in [0, len(lab) - 1]:
                lab[index] = "".join([str(index), lab[index], str(index)])
            print(lab[index])


def replace_at_index(labyrinth_line: str, replacement: str, index: int) -> str:
    return labyrinth_line[:index] + replacement + labyrinth_line[index + len(replacement):]


def prompt_integer(message: str) -> int:
    print(message)
    x = ""
    while not x.isdigit():
        x = input()
    return x


def check_if_in_labyrinth_and_traversable(lab: list[str], point: tuple[int, int]) -> bool:
    row_counter = len(lab) - 2
    column_counter = len(lab[0]) - 2
    if point[0] > row_counter or point[1] > column_counter:
        return False
    if not is_traversable(lab, point) or not is_traversable(lab, point):
        return False
    return True


def prompt_user_for_location(name: str) -> tuple[int, int]:
    row = int(prompt_integer("Row of " + name + ": "))
    column = int(prompt_integer("Column of " + name + ": "))
    return row, column


def bfs(lab: list[str], start: tuple[int, int], end: tuple[int, int]) -> list[tuple[int, int]]:
    already_visited_set = set()
    already_visited_set.add(start)
    path = deque([start])
    possible_moves = ((0, 1), (0, -1), (1, 0), (-1, 0))
    dict_of_parents = {}

    while path:
        current = path.popleft()
        if end in already_visited_set:
            solution_path = []
            current = end
            while current != start:
                solution_path.append(current)
                current = dict_of_parents[current]
            solution_path.append(start)
            solution_path.reverse()
            return solution_path
        for move_to_consider in possible_moves:
            row_to_consider = int(current[0]) + int(move_to_consider[0])
            column_to_consider = int(current[1]) + int(move_to_consider[1])
            neighbour = tuple((row_to_consider, column_to_consider))
            if neighbour not in already_visited_set and is_traversable(lab, neighbour):
                print(neighbour)
                path.append(neighbour)
                already_visited_set.add(neighbour)
                dict_of_parents[neighbour] = current

    # if no path could be found
    return []


def is_traversable(lab: list[str], location: tuple[int, int]) -> bool:
    row, column = location
    if lab[row][column] == '\u0020':
        return True
    else:
        return False


if __name__ == '__main__':
    space = '\u0020'
    wall = '\u2588'
    labyrinth = [f"{wall}{wall}{wall}{space}{space}{space}{wall}{wall}{wall}{wall}",
                 f"{wall}{wall}{space}{space}{wall}{space}{space}{space}{wall}{wall}",
                 f"{wall}{wall}{wall}{wall}{wall}{space}{wall}{space}{wall}{wall}",
                 f"{wall}{wall}{space}{space}{space}{space}{wall}{space}{wall}{wall}",
                 f"{wall}{wall}{space}{wall}{wall}{wall}{wall}{space}{space}{wall}",
                 f"{wall}{wall}{space}{space}{space}{space}{space}{space}{space}{wall}",
                 f"{wall}{space}{space}{wall}{space}{wall}{wall}{space}{wall}{wall}",
                 f"{wall}{space}{wall}{space}{space}{wall}{space}{space}{wall}{wall}",
                 f"{wall}{space}{space}{wall}{space}{space}{space}{wall}{wall}{wall}"]

    print_labyrinth(labyrinth)

    starting_point = ()
    end_point = ()
    valid_locations = [False, False]
    while not valid_locations[0]:
        starting_point = prompt_user_for_location("start")
        valid_locations[0] = check_if_in_labyrinth_and_traversable(labyrinth, starting_point)
    while not valid_locations[1]:
        end_point = prompt_user_for_location("end")
        valid_locations[1] = check_if_in_labyrinth_and_traversable(labyrinth, end_point)

    res_path = bfs(labyrinth, starting_point, end_point)

    print_labyrinth(labyrinth, res_path)
