def print_labyrinth(lab: list[str]):
    columns_counter = len(lab[0])
    columns_counter_string = " "
    for i in range(1, columns_counter+1):
        columns_counter_string += str(i)
        if i == columns_counter+1:
            columns_counter_string += " "
    lab.insert(0, columns_counter_string)
    lab.append(columns_counter_string)
    for index in range(1, len(lab)-1):
        lab[index] = str(index) + lab[index] + str(index)
    for line in lab:
        print(line)


if __name__ == '__main__':
    space = chr(32)
    wall = chr(219)
    print_labyrinth([wall + wall + wall + wall + wall + wall + wall,
                     wall + wall + wall + wall + wall + space + wall,
                     wall + wall + wall + wall + wall + space + wall,
                     wall + wall + space + space + space + space + wall,
                     wall + wall + space + wall + wall + wall + wall,
                     wall + wall + space + space + wall + wall + wall,
                     wall + space + space + wall + wall + wall + wall,
                     wall + space + space + space + space + wall + wall,
                     wall + wall + wall + wall + wall + wall + wall,
                    ])

