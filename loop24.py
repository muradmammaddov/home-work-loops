
votes_a = 0
votes_b = 0
votes_c = 0
spoiled = 0

while True:
    vote = input("Vote: ")

    if vote == "end":
        break
    elif vote == "A":
        votes_a += 1
    elif vote == "B":
        votes_b += 1
    elif vote == "C":
        votes_c += 1
    else:
        spoiled += 1

print(f"A: {votes_a} B: {votes_b} C: {votes_c}")
print(f"Spoiled: {spoiled}")

max_votes = max(votes_a, votes_b, votes_c)

winners = []
if votes_a == max_votes:
    winners.append("A")
if votes_b == max_votes:
    winners.append("B")
if votes_c == max_votes:
    winners.append("C")

if len(winners) > 1:
    print("Winner: Tie")
else:
    print(f"Winner: {winners[0]}")