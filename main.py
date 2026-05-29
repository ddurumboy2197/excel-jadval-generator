import pandas as pd

# Excel jadval hosil qilish uchun ma'lumotlar
data = {
    'Ism': ['Ali', 'Vali', 'Hasan', 'Husan'],
    'Yosh': [20, 25, 30, 35],
    'Kocha': ['A', 'B', 'C', 'D']
}

# Pandas kutubxonasidan foydalanib Excel jadval hosil qilamiz
df = pd.DataFrame(data)

# Excel faylga jadvalni saqlash
df.to_excel('jadvallar.xlsx', index=False)
```

```python
import pandas as pd

# Excel jadvaldan ma'lumotlar olish
df = pd.read_excel('jadvallar.xlsx')

# Excel jadvaldan ma'lumotlarni konsolga chiqarish
print(df)
```

```python
import pandas as pd

# Excel jadvaldan ma'lumotlar olish
df = pd.read_excel('jadvallar.xlsx')

# Excel jadvaldan ma'lumotlarni Excel fayliga qaytarish
df.to_excel('jadvallar.xlsx', index=False)
