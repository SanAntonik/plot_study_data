import matplotlib.pyplot as plt
import math


def calculate(PATH):
    with open(PATH, "r") as f:
        data = f.read()
        lines = data.splitlines()
        month = lines[0]

        study_time_per_day = []
        for line in lines[1::]:
            content = line.split(":")
            if lines[-1] == line:
                month_last_day = int(content[0])

            study = content[1].split("_")
            maths = int(study[0])
            computer_science = int(study[1])
            english = int(study[2])
            total = maths + computer_science + english
            study_time_per_day.append(total)

        mean = sum(study_time_per_day) // month_last_day
        std = math.sqrt(
            (sum([(day_total - mean)**2 for day_total in study_time_per_day]))/(month_last_day))
        return study_time_per_day, mean, std, month_last_day, month


# plot mean, mean+-standart deviation
def mean_std(ax, mean, std):
    ax.axhline(y=mean-std, color='k', linestyle='-')
    ax.axhline(y=mean, color='r', linestyle='-', label="mean")
    ax.axhline(y=mean+std, color='k', linestyle='-', label="mean+-std")


def plot_data(data):
    total_time, mean, std, month_last_day, month = data

    fig, (ax1, ax2) = plt.subplots(ncols=2)
    fig.suptitle(month)
    ax1.bar([x for x in range(1, month_last_day+1)], total_time, color="purple")
    mean_std(ax1, mean, std)

    ax2.plot(total_time, color="purple")
    mean_std(ax2, mean, std)
    ax2.legend()

    plt.show()


if __name__ == '__main__':
    # data_to_plot_PATH = "C:/Users/San/Documents/inf/time monitoring/Mar 2022 study data.txt"
    data_to_plot_PATH = "C:/Users/San/Documents/inf/time monitoring/studying time.txt"
    plot_data(calculate(data_to_plot_PATH))
