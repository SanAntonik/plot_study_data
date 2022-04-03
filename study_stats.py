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
            # day = int(content[0])

            study = content[1].split("_")
            math = int(study[0])
            computer_science = int(study[1])
            english = int(study[2])
            total = math + computer_science + english
            study_time_per_day.append(total)
        # total_study_time = (math + computer_science + english) // 60
        # mean = total_study_time // month_last_day

        return study_time_per_day


def plot_data(data):
    min_count = 0
    for day_total in data:
        print(day_total)
        min_count += day_total
    print(min_count, min_count//60)
    plt.plot(data)
    plt.axhline(y=120, color='r', linestyle='-')
    plt.axhline(y=180, color='b', linestyle='-')
    plt.show()


if __name__ == '__main__':
    data_to_plot_PATH = "C:/Users/San/Documents/inf/time monitoring/Mar 2022 study data.txt"
    print(calculate(data_to_plot_PATH))
    print(plot_data(calculate(data_to_plot_PATH)))
