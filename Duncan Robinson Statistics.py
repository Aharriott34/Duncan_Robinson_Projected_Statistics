import numpy as np
from scipy.stats import binom_test
from scipy.stats import norm
import random
import seaborn as sns
from matplotlib import pyplot as plt
from collections.abc import Iterable

# Statistics from NBA.com and basketball-reference
sns.color_palette("crest", as_cmap=True)
sns.set_palette("Spectral")
sns.set_style("darkgrid")
# Forecast Duncan Robinson's three point percentage and points per game for the next 5 season.
points_per_season = [50, 983, 952]
ppg_per_season = [3.33, 13.47, 14.41]
three_point_percentage_seasons = [30.3, 44.6, 41.3]
three_point_shots_made = [10, 270, 253]
three_point_attempts_per_season = [33, 606, 612]
career_3_pt_avg = 42.6

forecast_3_made = sum(three_point_shots_made) / len(three_point_shots_made)
forecast_3_attempt = sum(three_point_attempts_per_season) / len(three_point_attempts_per_season)

# Binomial sample n= three point shots made , p= career percentage, size= total threes attempted
forecast_average_model = np.random.binomial(n=forecast_3_attempt, p=0.426, size=int(forecast_3_made))
forecast_model = np.random.binomial(n=612, p=0.429, size=264)
binom_test_1 = binom_test(int(forecast_3_made), n=forecast_3_attempt, p=0.426)
binom_test_2 = binom_test(264, n=612, p=0.429)

seasons_label = ("Season 1", "Season 2", "Season 3", "Season 4", "Season 5", "Season 6", "Season 7", "Season 8")
actual_shots_made = [10, 270, 253, 0, 0, 0, 0, 0]
forecasted_shots_made = [random.randint(230,290) for i in range(8)]

_, bins, _ = plt.hist(forecast_model, density=True)
mu, sigma = norm.fit(forecast_model)
best_fit = norm.pdf(bins, mu, sigma)

plt.plot(bins, best_fit, color='black')
plt.title("Duncan Robinson: Distribution of Shots Made per Season")
plt.xlabel("Shots Made")
plt.ylabel("Density")
plt.show()

# Projected
n = 1  # This is our first dataset (out of 2)
t = 2 # Number of dataset
d = range(len(seasons_label)) # Number of sets of bars
w = 0.5 # Width of each bar
bars1_x = [t*element + w*n for element
             in range(len(d))]

# Actual
n = 2 # This is our first dataset (out of 2)
t = 2 # Number of dataset
d = range(len(seasons_label)) # Number of sets of bars
w = 0.5 # Width of each bar
bars2_x = [t*element + w*n for element
             in range(len(d))]

middle_x = [(a + b) / 2.0 for a, b in zip(bars1_x, bars2_x)]
labels = ["Projected Shots Made", "Actual Shots Made"]

plt.clf()
plt.bar(bars1_x, forecasted_shots_made)
plt.bar(bars2_x, actual_shots_made)
plt.xticks(middle_x, seasons_label)
plt.xlabel("Seasons")
plt.ylabel("Shots Made")
plt.title("Duncan Robinson: Projected Three Pointers Made Per Season")
plt.legend(labels)
plt.show()

# Season 3 was a lockout and season 8 was injury plagued season.
ray_allen_first_8 = [117, 134, 74, 172, 202, 229, 201, 78]
ray_allen_career = 2973
# Injured in season 3
stephen_curry_first_8 = [166, 151, 55, 272, 261, 286, 402, 324]
stephen_curry_career = 2832
# No injuries
reggie_miller_first_8 = [61, 98, 150, 112, 129, 167, 123, 195]
reggie_miller_career = 2560
# Did not play for the first 23 games in season 7
kyle_korver_first_8 = [81, 226, 184, 132, 111, 103, 59, 120]
kyle_korver_career = 2450
# No injuries
james_harden_first_8 = [93, 113, 114, 179, 177, 208, 236, 262]
james_harden_career = 2445

all_8_combined = [sum(ray_allen_first_8), sum(stephen_curry_first_8), sum(reggie_miller_first_8), sum(kyle_korver_first_8), sum(james_harden_first_8)]
three_point_shots_made.append([random.randint(230, 290) for i in range(5)])

