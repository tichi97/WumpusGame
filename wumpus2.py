import random

class Environment:
    board = [
        ['S', '0', 'B', 'P'],
        ['W', ['B', 'S', 'G'], 'P', 'B'],
        ['S', '0', 'B', '0'],
        ['0', 'B', 'P', 'B']
    ]
    board_positions = [
        ['00', '01', '02', '03'],
        ['10', '11', '12', '13'],
        ['20', '21', '22', '23'],
        ['30', '31', '32', '33'],
    ]
    strikes = 1
    mygraph = {'00': set(['01', '10']),
               '01': set(['00', '11', '02']),
               '02': set(['01', '12', '03']),
               '03': set(['02', '13']),
               '10': set(['00', '11', '20']),
               '11': set(['10', '01', '12', '21']),
               '12': set(['11', '02', '13', '22']),
               '13': set(['12', '03', '23']),
               '20': set(['10', '21', '30']),
               '21': set(['11', '20', '31', '22']),
               '22': set(['21', '12', '23', '32']),
               '23': set(['13', '22', '33']),
               '30': set(['20', '31']),
               '31': set(['21', '30', '32']),
               '32': set(['22', '32', '33']),
               '33': set(['23', '32'])
               }

    safe_states = {
        '00': ['N', 'N'],
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

    start = "30"

class Agent:
    def curr_state(value, pos,safe_states):
        if value == 'B':
            safe_states[pos][0] = 'B'
        elif value == 'S':
            safe_states[pos][1] = 'S'
        return safe_states[pos]

    def check_lose(pos,board):
        val = [int(pos[0]), int(pos[1])]
        if board[val[0]][val[1]] == 'W' or board[val[0]][val[1]] == 'P':
            print("GAME OVER! YOU LOST!")
            return 0

    def check_move(current,board,safe_states):
        pos = [int(current[0]), int(current[1])]
        current_state = Agent.curr_state(board[pos[0]][pos[1]], current,safe_states)
        if current_state == ['N', 'N']:
            print("Position ", current, "is clear")
        elif "B" in current_state and "S" in current_state:
            print("Warning! Pit and/or Wumpus nearby")
        elif "B" in current_state:
            print("Pit nearby")
        elif "S" in current_state:
            print("Wumpus nearby")

    def check_strike(strikes, current,board,graph):
        strike = input("Would you like to strike a nearby position? Yes or no ").lower()
        if strike == "yes":
            strike_pos = input("Which position out of these out of your possible moves: ")
            while strike_pos not in graph[current]:
                strike_pos = input("Please choose a valid option")
            if board[int(strike_pos[0])][int(strike_pos[1])] == "W" or "W" in board[int(strike_pos[0])][
                int(strike_pos[1])]:
                print("You killed the Wumpus! Now find the gold and ignore the stink")
                board[int(strike_pos[0])][int(strike_pos[1])] = "0"
            else:
                print("Sorry no Wumpus there. Be careful!")
            strikes = 0
            print("You now have no more strikes left")
        return strikes

    def collection(current,board):
        collect = input("Would you like to collect here? Yes or no ").lower()
        if collect == "yes":
            if board[int(current[0])][int(current[1])] == "G" or "G" in board[int(current[0])][int(current[1])]:
                print("WINNER! YOU FOUND THE GOLD!")
                return 0
            else:
                print("Nothing to collect here")


    def play_game(start,graph,strikes,board,safe_states):
        current=start
        i=0
        while True:
            print("----------------------------------------------------------------------------------------------------")
            print("Current position: ",current," Possible moves are: ", graph[current])
            Agent.check_move(current,board,safe_states)

            if Agent.collection(current,board) == 0:
                break

            if strikes>0:
                strikes=Agent.check_strike(strikes,current,board,graph)
            move = input("Where do you want to move to? ")
            while move not in graph[current]:
                move = input("Please choose a valid option")
            if Agent.check_lose(move,board) == 0:
                break
            current = move

    def __init__(self,Environment):
        Agent.play_game(Environment.start,Environment.mygraph,Environment.strikes,Environment.board,Environment.safe_states)





theEnvironment = Environment()
print("These are the board positions. You are at 30")
for i in theEnvironment.board_positions:
    print(i)
theAgent = Agent(theEnvironment)
# play_game(start,mygraph,strikes)

