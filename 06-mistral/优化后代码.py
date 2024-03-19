from langchain.llms import Ollama
from langchain.prompts import PromptTemplate
import pandas as pd
import openpyxl
import os

file_path = os.path.expanduser('~/素材库/02-文章相关/大纲提炼/简说美篇0106.xlsx')
output_file_path = os.path.expanduser('~/素材库/02-文章相关/大纲提炼/输出结果0106.xlsx')

# ... 余下的代码 ...

# 初始化 Ollama 模型
llm = Ollama(base_url="http://localhost:11434", model="openchat:7b-v3.5-1210")

# 创建 Lang Chain Prompt 模板
template = """
INSTRUCTIONS:
请根据下面TEXT内包含的内容仿写一个故事的大纲，要求：
1. 修改原故事中的人物名称、年龄；
2. 适当修改原故事情节，使故事更加吸引人。
3. 以第一人称书写。
4. 大纲文字简洁明了，不超过200字。
5. 故事大纲格式按照如下要求进行输出：
    1. 引子：人物背景与人物关系；
    2. 冲突：故事开端和冲突；
    3. 转折：发生什么样的转折；
    4. 解决：最后如何解决冲突。
6. 全部以中文进行回复，不要出现英文。
TEXT:"
{text}
"
"""

prompt_template = PromptTemplate(
    input_variables=["text"],
    template=template,
)

# 用于存储输出结果的列表
outputs = []

workbook = None
try:
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active
    for row in sheet.iter_rows(min_row=2):  # 假设第一行是表头
        text = row[0].value  # 假设文本在第一列
        final_prompt = prompt_template.format(text=text)
        output = llm(final_prompt)
        print(output)
        outputs.append(output)
except Exception as e:
    print(f"Error: {e}")
finally:
    if workbook:
        workbook.close()

# 将所有输出写入 Excel 文件
output_df = pd.DataFrame(outputs, columns=['故事大纲'])
output_df.to_excel(output_file_path, engine='openpyxl', index=False)
