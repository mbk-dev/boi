import boi

abc = boi.gdp.get_gdp(date_start='2000-01-01')
print(abc)

abc = boi.infl.get_cpi(date_start='2022-01-01')
print(abc)

abc = boi.kr.get_ir(date_start='2022-01-01')
print(abc)

abc = boi.infl.get_inflation(date_start='2021-01-01')
print(abc * 100)
