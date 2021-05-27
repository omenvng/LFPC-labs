import pandas as pd

nfa = {}                                 
file1 = open('input.txt', 'r')
Lines = file1.readlines()
temp = Lines[0].strip()
n = int(temp[0])
t = int(temp[2])
for i in range(1,t+1):
    str = Lines[i].split('=') # linia parsata
    state = str[1]
    state = "".join(str[1]).split(',')[0].rstrip('\n') 
    print([state])
    nfa[state] = {}
    path = str[0].split(',')
    path = " ".join(path) 
    nfa[state][str[0].split(',')[1]] = str[0].split(',')[0] # nfa[q][a] = q
final_state = Lines[t+1].split("F={")[1].split("}")[0] #final state
# print(final_state)
# print(nfa)                                    
print("\nNFA table")
nfa_table = pd.DataFrame(nfa)
print(nfa_table.transpose())

print("Enter final state of NFA : ")
nfa_final_state = final_state     

new_states_list = []                          
dfa = {}                                      
keys_list = list(list(nfa.keys()))
print(list(nfa.keys()), ' ddddddddddddd')
print(keys_list[0])                  
path_list = list(nfa[keys_list[0]].keys())    

dfa[keys_list[0]] = {}                        
for y in range(1, t):
    var = "".join(nfa[keys_list[0]][path_list[y]])   
    dfa[keys_list[0]][path_list[y]] = var            
    if var not in keys_list:                         
        new_states_list.append(var)                  
        keys_list.append(var)                        
while len(new_states_list) != 0:                     
    dfa[new_states_list[0]] = {}                     
    for _ in range(len(new_states_list[0])):
        for i in range(len(path_list)):
            temp = []                                
            for j in range(len(new_states_list[0])):
                temp += nfa[new_states_list[0][j]][path_list[i]]  
            s = ""
            s = s.join(temp)                         
            if s not in keys_list:                   
                new_states_list.append(s)            
                keys_list.append(s)                  
            dfa[new_states_list[0]][path_list[i]] = s   
        
    new_states_list.remove(new_states_list[0])       

print("\ndfa table ")
dfa_table = pd.DataFrame(dfa)
print(dfa_table.transpose())

dfa_states_list = list(dfa.keys())
dfa_final_states = []
for x in dfa_states_list:
    for i in x:
        if i in nfa_final_state:
            dfa_final_states.append(x)
            break
        
print("\nFinal states  ",dfa_final_states)  