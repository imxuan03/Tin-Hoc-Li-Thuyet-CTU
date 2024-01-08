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
        
        print(new_current_states, end="->")
        print(self.epsilon_closure(new_current_states))

        self.current_states = new_current_states
    
    def in_accept_state(self):
        return bool(self.current_states.intersection(self.accept_states))
    
    def go_to_initial_state(self):
        self.current_states = {self.start_state}
    
    def run_with_input_list(self, input_list):
        self.go_to_initial_state()
        s = ''
        for inp in input_list:
            s+=inp
            print('(',self.start_state , ',' ,s ,') = ', end="")
            self.transition_to_states_with_input(inp)
        
        return self.in_accept_state()

L = input("Hãy nhập chuỗi cần kiểm tra có thuộc NFAe vào : ")
current_states = {L[0]}
# print("L 0 = ", L[0])

# Mở tệp để đọc
with open('E:\\Tin học lí thuyết\\Project\\convert\\test1.txt', 'r') as file:
    # Đọc các dòng từ tệp
    lines = file.readlines()

# Xây dựng các biến từ dữ liệu đọc được
states = set(lines[0].strip().split(','))
alphabet = set(lines[1].strip().split(','))
# print("aphabet là " , alphabet)
start_state = lines[2].strip()
accept_states = set( lines[3].strip().split(','))



tf = {}
for line in lines[4:]:
    # Chia dòng thành các phần tách bởi dấu phẩy
    parts = line.strip().split(',')

    # Chuyển đổi dữ liệu thành các kiểu phù hợp
    current_state = parts[0]
    symbol = parts[1]
    next_states = set( parts[2].split())

    # Thêm vào từ điển chuyển trạng thái
    tf[(current_state, symbol)] = next_states

# In ra các biến để kiểm tra
print("States:", states)
print("Alphabet:", alphabet)
print("Start State:", start_state)
print("Accept States:", accept_states)
print("Transition Function:", tf)


print("\nTrạng thái chuyển Epsilon là : ")
nfa_epsilon = EpsilonNFA(states, alphabet, tf, start_state, accept_states)

if(nfa_epsilon.run_with_input_list(L)):
    print("=> Chuỗi ", L, " thuộc NFAe")
else:
    print("=> Error. Chuỗi ", L, " không thuộc NFAe")
