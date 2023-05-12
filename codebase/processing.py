import numpy as np
import pandas as pd
pd.options.mode.chained_assignment = None

from collections import defaultdict

import plotly.express as px
import plotly.io as pio

import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.style as style
import seaborn as sns

import os

df = pd.read_csv(open(os.path.expanduser("~/documents/data/attribution.csv")))
df['time'] = pd.to_datetime(df['time'])
df = df.sort_values(['cookie', 'time'],
                    ascending=[False, True])
df['order'] = df.groupby('cookie').cumcount() + 1
df.head()
