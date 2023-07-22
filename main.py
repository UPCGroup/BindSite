import pandas as pd
import os

def convert(fileName):
    df = pd.read_csv(fileName, sep="|")
    target = pd.DataFrame(columns=["SequenceID", "Site", "Label"])
    for _,item in df.iterrows():
        count = 0
        for index, curr_char in enumerate(item["Label"]):
            if curr_char == '#':
                # 注意 DeepPhos 的字符索引从 1 开始
                # 因此在字符串中索引为 0 的 S T 或者 Y，其位点应当为 1
                target.loc[len(target)] = [item["SequenceID"], index + count, item["Label"].replace('#', '')]
                count -= 1

    if os.path.exists("./output/" + fileName) and os.path.isfile("./output/" + fileName):
        os.remove("./output/" + fileName)
    print(target)
    target.to_csv("./output/" + fileName, header=None, index=None)

# convert(csv 文件的位置)
# 生成符合 test data.csv 格式的 CSV 文件