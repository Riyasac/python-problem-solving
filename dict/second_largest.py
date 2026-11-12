marks = {
    'Rashmita': 80,
    'Priyanka': 60,
    'Anita': 70,
    'Advika': 50
}

largest = float('-inf')
second_largest = float('-inf')

for score in marks.values():
    if score > largest:
        second_largest = largest
        largest = score

    elif largest > score > second_largest:
        second_largest = score

for name, score in marks.items():
    if score == second_largest:
        print(name)



# ======== Alternative method to find the second largest value in a dictionary ========
marks = {
    'Rashmita': 80,
    'Priyanka': 60,
    'Anita': 70,
    'Advika': 50
}

second_largest = sorted(marks.values(), reverse=True)[1]

for name, score in marks.items():
    if score == second_largest:
        print(name)