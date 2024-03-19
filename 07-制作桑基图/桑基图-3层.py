import plotly.graph_objects as go

# 节点标签
nodes = [
    '收入A', '收入B',  # 收入节点
    '部门',  # 部门节点
    '部门1薪资', '部门1材料',  # 部门1支出节点
    '部门2薪资', '部门2材料',  # 部门2支出节点
    '部门3薪资', '部门3材料'   # 部门3支出节点
]

# 链接，指明流向和大小
links = {
    'source': [0, 1, 2, 2, 2, 2, 2, 2],  # 从收入到部门，再到支出
    'target': [2, 2, 3, 4, 5, 6, 7, 8],  # 目标节点的索引
    'value':  [500, 300, 200, 200, 150, 150, 100, 100]  # 流的大小
}

# 创建桑基图
fig = go.Figure(data=[go.Sankey(
    node=dict(
      pad=15,
      thickness=20,
      line=dict(color='black', width=0.5),
      label=nodes
    ),
    link=links
)])

# 添加标题
fig.update_layout(title_text="三层桑基图示例", font_size=10)

# 显示桑基图
fig.show()
