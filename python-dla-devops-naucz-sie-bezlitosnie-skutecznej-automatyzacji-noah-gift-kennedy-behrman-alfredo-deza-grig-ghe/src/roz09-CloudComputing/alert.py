from random import choices

hours = list(range(1,25))
status = ["Alert", "Brak alertu"]
for hour in hours:
    print(f"Godzina: {hour} -- {choices(status)}"
