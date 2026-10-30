def replace_value(values, index, new_value):
    values[index] = new_value
    return None
def find_first(values, target):
    for i in range(len(values)):
        if values[i] == target:
            return i
    return -1
def summarize(values):
    return min(values), max(values), sum(values)
num_days = int(input("Enter the number of days: "))
original = []
for _ in range(num_days):
    emails = int(input("Enter the number of emails received: "))
    original.append(emails)
updated = original[:]
index = int(input("Enter the index to correct: "))
new_value = int(input("Enter the new number of emails: "))
replace_value(updated, index, new_value)
target = int(input("Enter the number of emails to search for: "))
first_index = find_first(updated, target)
match_count = updated.count(target)
minimum, maximum, total = summarize(updated)
sorted_list = sorted(updated)
print(f"Original: {original}")
print(f"Updated: {updated}")
print(f"Sorted: {sorted_list}")
print(f"Minimum number of emails: {minimum}")
print(f"Maximum number of emails: {maximum}")
print(f"Total number of emails: {total}")
if first_index == -1:
    print("Target not found")
else:
    print(f"First matching index: {first_index}")
print(f"Matching values: {match_count}")