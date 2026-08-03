# List Methods

scores = [18, 20, 16, 9, 15]

print("avg_score:", sum(scores) / len(scores))
print("min_score:", min(scores))
print("max_score:", max(scores))

print("reversed_list:", list(reversed(scores)))  # معکوس
print("sorted_scores (asc):", sorted(scores)) # صعودی
print("sorted_scores (desc):", sorted(scores, reverse=True)) # نزولی

scores.sort()
print("new_list:", scores) # لیست اصلی به مرتب شده تغییر کرد

scores.sort(reverse=True)
print("new_list:", scores)


filtered = [s for s in scores if s >= 10]
print("filtered:", filtered)

print("filtered:", list(filter(lambda s: s >= 10, scores)))

