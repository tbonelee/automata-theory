class DFA:

    def __init__(self, Q, Sigma, delta, q0, F):
        self.Q = Q # Set of states
        self.Sigma = Sigma # Alphabet
        self.delta = delta # Transition function
        self.q0 = q0 # Start state
        self.F = F # Set of accept states

    def __repr__(self):
        return "DFA({}, {}, {}, {}, {})".format(self.Q, self.Sigma, self.delta, self.q0, self.F)

    def run(self, w):
        q = self.q0
        for a in w:
            q = self.delta.get((q, a), q)  # Use .get to handle unexpected inputs
        return q in self.F

# States
Q = {'Idle', 'MovingUp', 'MovingDown'}

# Input alphabet
Sigma = {'call_to_floor_1', 'call_to_floor_2'}

# Transition function: (current_state, input) -> next_state
delta = {
    ('Idle', 'call_to_floor_1'): 'MovingDown',
    ('Idle', 'call_to_floor_2'): 'MovingUp',
    ('MovingUp', 'call_to_floor_1'): 'MovingDown',  # Assuming it processes the call after reaching the top
    ('MovingDown', 'call_to_floor_2'): 'MovingUp'   # Assuming it processes the call after reaching the bottom
}

# Initial state
q0 = 'Idle'

# Accepting states (in this case, we can consider Idle as the accepting state, indicating the elevator is ready for new commands)
F = {'Idle'}

# Instantiate the DFA
elevator_dfa = DFA(Q, Sigma, delta, q0, F)

# Let's test the DFA with a sequence of commands
commands = ['call_to_floor_2', 'call_to_floor_1']
result = elevator_dfa.run(commands)

print("Elevator state after commands:", result)  # Should return True if it ends in 'Idle', False otherwise
