
shapes = {
    "A": "rock",
    "B": "paper",
    "C": "scissors",
    "X": "rock",
    "Y": "paper",
    "Z": "scissors"
}

points = {
    "rock": 1,
    "paper": 2,
    "scissors": 3
}

run_points = {
    "win": 6,
    "tie": 3,
    "lose": 0
}

pointsLu = [
    ("A X", 3 + 1),
    ("A Y", 6 + 2),
    ("A Z", 0 + 3),
    ("B X", 0 + 1),
    ("B Y", 3 + 2),
    ("B Z", 6 + 3),
    ("C X", 6 + 1),
    ("C Y", 0 + 2),
    ("C Z", 3 + 3)
]

wins = ["A Y", "B Z", "C X"]
losses = ["A Z", "B X", "C Y"]
ties = ["A X", "B Y", "C Z"]

with open('day2_input.txt', 'r') as file:
    data = file.read()
file.close()

total = 0
for line in data.splitlines():
    if line in wins:
        lookupRun = "win"
        table = "wins"
    elif line in losses:
        lookupRun = "lose"
        table = "losses"
    elif line in ties:
        lookupRun = "tie"
        table = "ties"

    shape_points =  points[shapes[line.split()[1]]]
    _run_points = run_points[lookupRun]

    total += shape_points + _run_points
    
print(total)

total = 0
for line in data.splitlines():
    shape,outcome = line.split(" ")
    if outcome == 'Z':
        table = wins
        run_points = 6
    elif outcome == 'X':
        table = losses
        run_points = 0
    elif outcome == 'Y':
        table = ties
        run_points = 3
    
    neededShape = [idx for idx in table if idx[0] == shape][0]

    total += (points[shapes[neededShape.split()[1]]])
    total += run_points

print(total)
