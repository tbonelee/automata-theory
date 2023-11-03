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
            q = self.delta[(q, a)]
        return q in self.F


Q = {0, 1, 2}
Sigma = {"a", "b"}
delta = {(0, "a"): 0, (0, "b"): 1,
         (1, "a"): 2, (1, "b"): 1,
         (2, "a"): 2, (2, "b"): 2}
q0 = 0
F = {0, 1}

D0 = DFA(Q, Sigma, delta, q0, F)

print("D0:", D0)
print("D0.run('ab'):", D0.run("ab"))
print("D0.run('abab'):", D0.run("abab"))
print("D0.run('ababab'):", D0.run("ababab"))
print("D0.run(''):", D0.run(""))