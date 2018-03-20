import matplotlib.pyplot as plt
import numpy as np

# creates a graphic with one type of bins
def plot(index, percentages, ticklabels, outfile):
    fig, ax = plt.subplots()
    bar_width = 0.5
    opacity = 0.4
    bars = ax.bar(index, percentages, bar_width, alpha=opacity)
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2.0, 0.99 * height, '%d' % int(height) + "%", ha='center', va='bottom')
    ax.set_ylabel("Percentage")
    ax.set_xlabel("Rating")
    ax.set_title("Difficulty Rating")
    ax.set_xticks(index)
    ax.set_xticklabels(ticklabels)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    fig.tight_layout()
    fig.savefig(outfile)
    plt.show()

# creates a graphic with two types of bins
def plot_bool(outfile):
    fig, ax = plt.subplots()
    bar_width = 0.4
    opacity = 0.4
    index = np.arange(4)
    yes_values = (30, 35, 60, 75)
    no_values = (70, 65, 40, 25)
    yes_bars = ax.bar(index, yes_values, bar_width, label='Right', color='g', alpha=opacity)
    for yes_bar in yes_bars:
        height = yes_bar.get_height()
        ax.text(yes_bar.get_x() + yes_bar.get_width() / 2.0, 0.99 * height, '%d' % int(height) + "%", ha='center',
                va='bottom')
    no_bars = ax.bar(index + bar_width, no_values, bar_width, label='Wrong', color='r', alpha=opacity)
    for no_bar in no_bars:
        height = no_bar.get_height()
        ax.text(no_bar.get_x() + no_bar.get_width() / 2.0, 0.99 * height, '%d' % int(height) + "%", ha='center',
                va='bottom')
    ax.set_ylabel("Percentage")
    ax.set_xlabel("Questions")
    ax.set_title("Language Test")
    ax.set_xticks(index + bar_width / 2)
    ax.set_xticklabels(('Q1', 'Q2', 'Q3', 'Q4'))
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.legend()
    fig.tight_layout()
    fig.savefig(outfile)
    plt.show()

# creates a graphic with three (or more) types of bins
def plot_multiple(outfile):
    fig, ax = plt.subplots()
    bar_width = 0.3
    opacity_sim = 0.3
    opacity_diff = 0.7
    opacity_inter = 0.5
    index = np.arange(3)
    sim_values = (100, 33.3, 60)
    inter_values = (0, 33.3, 20)
    diff_values = (0, 33.3, 20)
    sim_bars = ax.bar(index, sim_values, bar_width, label='Similar', color='b', alpha=opacity_sim)
    for sim_bar in sim_bars:
        height = sim_bar.get_height()
        ax.text(sim_bar.get_x() + sim_bar.get_width() / 2.0, 0.99 * height, '%d' % int(height) + "%", ha='center',
                va='bottom')
    inter_bars = ax.bar(index + bar_width, inter_values, bar_width, label='Intermediate', color='b',
                        alpha=opacity_inter)
    for inter_bar in inter_bars:
        height = inter_bar.get_height()
        ax.text(inter_bar.get_x() + inter_bar.get_width() / 2.0, 0.99 * height, '%d' % int(height) + "%", ha='center',
                va='bottom')
    diff_bars = ax.bar(index + bar_width*2, diff_values, bar_width, label='Different', color='b', alpha=opacity_diff)
    for diff_bar in diff_bars:
        height = diff_bar.get_height()
        ax.text(diff_bar.get_x() + diff_bar.get_width() / 2.0, 0.99 * height, '%d' % int(height) + "%", ha='center',
                va='bottom')
    ax.set_ylabel("Percentage")
    ax.set_xlabel("Category")
    ax.set_title("Identification of Category")
    ax.set_xticks(index + bar_width)
    ax.set_xticklabels(('Similar', 'Intermediate', 'Different'))
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.legend()
    fig.tight_layout()
    fig.savefig(outfile)
    plt.show()


if __name__ == '__main__':
    print("")
    # plot_bool("C:\\Users\\Jakob\\Documents\\LanguageTest.svg")
    # plot(np.arange(5), (22, 0, 56, 22, 0), ('Very Easy', '', '', '','Very Hard'), "C:\\Users\\Jakob\\Documents\\Difficulty.pdf")
    plot_multiple("C:\\Users\\Jakob\\Documents\\Category.png")
