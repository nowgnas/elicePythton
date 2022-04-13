from math import fabs
import pandas as pd


# ./data/tree_data.csv 파일을 읽어서 작업해보세요!
file = '/Volumes/nowgnas/#elicepy/onlineClass/week13data/class1/series/data/tree_data.csv'
csv_file = pd.read_csv(file, delimiter=',')

sortCsv = csv_file.sort_values('height', ascending=False)

print(sortCsv.iloc[0])
