class NFA(object):
    
    def __init__(self, states, alphabet, transition_function, start_state, accept_states):
        self.states = states
        self.alphabet = alphabet
        self.transition_function = transition_function
        self.start_state = start_state
        self.accept_states = accept_states
        self.current_states = {start_state}
    
    def transition_to_states_with_input(self, input_value):
        new_current_states = set()
        for state in self.current_states:
            transitions = self.transition_function.get((state, input_value), set())
            new_current_states.update(transitions)
        
        self.current_states = new_current_states
    
    def in_accept_state(self):
        return bool(self.current_states.intersection(self.accept_states))
    
    def go_to_initial_state(self):
        self.current_states = {self.start_state}
    
    def run_with_input_list(self, input_list):
        self.go_to_initial_state()
        for inp in input_list:
            self.transition_to_states_with_input(inp)
        
        return self.in_accept_state()

# Example usage:
states = {0, 1, 2, 3, 4}
alphabet = {'0', '1'}
start_state = 0
accept_states = {2, 4}

tf = {}
tf[(0, '0')] = {0, 3}
tf[(0, '1')] = {0, 1}
tf[(1, '0')] = set()
tf[(1, '1')] = {2}
tf[(2, '0')] = {2}
tf[(2, '1')] = {2}
tf[(3, '0')] = {4}
tf[(3, '1')] = set()
tf[(4, '0')] = {4}
tf[(4, '1')] = {4}

L = list('111')
current_states = {0}

nfa1 = NFA(states, alphabet, tf, start_state, accept_states)

print(nfa1.run_with_input_list(L))
