import numpy as np
import pandas as pd

# 두 개의 시리즈 데이터가 있습니다.
print("Population series data:")
population_dict = {
    'korea': 5180,
    'japan': 12718,
    'china': 141500,
    'usa': 32676
}
population = pd.Series(population_dict)
print(population, "\n")

print("GDP series data:")
gdp_dict = {
    'korea': 169320000,
    'japan': 516700000,
    'china': 1409250000,
    'usa': 2041280000,
}
gdp = pd.Series(gdp_dict)
print(gdp, "\n")


# 이곳에서 2개의 시리즈 값이 들어간 데이터프레임을 생성합니다.
print("Country DataFrame")
frame = {'population': population_dict, 'gdp': gdp_dict}
country = pd.DataFrame(frame)
print(country)

# 데이터 프레임에 gdp per capita 칼럼을 추가하고 출력합니다.
country['gdp per captia'] = country['gdp']/country['population']
print(country)

# 데이터 프레임을 만들었다면, index와 column도 각각 확인해보세요.
print(country.index)
print(country.columns)
