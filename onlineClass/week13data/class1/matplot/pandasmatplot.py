# from elice_utils import EliceUtils
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# elice_utils = EliceUtils()

df = pd.read_csv("./data/pokemon.csv")

fire = df[
    (df['Type 1'] == 'Fire') | ((df['Type 2']) == "Fire")
]

water = df[
    (df['Type 1'] == 'Water') | ((df['Type 2']) == "Water")
]

fig, ax = plt.subplots()
ax.scatter(fire['Attack'], fire['Defense'],
           color='R', label='Fire', marker="*", s=50)
ax.scatter(water['Attack'], water['Defense'],
           color='B', label="Water", s=25)
ax.set_xlabel("Attack")
ax.set_ylabel("Defense")
ax.legend(loc="upper right")

fig.savefig("plot.png")
# elice_utils.send_image("plot.png")
