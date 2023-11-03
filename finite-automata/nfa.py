class NFA:
    def __init__(self, states, alphabet, transitions, start_state, accept_states):
        self.states = states # Set of states
        self.alphabet = alphabet # Alphabet
        self.transitions = transitions  # Dictionary of tuples: {(state, symbol): set(next_states)}
        self.start_state = start_state # Start state
        self.accept_states = accept_states # Set of accept states

    def accepts(self, input_str):
        # Start with a set containing the start state
        current_states = {self.start_state}

        for symbol in input_str:
            # Find the set of next states for each current state
            next_states = set()
            # For each current state, find the next states for the current symbol
            for state in current_states:
                # If there is a transition for the current state and symbol, add the next states to the set
                if (state, symbol) in self.transitions:
                    next_states |= self.transitions[(state, symbol)] # Union of sets
            # Set the current states to the next states
            current_states = next_states

        # Check if any of the current states is an accept state
        return any(state in self.accept_states for state in current_states)

# Example usage:
# Accepting strings with an even number of 'a's or 'aaa'
states = {'q0', 'q1', 'q2', 'q3', 'q4', 'q5'}
alphabet = {'a'}
transitions = {
    ('q0', 'a'): {'q1', 'q2'},
    ('q1', 'a'): {'q2'},
    ('q2', 'a'): {'q3'},
    ('q4', 'a'): {'q5'},
    ('q5', 'a'): {'q4'},
}
start_state = 'q0'
accept_states = {'q3', 'q5'}

nfa = NFA(states, alphabet, transitions, start_state, accept_states)

# Test the NFA with some input strings
test_strings = ['', 'a', 'aa', 'aaa', 'aaaa', 'aaaaa', 'aaaaaa']
for test_string in test_strings:
    print(f"{test_string}:", nfa.accepts(test_string))