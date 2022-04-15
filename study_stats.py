import matplotlib.pyplot as plt
import math


def calculate(PATH):
    with open(PATH, "r") as f:
        data = f.read()
        lines = data.splitlines()
        month = lines[0]

        # maths = 0
        # computer_science = 0
        # english = 0
        study_time_per_day = []
        for line in lines[1::]:
            content = line.split(":")
            if lines[-1] == line:
                #     sport = int(content[2])
                month_last_day = int(content[0])
            # day = int(content[0])

            study = content[1].split("_")
            maths = int(study[0])
            computer_science = int(study[1])
            english = int(study[2])
            total = maths + computer_science + english
            study_time_per_day.append(total)

        # total_study_time = (maths + computer_science + english) // 60
        mean = sum(study_time_per_day) // month_last_day
        std = math.sqrt(
            (sum([(day_total - mean)**2 for day_total in study_time_per_day]))/(month_last_day))
        print(std)
        return study_time_per_day, mean, std, month_last_day, month


def plot_data(data):
    print(data)
    total_time, mean, std, month_last_day, month = data
    min_count = 0
    inside_1std = 0
    for day_total in total_time:
        if day_total >= (mean-std) and day_total <= (mean+std):
            inside_1std += 1
        # print(day_total)
        min_count += day_total
    print(min_count, min_count//60)
    print(inside_1std, inside_1std/month_last_day)

    fig, (ax1, ax2) = plt.subplots(ncols=2)
    fig.suptitle(month)
    ax1.bar([x for x in range(1, month_last_day+1)], total_time)


    ax2.plot(total_time, color="purple")
    ax2.axhline(y=mean-std, color='k', linestyle='-')
    ax2.axhline(y=mean, color='r', linestyle='-', label="mean")
    ax2.axhline(y=mean+std, color='k', linestyle='-', label="mean+-std")
    ax2.legend()

    plt.show()


if __name__ == '__main__':
    # data_to_plot_PATH = "C:/Users/San/Documents/inf/time monitoring/Mar 2022 study data.txt"
    data_to_plot_PATH = "C:/Users/San/Documents/inf/time monitoring/studying time.txt"
    # print(calculate(data_to_plot_PATH))
    print(plot_data(calculate(data_to_plot_PATH)))
