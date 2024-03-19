import os
import pandas

# 读取文件路径，创建文件绝对路径列表
def read_excel_files(path):
    # 读取目录中的文件
    filenames = []
    '''遍历文件夹中的所有文件，为下一步获取文件夹中的files
    会返回一个三元组（root，dirs, files)
    root 所指的是当前正在遍历的这个文件夹的本身的地址
    dirs 是一个 list ，内容是该文件夹中所有的目录的名字(不包括子目录)
    files 同样是 list , 内容是该文件夹中所有的文件(不包括子目录)
    '''
    for i in os.walk(path):
        '''
        将files替换为文件的绝对路径
        '''
        for filename in i[-1]:
            full_filename = os.path.join(i[0],filename)
            filenames.append(full_filename)
    return filenames

# 创建新的Excel表格
def read_excel(filename):
    """读入excel，返回dataFrame"""
    df = pd.read_excel(filename, index_col=None, headers = 0)
    return df

# 将列表中的文件添加到新的Excel表格中
def merge_excel(datas,index):
    """合并数据,index为参考去重的列名"""
    return pd.concat(datas,ignore_index=True).drop_duplicates(index)

# 主程序
if __name__ == '__main__':
    print('Program is running...')
    # 待读取文件所在文件夹
    path = r''
    # 存储文件所在文件夹
    target_path = r''
    # 读取文件
    data = []
    for filename in read_excel_files(path):
        data.append(read_excel(filename))
    # 合并文件
    df = merge_excel(data)
    # 保存文件
    df.to_excel(target_path+os.sep+'汇总文件.xlsx',index=False)
    print('Success!')

