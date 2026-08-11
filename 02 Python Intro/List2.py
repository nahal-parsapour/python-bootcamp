# more challenge for Lists

scores = [12, 18, 7, 20, 15, 20, 9, 18, 14]

duplicated = {s for s in scores if scores.count(s) > 1}

avg = sum(scores) / len(scores)
filtered = [s for s in scores if s >= avg]

unique_scores = list(set(scores))

sorted_desc = sorted(scores, reverse=True)

max_score = max(scores)
second_max = max(s for s in scores if s != max_score)

print("Duplicated:", duplicated)
print("Avg:", avg)
print("Unique scores:", unique_scores)
print("Sorted descending:", sorted_desc)
print("Second Max:", second_max)