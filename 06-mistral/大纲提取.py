from langchain.llms import Ollama
from langchain.prompts import PromptTemplate
import pandas as pd
import re
import openpyxl

# 初始化 Ollama 模型
llm = Ollama(base_url="http://localhost:11434", model="openchat:7b-v3.5-1210")

# 加载 Excel 文件
file = pd.read_excel('~/素材库/02-文章相关/大纲提炼/简说美篇-正文300篇以后.xlsx', engine='openpyxl')

# 定义模板
template = """
%INSTRUCTIONS:
请总结文章，按照如下结构进行总结：
1.故事类型
2.故事人物及背景
3.主人公的梦想或目标
4.实现目标过程中遇到的挫折
5.故事发展中遇到的反转
6.故事结局

%TEXT:
{text}
"""

# 创建 Lang Chain Prompt 模板
prompt_template = PromptTemplate(
    input_variables=["text"],
    template=template,
)

# 迭代 DataFrame 的行
for index, row in file.iterrows():
    # 从当前行提取文本
    confusing_text = row['Text']

    # 使用当前文本格式化模板
    final_prompt = prompt_template.format(text=confusing_text)

    # 从 Ollama 获取输出
    output = llm(final_prompt)
    print(output)

    # 使用正则表达式分割输出为六个部分
    parts = re.split(r'\d+\.', output)
    parts = [part.strip() for part in parts if part.strip()]  # 移除空白部分

    # 确保分割后有六个部分
    if len(parts) != 6:
        # 如果没有六个部分，添加空白字符串占位
        parts.extend([''] * (6 - len(parts)))

    # 打开 Excel 文件
    with pd.ExcelWriter('~/素材库/02-文章相关/大纲提炼/输出结果0106.xlsx', engine='openpyxl', mode='a', if_sheet_exists='overlay') as writer:
        # 将当前行的输出转换为 DataFrame
        output_df = pd.DataFrame([parts], columns=[
            '故事类型', '故事人物及背景', '主人公的梦想或目标', 
            '实现目标过程中遇到的挫折', '故事发展中遇到的反转', '故事结局'
        ])
        # 将 DataFrame 追加到 Excel 文件
        output_df.to_excel(writer, index=False, header=False, startrow=writer.sheets['Sheet1'].max_row)

# 注意：首次运行代码前，确保 '输出结果1.xlsx' 文件存在且至少有一行表头
