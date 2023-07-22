import pandas as pd
import os

def convert(fileName):
    df = pd.read_csv(fileName, sep="|")
    target = pd.DataFrame(columns=["SequenceID", "Site", "Label"])
    for _,item in df.iterrows():
        for index, curr_char in enumerate(item["Label"]):
            if curr_char == '#':
                target.loc[len(target)] = [item["SequenceID"], index, item["Label"].replace('#', '')]

    if os.path.exists("./output/" + fileName) and os.path.isfile("./output/" + fileName):
        os.remove("./output/" + fileName)
    print(target)
    target.to_csv("./output/" + fileName, header=None, index=None)

convert("testing_proteins_withannotation_STY.csv")
#convert("training_proteins_nonredundant_STY.csv")