import random

class TicTacToeEnvironment:
    def __init__(self):
        self.board = [' '] * 9

    def display_board(self):
        for i in range(0, 9, 3):
            print(f"{self.board[i]} | {self.board[i + 1]} | {self.board[i + 2]}")
        print("---------")

    def available_moves(self):
        return [i for i, val in enumerate(self.board) if val == ' ']

    def make_move(self, position, symbol):
        self.board[position] = symbol

    def check_winner(self, symbol):
        winning_combos = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]
        for combo in winning_combos:
            if all(self.board[i] == symbol for i in combo):
                return True
        return False

class MonteCarloAgent:
    # ... (other code remains the same)

    def choose_action(self, environment):
        possible_moves = environment.available_moves()

        if not possible_moves:  # If no available moves, return None
            return None

        best_value = -1
        best_move = None

        for move in possible_moves:
            environment.make_move(move, self.symbol)
            state = ''.join(environment.board)
            environment.make_move(move, ' ')

            if state not in self.states_value:
                self.states_value[state] = 0.5

            if self.states_value[state] > best_value:
                best_value = self.states_value[state]
                best_move = move

        return best_move


def play_game(agent1, agent2):
    env = TicTacToeEnvironment()
    agents = [agent1, agent2]
    current_agent_idx = random.choice([0, 1])

    episode_states = []
    rewards = []

    while not env.check_winner('X') and not env.check_winner('O') and len(env.available_moves()) > 0:
        current_agent = agents[current_agent_idx]
        move = current_agent.choose_action(env)

        if move is None:  # Handle case where move is None
            break

        env.make_move(move, current_agent.symbol)
        state = ''.join(env.board)
        episode_states.append(state)

        # Rest of the code remains the same

    env = TicTacToeEnvironment()
    agents = [agent1, agent2]
    current_agent_idx = random.choice([0, 1])

    episode_states = []
    rewards = []

    while not env.check_winner('X') and not env.check_winner('O') and len(env.available_moves()) > 0:
        current_agent = agents[current_agent_idx]
        move = current_agent.choose_action(env)
        env.make_move(move, current_agent.symbol)
        state = ''.join(env.board)
        episode_states.append(state)

        if env.check_winner(current_agent.symbol):
            rewards.extend([1 if i % 2 == current_agent_idx else -1 for i in range(len(episode_states))])
            break
        elif len(env.available_moves()) == 0:
            rewards.extend([0 for _ in range(len(episode_states))])

        current_agent_idx = 1 - current_agent_idx

    agents[0].update_value_function(episode_states, rewards)
    agents[1].update_value_function(episode_states, rewards)

# Create agents
agent_X = MonteCarloAgent('X')
agent_O = MonteCarloAgent('O')

# Train agents through self-play
for _ in range(10000):
    play_game(agent_X, agent_O)

# Evaluation against a random player
class RandomPlayer:
    def __init__(self, symbol):
        self.symbol = symbol  # Define the symbol attribute for RandomPlayer

    def choose_action(self, environment):
        return random.choice(environment.available_moves())


# Evaluation against a random player
def evaluate(agent, opponent, num_games):
    wins = 0
    for _ in range(num_games):
        env = TicTacToeEnvironment()
        agents = [agent, opponent(symbol='O')]  # Pass the symbol to RandomPlayer
        current_agent_idx = random.choice([0, 1])

        while not env.check_winner('X') and not env.check_winner('O') and len(env.available_moves()) > 0:
            current_agent = agents[current_agent_idx]
            move = current_agent.choose_action(env)
            env.make_move(move, current_agent.symbol)

            if env.check_winner(current_agent.symbol):
                wins += 1 if current_agent_idx == 0 else 0
                break
            elif len(env.available_moves()) == 0:
                break

            current_agent_idx = 1 - current_agent_idx

    win_rate = wins / num_games
    print(f"Win rate against the opponent: {win_rate}")

# Evaluate agent against a random player
evaluate(agent_X, RandomPlayer, 1000)  # Pass the class itself, not an instance

