class DFA:
    def __init__(self, Q, Sigma, delta, q0, F):
        self.Q = Q  # Set of states
        self.Sigma = Sigma  # Alphabet
        self.delta = delta  # Transition function
        self.q0 = q0  # Start state
        self.F = F  # Set of accept states

    def run(self, w):
        q = self.q0
        for a in w:
            q = self.delta.get((q, a), 'dead')  # Use 'dead' state for invalid transitions
            if q == 'dead':
                break
        return q in self.F


# Define the states
Q = {'start', 'letter1', 'digit1', 'digit2', 'digit3', 'letter2', 'letter3', 'dead'}

# Define the alphabet: uppercase letters and digits
Sigma = set(chr(i) for i in range(65, 91)) | set(chr(i) for i in range(48, 58))

# Define the transition function
delta = {}

# Start with a letter
for letter in set(chr(i) for i in range(65, 91)):
    delta[('start', letter)] = 'letter1'

# Followed by three digits
for digit in set(chr(i) for i in range(48, 58)):
    delta[('letter1', digit)] = 'digit1'
    delta[('digit1', digit)] = 'digit2'
    delta[('digit2', digit)] = 'digit3'

# End with two letters
for letter in set(chr(i) for i in range(65, 91)):
    delta[('digit3', letter)] = 'letter2'
    delta[('letter2', letter)] = 'letter3'

# Define the start state
q0 = 'start'

# Define the accept states
F = {'letter3'}

# Initialize the DFA
serial_dfa = DFA(Q, Sigma, delta, q0, F)

# Examples
serial_numbers = ['A123BC', 'B001XY', 'C789ZZ', 'D1234E', 'EXYZ', '123ABC', 'A12B34']

for serial in serial_numbers:
    if serial_dfa.run(serial):
        print(f"'{serial}' is a valid serial number.")
    else:
        print(f"'{serial}' is not a valid serial number.")
