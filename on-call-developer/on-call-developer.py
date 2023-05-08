import random
import pandas as pd

dev_names = ['Lynx Lockwood', 'Rex Sharp', 'Nova Frost', 'Avery Steele',
             'Phoenix Blaze', 'Raven Swift', 'Eliot Voss', 'Sage Harper']
subsitute_names = list(reversed(dev_names))

schedule = pd.DataFrame(columns=["Week", "On-call-developer", "Substitute"])

on_call_devs = []
subsitutes = []

for week in range(1, 53):
    index = (week - 1) % len(dev_names)

    on_call_dev = dev_names[index]
    sub_dev = subsitute_names[index]

    # if the on-call developer is the same as the substitute, choose a new substitute
    while sub_dev == on_call_dev:
        sub_index = random.randint(0, len(dev_names) - 1)
        sub_dev = dev_names[sub_index]

    # if the subsitute is the same as the previous week's on-call developer or substitute, choose a new substitute
    if (week > 1):
        while sub_dev == on_call_devs[week - 2] or sub_dev == subsitutes[week - 2]:
            sub_index = random.randint(0, len(dev_names) - 1)
            sub_dev = dev_names[sub_index]

    on_call_devs.append(on_call_dev)
    subsitutes.append(sub_dev)

    schedule.loc[week] = [week, on_call_dev, sub_dev]

schedule.to_excel("on_call_schedule.xlsx", index=False)

print(schedule)
