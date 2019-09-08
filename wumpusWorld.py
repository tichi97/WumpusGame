import random

board = [
    ['S', '0', 'B','P'],
    ['W', ['B','S','G'], 'P','B'],
    ['S', '0', 'B','0'],
    ['0', 'B', 'P','B']
]

mygraph = {'00': set(['01','10']),
               '01': set(['00','11','02']),
               '02': set(['01','12','03']),
               '03': set(['02','13']),
               '10': set(['00','11','20']),
               '11': set(['10','01','12','21']),
               '12': set(['11','02','13','22']),
               '13': set(['12','03','23']),
               '20': set(['10','21','30']),
               '21': set(['11','20','31','22']),
               '22': set(['21','12','23','32']),
               '23': set(['13','22','33']),
               '30': set(['20','31']),
               '31': set(['21','30','32']),
               '32': set(['22','32','33']),
               '33': set(['23','32'])
        }

safe_states={
'00':['N', 'N'],
               '01': ['N', 'N'],
               '02': ['N', 'N'],
               '03': ['N', 'N'],
               '10': ['N', 'N'],
               '11': ['N', 'N'],
               '12': ['N', 'N'],
               '13': ['N', 'N'],
               '20': ['N', 'N'],
               '21': ['N', 'N'],
               '22': ['N', 'N'],
               '23': ['N', 'N'],
               '30': ['N', 'N'],
               '31': ['N', 'N'],
               '32': ['N', 'N'],
               '33': ['N', 'N']
}
safe_positions={
'00':0,
               '01': 0,
               '02': 0,
               '03': 0,
               '10': 0,
               '11': 0,
               '12': 0,
               '13': 0,
               '20': 0,
               '21': 0,
               '22': 0,
               '23': 0,
               '30': 0,
               '31': 0,
               '32': 0,
               '33': 0
}

start = "30"

def curr_state(value,pos):
    if value == 'B':
        safe_states[pos][0]='B'
    elif value == 'S':
        safe_states[pos][1] = 'S'
    return safe_states[pos]

def choose_path(start,graph):
    p=[]
    p.append(start)
    current=start
    i=0
    safe_moves = set()
    while start:
        moves=[]
        pos=[int(current[0]), int(current[1])]
        current_state = curr_state(board[pos[0]][pos[1]],current)
        print("currently at ", current, "with the state ", current_state, " and safety ", safe_positions[current])

        if board[pos[0]][pos[1]] == "G" or "G" in board[pos[0]][pos[1]]:
            print("WINNER!")
            return p

        if current_state == ['N', 'N']:
            safe_positions[current] = "OK"
            for next in graph[current]:
                safe_positions[next] = "OK"
                moves.append(next)
        elif "B" in current_state and "S" in current_state:
            for next in graph[current]:
                if safe_positions[next] != "OK":
                    print(next, " may be a Pit and Wumpus")
                    safe_positions[next] = "PW?"
                    #pass
                    # this next may have a breeze
                moves.append(next)
        elif "B" in current_state:
            for next in graph[current]:
                if safe_positions[next] != "OK":
                    if safe_positions[next] == "W?":
                        safe_positions[next] == "OK"
                        moves.append(next)
                    else:
                        print(next, " may be a Pit")
                        safe_positions[next] = "P?"
                else:
                    moves.append(next)

        elif "S" in current_state:
            for next in graph[current]:
                if safe_positions[next] != "OK":
                    if safe_positions[next] == "P?":
                        safe_positions[next] == "OK"
                        moves.append(next)
                    else:
                        print(next, " may be a Wumpus")
                        safe_positions[next] = "W?"
                else:
                    moves.append(next)
        # elif current_state=="OK":
        #     safe_moves.append(next)
        if moves == []:
            current = p[-2]
            p.pop()
            continue

        current = random.choice(moves)
        p.append(current)
        print(safe_moves)
        i=i+1
    return p

print(choose_path(start,mygraph))
