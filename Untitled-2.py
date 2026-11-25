graph = {'A':['B','C','D'], 'B':['G'], 'C':['E','F'], 'D':['H'], 'E':[], 'F':[], 'G':[], 'H':[]}
value = {'A':100, 'B':95, 'C':108, 'D':95, 'E':107, 'F':150, 'G':110, 'H':105}
current = 'A'
while graph[current]:
    print("Current:", current, "Value:", value[current])
    neighbor = graph[current][0]
    for x in graph[current]:
        if value[x] > value[neighbor]: neighbor = x
    print("Selected Neighbor:", neighbor, "Value:", value[neighbor])
    if value[neighbor] < value[current]: break
    current = neighbor
    print("Moving to:", current, "\n")
print("Final State:", current, "Value:", value[current])