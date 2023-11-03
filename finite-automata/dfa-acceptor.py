class DFA:
    def __init__(self, Q, Sigma, delta, q0, F):
        self.Q = Q                  # Set of states
        self.Sigma = Sigma          # Alphabet
        self.delta = delta          # Transition function
        self.q0 = q0                # Start state
        self.F = F                  # Set of accept states

    def run(self, w):
        q = self.q0
        for a in w:
            q = self.delta[(q, a)]
            if q == 'dead':
                break
        return q in self.F

# Define the states
Q = {'start', 'open_quote', 'inside', 'close_quote', 'dead'}

# Define the alphabet: double quote, letter 'a', and space
Sigma = {'"', 'a', ' '}

# Define the transition function with explicit 'dead' state transitions
delta = {
    ('start', '"'): 'open_quote',
    ('start', 'a'): 'dead',
    ('start', ' '): 'dead',
    ('open_quote', 'a'): 'inside',
    ('open_quote', ' '): 'inside',
    ('open_quote', '"'): 'close_quote',
    ('inside', 'a'): 'inside',
    ('inside', ' '): 'inside',
    ('inside', '"'): 'close_quote',
    # Transitions to 'dead' state when an invalid input is read
    ('close_quote', '"'): 'dead',
    ('close_quote', 'a'): 'dead',
    ('close_quote', ' '): 'dead',
    ('dead', '"'): 'dead',
    ('dead', 'a'): 'dead',
    ('dead', ' '): 'dead',
    # You can add more 'dead' transitions for any other character if the alphabet is larger
}

# Define the start state
q0 = 'start'

# Define the accept states
F = {'close_quote'}

# Initialize the DFA
quotes_dfa = DFA(Q, Sigma, delta, q0, F)

# Examples
tokens = ['"a"', '"aa"', '" "', '"a a"', '"aaa"', '""', '"a"', '" a"', '"a "', '"aa" "', '" "',
    '"', ' "', 'a"', 'a "', 'a', 'a ', ' ', 'a a', 'a a ', 'a a a', 'a a a ', 'a a a a', 'a a a a ']

for token in tokens:
    if quotes_dfa.run(token):
        print(f"OK - |{token}| is a valid string.")
    else:
        print(f"WRONG - |{token}| is not a valid string.")
