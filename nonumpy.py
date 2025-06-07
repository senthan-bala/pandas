
from datetime import datetime
import numpy as np

# Get the current date and time

# length = [x*2 for x in range(20000000)]
# width = [x for x in range(20000000)]

rng = np.random.default_rng()

length = rng.integers(low=1, high=9, size=20000000)
width = [x for x in range(20000000)]


areas = []

# using numpy

def no_numpy(l, w, a):
    item_count = len(l)

    for i in range(0, item_count):
        area = (l[i] * w[i]) + 103
        a.append(area)

    # print(a)


def yes_numpy(l, w, a):
    nl = np.array(l)
    nw = np.array(w)
    na = nl * nw

    np.save('areas.npy', na)
    print(na[3])


def load_numpy():
    na = np.load('areas.npy')
    print(na[3])


now = datetime.now()
print("Starting processing:", now)

# no_numpy(length, width, areas)
# yes_numpy(length, width, areas)
load_numpy()

now2 = datetime.now()
print("Completed processing:", now2)
