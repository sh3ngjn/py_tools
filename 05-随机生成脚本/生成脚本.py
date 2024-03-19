import pandas as pd

# 读取excel文件
file = pd.read_excel('~/Desktop/2-实操/09-微信公众号/情感文章素材库.xlsx', engine='openpyxl')

zhurengong = file['主人公']
dream = file['梦想和目标']
action = file['为目标所采取的行动']
faile = file['意外库']
fz = file['惊喜或反转库']
end = file['结局库']
i = 0
while i < 11:
    a = zhurengong.sample(n=None, frac=None, replace=False, weights=None, axis=0).item()
    # print(a)
    b = dream.sample(n=None, frac=None, replace=False, weights=None, axis=0).item()
    c = action.sample(n=None, frac=None, replace=False, weights=None, axis=0).item()
    d = faile.sample(n=None, frac=None, replace=False, weights=None, axis=0).item()
    e = fz.sample(n=None, frac=None, replace=False, weights=None, axis=0).item()
    f = end.sample(n=None, frac=None, replace=False, weights=None, axis=0).item()
    outline = a + '，' + b + '，' + c + '，' + d + '，' + e + '，' + f
    print('---------------------------------------------')
    print(outline)
    print('---------------------------------------------')
    i += 1