top_5_per_season = [ray_allen_first_8, stephen_curry_first_8, reggie_miller_first_8, kyle_korver_first_8, james_harden_first_8]
top_5_career_made = [ray_allen_career, stephen_curry_career, reggie_miller_career, kyle_korver_career, james_harden_career]

def flatten(lis):
    for item in lis:
        if isinstance(item, Iterable) and not isinstance(item, str):
            for x in flatten(item):
                yield x
        else:
            yield item

duncan_robinson_first_8 = list(flatten(three_point_shots_made))

players_vs_duncan_label = ["R. Allen* vs D.Robinson", "S. Curry vs D.Robinson", "R. Miller* vs D.Robinson", "K. Korver* vs D.Robinson", "J. Harden vs D. Robinson"]
player_label = ["Ray Allen*", "Stephen Curry", "Reggie Miller*", "Kyle Korver*", "James Harden"]

# Current or Former NBA Player
n = 1  # This is our first dataset (out of 2)
t = 2 # Number of dataset
d = range(len(all_8_combined)) # Number of sets of bars
w = 0.5 # Width of each bar
bars3_x = [t*element + w*n for element
             in range(len(d))]

# Duncan
n = 2 # This is our first dataset (out of 2)
t = 2 # Number of dataset
d = range(len(all_8_combined)) # Number of sets of bars
w = 0.5 # Width of each bar
bars4_x = [t*element + w*n for element
             in range(len(d))]

middle_x_2 = [(a + b) / 2.0 for a, b in zip(bars3_x, bars4_x)]
star_labels = ["Player", "Duncan Robinson"]

plt.bar(bars3_x, all_8_combined)
plt.bar(bars4_x, sum(duncan_robinson_first_8))
plt.xticks(middle_x_2, players_vs_duncan_label)
plt.legend(star_labels)
plt.title("Can Duncan Robinson Surpass The Top Five NBA Three Point Shooters In His First Eight Seasons?")
plt.ylabel("Three Pointers Made")
plt.xlabel("NBA Players")
plt.show()

def show_values_on_bars(axs, h_v="v", space=0.4):
    def _show_on_single_plot(ax):
        if h_v == "v":
            for p in ax.patches:
                _x = p.get_x() + p.get_width() / 2
                _y = p.get_y() + p.get_height()
                value = int(p.get_height())
                ax.text(_x, _y, value, ha="center")
        elif h_v == "h":
            for p in ax.patches:
                _x = p.get_x() + p.get_width() + float(space)
                _y = p.get_y() + p.get_height()
                value = int(p.get_width())
                ax.text(_x, _y, value, ha="left")

    if isinstance(axs, np.ndarray):
        for idx, ax in np.ndenumerate(axs):
            _show_on_single_plot(ax)
    else:
        _show_on_single_plot(axs)

plt.clf()
ax = sns.barplot(x=player_label, y=top_5_career_made)
ax.set_title("Most Three Pointers Made")
ax.set_ylabel("Shots Made")
ax.set_xlabel("NBA Players")
ax.text(3.4, 2850, 'Player Retired = Asterisk(*)', style='italic',  bbox={'facecolor': 'red', 'alpha': 0.5, 'pad': 10})
show_values_on_bars(ax)
plt.tight_layout()
plt.show()


plt.clf()
ax1 = sns.violinplot(data=top_5_per_season, orient='h')
ax1.set_yticks(range(len(player_label)))
ax1.set_yticklabels(player_label)
ax1.set_title("Distribution of the Top Five NBA Three Point Shooters in Eight Seasons")
ax1.set_xlabel("Points")
ax1.set_ylabel("NBA Players")
ax1.text(420, 0, 'Asterisk(*) = Player Retired', style='italic',  bbox={'facecolor': 'red', 'alpha': 0.5, 'pad': 10})
# plt.tight_layout()
plt.show()

plt.clf()
ax2 = sns.boxplot(data=top_5_per_season, orient='v')
ax2.set_xticks(range(len(player_label)))
ax2.set_xticklabels(player_label)
ax2.set_title("Distribution of the Top Five NBA Three Point Shooters in Eight Seasons")
ax2.set_ylabel("Three Point Shots Made")
ax2.text(3.4, 370, 'Asterisk(*) = Player Retired', style='italic',  bbox={'facecolor': 'red', 'alpha': 0.5, 'pad': 10})
plt.show()