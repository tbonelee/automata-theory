class MealyMachine:
    def __init__(self, states, input_alphabet, output_alphabet, transition_table):
        self.states = states
        self.input_alphabet = input_alphabet
        self.output_alphabet = output_alphabet
        self.transition_table = transition_table

    def transition(self, state, input):
        if (state, input) not in self.transition_table:
            raise ValueError("Input not in input alphabet")
        next_state, output = self.transition_table[(state, input)]
        if output not in self.output_alphabet:
            raise ValueError("Output not in output alphabet")
        return next_state, output


# Transition table for the binary adder
transition_table = {
    # (current_state, (input1, input2)): (next_state, output)
    ('NO_CARRY', ('0', '0')): ('NO_CARRY', '0'),
    ('NO_CARRY', ('0', '1')): ('NO_CARRY', '1'),
    ('NO_CARRY', ('1', '0')): ('NO_CARRY', '1'),
    ('NO_CARRY', ('1', '1')): ('CARRY', '0'),
    ('CARRY', ('0', '0')): ('NO_CARRY', '1'),
    ('CARRY', ('0', '1')): ('CARRY', '0'),
    ('CARRY', ('1', '0')): ('CARRY', '0'),
    ('CARRY', ('1', '1')): ('CARRY', '1'),
}

# States are 'NO_CARRY' and 'CARRY'
states = {'NO_CARRY', 'CARRY'}
# Input alphabet is all pairs of binary digits
input_alphabet = {('0', '0'), ('0', '1'), ('1', '0'), ('1', '1')}
# Output alphabet is binary digits
output_alphabet = {'0', '1'}

# Create the binary adder Mealy machine with the transition table
binary_adder = MealyMachine(states, input_alphabet, output_alphabet, transition_table)


def adder(bin1, bin2):
    # Ensure the binary strings are of the same length
    if len(bin1) != len(bin2):
        raise ValueError("Binary strings must be of the same length")

    result = ''
    state = 'NO_CARRY'
    # Add from right to left
    for i in range(len(bin1) - 1, -1, -1):
        state, bit = binary_adder.transition(state, (bin1[i], bin2[i]))
        result = bit + result

    # If there is a carry left at the end, prepend it to the result
    if state == 'CARRY':
        result = '1' + result

    return result


# Example usage:
bin1 = "1101"
bin2 = "1011"
print(adder(bin1, bin2))  # Output should be '11000'


if __name__ == '__main__':
    # The MealyMachine class and the adder function are defined as in the previous message.

    # Example usage:
    # Test case 1: No carryover in any bit addition
    bin1 = "1010"
    bin2 = "0101"
    print(f"Adding {bin1} and {bin2}: {adder(bin1, bin2)}")  # Output should be '1111'

    # Test case 2: Carryover in the last bit addition
    bin1 = "1001"
    bin2 = "0110"
    print(f"Adding {bin1} and {bin2}: {adder(bin1, bin2)}")  # Output should be '1111'

    # Test case 3: Carryover in one of the middle bit additions
    bin1 = "1101"
    bin2 = "1011"
    print(f"Adding {bin1} and {bin2}: {adder(bin1, bin2)}")  # Output should be '11000'

    # Test case 4: All bits are 1 and result in a carryover
    bin1 = "1111"
    bin2 = "1111"
    print(f"Adding {bin1} and {bin2}: {adder(bin1, bin2)}")  # Output should be '11110'

    # Test case 5: Adding zeros
    bin1 = "0000"
    bin2 = "0000"
    print(f"Adding {bin1} and {bin2}: {adder(bin1, bin2)}")  # Output should be '0000'

    # Test case 6: Different combinations of 1s and 0s
    bin1 = "101010"
    bin2 = "010101"
    print(f"Adding {bin1} and {bin2}: {adder(bin1, bin2)}")  # Output should be '111111'

    # Test case 7: Single bit addition
    bin1 = "1"
    bin2 = "1"
    print(f"Adding {bin1} and {bin2}: {adder(bin1, bin2)}")  # Output should be '10'
