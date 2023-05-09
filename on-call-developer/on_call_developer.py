import random
from excel_writer import ExcelWriter


class OnCallDeveloperList:
    def __init__(self, dev_names, weeks=52):
        self.dev_names = dev_names
        self.weeks = weeks
        self.subsitute_names = list(reversed(dev_names))
        self.excel_writer = ExcelWriter(
            ["Week", "On-call-developer", "Substitute"], "on_call_schedule.xlsx")

    def generate(self):
        on_call_devs = []
        subsitutes = []

        for week in range(1, self.weeks + 1):
            index = (week - 1) % len(self.dev_names)

            on_call_dev = self.dev_names[index]
            sub_dev = self.subsitute_names[index]

            # if the on-call developer is the same as the substitute, choose a new substitute
            while sub_dev == on_call_dev:
                sub_index = random.randint(0, len(self.dev_names) - 1)
                sub_dev = self.dev_names[sub_index]

            # if the subsitute is the same as the previous week's on-call developer or substitute, choose a new substitute
            if (week > 1):
                while sub_dev == on_call_devs[week - 2] or sub_dev == subsitutes[week - 2]:
                    sub_index = random.randint(0, len(self.dev_names) - 1)
                    sub_dev = self.dev_names[sub_index]

            on_call_devs.append(on_call_dev)
            subsitutes.append(sub_dev)

            self.excel_writer.add_to_columns(
                week, [week, on_call_dev, sub_dev])

        self.excel_writer.write()


OnCallDeveloperList(['Lynx Lockwood', 'Rex Sharp', 'Nova Frost', 'Avery Steele',
                     'Phoenix Blaze', 'Raven Swift', 'Eliot Voss', 'Sage Harper'], 52).generate()
