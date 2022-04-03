import matplotlib.pyplot as plt


def calculate(PATH):
    with open(PATH, "r") as f:
        data = f.read()
        lines = data.splitlines()
        # month = lines[0]

        # math = 0
        # computer_science = 0
        # english = 0
        study_time_per_day = []
        for line in lines[1::]:
            content = line.split(":")
            # if lines[-1] == line:
            #     sport = int(content[2])
            #     month_last_day = int(content[0])
            day = int(content[0])

            study = content[1].split("_")
            math = int(study[0])
            computer_science = int(study[1])
            english = int(study[2])
            total = (math + computer_science + english) // 60
            study_time_per_day.append((day, total))
        # total_study_time = (math + computer_science + english) // 60
        # mean = total_study_time // month_last_day

        return study_time_per_day


if __name__ == '__main__':
    data_to_plot_PATH = "C:/Users/San/Documents/inf/time monitoring/Mar 2022 study data.txt"
    print(calculate(data_to_plot_PATH))