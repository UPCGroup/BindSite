# 注意事项
由 Fasta 转化为 CSV 后，你需要先将 CSV 文件中的第一行，改为如下的表头
```csv
Meta|SequenceID|Name|Label|Index
```
同时你还需要将所有的逗号分隔符替换为|分隔符，使用文本编辑器中的替换功能应当可以完成这些。
<br>这是因为转化出来的 CSV 文件中，Label 标签下的数据包含了形如
```
3BP5L_HUMAN,MAEL...QRSVSL,1
```
的内容。
<br>如果你不执行这些操作，转化出来的数据集将会包含 3BP5L_HUMAN 和 1 这种与序列无关的内容。