import tkinter as tk
from tkinter import messagebox

class EpsilonNFA(object):
    
    def __init__(self, states, alphabet, transition_function, start_state, accept_states):
        self.states = states
        self.alphabet = alphabet
        self.transition_function = transition_function
        self.start_state = start_state
        self.accept_states = accept_states
        self.current_states = {start_state}
    
    def epsilon_closure(self, states):
        epsilon_closures = set(states)
        stack = list(states)

        while stack:
            current_state = stack.pop()
            if (current_state, 'e') in self.transition_function:
                for next_state in self.transition_function[(current_state, 'e')]:
                    if next_state not in epsilon_closures:
                        epsilon_closures.add(next_state)
                        stack.append(next_state)

        return epsilon_closures
    
    def transition_to_states_with_input(self, input_value):
        new_current_states = set()
        for state in self.current_states:
            epsilon_states = self.epsilon_closure({state})
            for epsilon_state in epsilon_states:
                transitions = self.transition_function.get((epsilon_state, input_value), set())
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

# Function to handle button click event
def check_string():
    input_string = entry.get()
    nfa_epsilon.go_to_initial_state()  # Reset the current states
    result_text.delete(1.0, tk.END)  # Clear the previous content
    result_text.insert(tk.END, f"Checking string: {input_string}\n\n")

    for index, inp in enumerate(input_string):
        result_text.insert(tk.END, f"Step {index + 1}: Input = {inp}\n")
        nfa_epsilon.transition_to_states_with_input(inp)
        result_text.insert(tk.END, f"  Current States: {nfa_epsilon.current_states}\n")
        epsilon_states = nfa_epsilon.epsilon_closure(nfa_epsilon.current_states)
        result_text.insert(tk.END, f"  Epsilon Closure: {epsilon_states}\n\n")

    result = nfa_epsilon.in_accept_state()

    if result:
        result_text.insert(tk.END, f"  ==> {input_string} belongs to NFAe.\n\n")
        messagebox.showinfo("Result", f"The string {input_string} belongs to NFAe.")
    else:
        result_text.insert(tk.END, f"  ==> {input_string} does not belong to NFAe.\n\n")
        messagebox.showinfo("Result", f"Error. The string {input_string} does not belong to NFAe.")

# Read NFAe information from file
with open('E:\\Tin học lí thuyết\\Project\\convert\\test1.txt', 'r') as file:
    lines = file.readlines()

states = set(map(int, lines[0].strip().split(',')))
alphabet = set(lines[1].strip().split(','))
start_state = int(lines[2].strip())
accept_states = set(map(int, lines[3].strip().split()))

tf = {}
for line in lines[4:]:
    parts = line.strip().split(',')
    current_state = int(parts[0])
    symbol = parts[1]
    next_states = set(map(int, parts[2].split()))
    tf[(current_state, symbol)] = next_states

# Create EpsilonNFA instance
nfa_epsilon = EpsilonNFA(states, alphabet, tf, start_state, accept_states)

# GUI setup
root = tk.Tk()
root.title("NFAe String Checker")

# Add a label and an entry for input string
label = tk.Label(root, text="Enter a string:")
label.pack(pady=10)
entry = tk.Entry(root)
entry.pack(pady=10)

# Add a Text widget to display intermediate steps
result_text = tk.Text(root, height=10, width=40)
result_text.pack(pady=10)

# Add a button to check the string
button = tk.Button(root, text="Check String", command=check_string)
button.pack(pady=10)

# Run the GUI
root.mainloop()









