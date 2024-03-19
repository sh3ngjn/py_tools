import plotly.graph_objects as go

# 桑基图数据
data = dict(
    # 定义节点，即图中的各个框
    node=dict(
        pad=20,
        thickness=30,
        line=dict(color="red", width=0.5),
        label=["薪金", "投资", "租金", "水电", "汽车", "食品", "储蓄"],  # 节点名称
    ),
    # 定义链接，即节点之间的流
    link=dict(
        source=[0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2],  # 源节点的索引
        target=[3, 4, 5, 6, 3, 4, 5, 6, 3, 4, 5, 6],  # 目标节点的索引
        value=[750, 150, 500, 100, 500, 200, 500, 100, 100, 50, 250, 500]  # 流的值
    )
)

# 创建图形对象并添加桑基图数据
fig = go.Figure(go.Sankey(
    arrangement = "snap",
    node = data['node'],
    link = data['link']
))

# 设置图表标题
fig.update_layout(title_text="资金流转", font_size=10)

# 显示图表
fig.show()
