print("The total number of characters within the string are...")
print(len(puzzle_input))

increase = puzzle_input.count("(")
print(increase)

decrease = puzzle_input.count(")")
print(decrease)

floor = increase - decrease
print(f"Santa ends up on floor number: {floor}")


level = 0
puzzle_dict = []
while level > -1:
    for character in puzzle_input:
        puzzle_dict.append(character)
        if character == '(':
            level += 1
        else:
            level -= 1
            if level == -1:
                break

    print(f"Santa enters the basement at position {len(puzzle_dict)}.")
