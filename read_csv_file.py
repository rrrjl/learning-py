import pandas as pd
import numpy as np
import csv

filename = 'test.csv'
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)
	print(header_row)
