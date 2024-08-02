'''user gives data like this…………………………………………………………………….
kerala-tiruvanantapuram	karnataka-bengaluru	tamilnadu-chennai
You have to separate the states and store in the list states[] and also the separated capitals must be stored in capitals[]'''

data=input("Enter state and capitals")
states = []
capitals = []

# Split the input data by space to get each state-capital pair
pairs = data.split()
print(pairs)

for pair in pairs:
    # Split each pair by the hyphen to separate state and capital
    state, capital = pair.split('-')
    states.append(state)
    capitals.append(capital)

# Print the results
print("States:", states)
print("Capitals:", capitals)