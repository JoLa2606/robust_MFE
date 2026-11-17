# Sorts the data according to the state and action the agent is in

# Sorts the policy data at t = 0
with open('output_wpi0.txt', 'r') as file:
    data = file.readlines()

data = [line.split() for line in data]

# Sort by second column
data.sort(key=lambda x: x[1], reverse=False) 

with open('output_wpi0.txt', 'w') as file:
    for line in data:
        file.write(' '.join(line) + '\n')

file.closed

# Sorts the policy data at t = 1
with open('output_wpi1.txt', 'r') as file:
    data = file.readlines()

data = [line.split() for line in data]

# Sort by second column
data.sort(key=lambda x: x[1], reverse=False)

with open('output_wpi1.txt', 'w') as file:
    for line in data:
        file.write(' '.join(line) + '\n')

file.closed

# Sorts the worst-case kernel data at t = 0
with open('output_wp0.txt', 'r') as file:
    data = file.readlines()

data = [line.split() for line in data]

# Sort by second then by third column
data.sort(key=lambda x: (x[1], x[2]), reverse=False) 

with open('output_wp0.txt', 'w') as file:
    for line in data:
        file.write(' '.join(line) + '\n')

file.closed

# Sorts the worst-case kernel data at t = 1
with open('output_wp1.txt', 'r') as file:
    data = file.readlines()

data = [line.split() for line in data]

# Sort by second then by third column
data.sort(key=lambda x: (x[1], x[2]), reverse=False)

with open('output_wp1.txt', 'w') as file:
    for line in data:
        file.write(' '.join(line) + '\n')

file.closed