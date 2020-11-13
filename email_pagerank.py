


# 数据加载
emails = pd.read_csv("./data/Emails.csv")

#读取别名文件
file = pd.read_csv("./data/Aliases.csv")
aliases = {}
for index, row in file.iterrows():
    aliases[row['Alias']] = row['PersonId']

#读取人名文件
file = pd.read_csv("./data/Persons.csv")
persons = {}
for index,row in file.iterrows():
    persons[row['Id']] = row['name']

