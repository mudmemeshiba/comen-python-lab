distance = int(input("Distance from starting point(m.): "))

l_move = []
move = 0
count = 0
while move != distance:
    while move <= distance:
        move += 5
        l_move.append(move)
        move -= 2
        l_move.append(move)
        count += 1
        if move > distance:
            break
    move -= 4
    l_move.append(move)
    move += 3
    l_move.append(move)
    count += 1
    if move == distance:
        break
if move == 0:
    l_move.append(move)
print(*l_move)
print(f"Buzz moved {count} set(s)")