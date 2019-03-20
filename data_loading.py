import pandas as pd
import numpy as np

"""Cite75_99.zip contains the pairwise citations data.
Pat63_99.zip contains the patent data, including the constructed
variables
Coname.zip contains the assignee names.
Match.zip contains the match to CUSIP numbers
Inventor.zip contains the individual inventor records
"""
cite75_99 = pd.read_csv("../data/cite75_99.txt")
pat63_99 = pd.read_csv("../data/apat63_99.txt")
coname = pd.read_csv("../data/aconame.txt")
inventor = pd.read_csv("../data/ainventor.txt")
#
subcategories = pd.read_csv("../data/subcategories.csv")
match = pd.read_csv("../data/match.csv")
