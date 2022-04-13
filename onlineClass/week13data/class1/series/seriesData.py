import numpy as np
import pandas as pd

# 예시) 시리즈 데이터를 만드는 방법.
series = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'], name="Title")
print(series, "\n")


# 국가별 인구 수 시리즈 데이터를 딕셔너리를 사용하여 만들어보세요.
coutry = pd.Series([5180, 12718, 141500, 32676], index=[
                   'korea', 'japan', 'china', 'usa'], name='country')
print(coutry)
