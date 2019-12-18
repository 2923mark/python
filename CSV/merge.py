#!/usr/bin/python
import pandas as pd

a = pd.read_csv("owners.csv")
b = pd.read_csv("compute.csv")

merged = a.merge(b, on='server')
merged.to_csv("output.csv", index=False)