import boi

abc = boi.gdp.get_gdp(date_start='2022-01-01')
print(abc)

abc = boi.infl.get_cpi()
print(abc)

abc = boi.kr.get_ir()
print(abc)

abc = boi.infl.get_inflation()
print(abc)
