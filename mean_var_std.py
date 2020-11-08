import numpy as np


def calculate(num_list):
    if len(num_list) < 9:
        raise ValueError("List must contain nine numbers.")

    modes = {"mean": "mean",
             "var": "variance",
             "std": "standard deviation",
             "max": "max",
             "min": "min",
             "sum": "sum"}

    data = {}

    array = np.asarray(num_list)
    array.shape = (3, 3)

    for mode in modes.keys():
        data[modes[mode]] = \
            eval(f"[list(array.{mode}(axis=0)), list(array.{mode}(axis=1)), array.flatten().{mode}()]")

    return data
