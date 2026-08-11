# Analyzing activity of users

users_day1 = ["ali", "sara", "nahal", "amir", "sara", "reza"]
users_day2 = ["amir", "sara", "tina", "nahal", "sina"]

set1 = set(users_day1)
set2 = set(users_day2)

both_days = set1 & set2
only_day1 = set1 - set2
only_day2 = set2 - set1
non_common = set1 ^ set2

print("Active both days:", both_days)
print("Active only day 1:", only_day1)
print("Active only day 2:", only_day2)
print("Non-common days:", non_common)