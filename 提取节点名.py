import re
import json
import pandas as pd

# 示例字符串，包含多个 JSON 对象
data = '''

    '''
# 提取所有匹配的 JSON 对象中的 "name" 字段值
names = []

# 逐行处理数据
lines = data.splitlines()
for line in lines:
    # 查找行中 JSON 对象的部分
    match = re.search(r'{.*}', line)
    if match:
        json_str = match.group()
        try:
            json_obj = json.loads(json_str)
            name_value = json_obj.get("name", "")
            if name_value:
                names.append(name_value)
        except json.JSONDecodeError:
            continue

# 将数据转为 DataFrame
df = pd.DataFrame(names, columns=['Name'])

# 保存到 Excel 文件
df.to_excel('names.xlsx', index=False)

print("数据已保存到 names.xlsx")