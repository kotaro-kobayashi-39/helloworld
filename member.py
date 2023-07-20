
ver = "0.9"


class Member:
    def __init__(self, name, words=""):
        self.name = name
        self.words = words
    
    def name(self):
        return self.name

print("メンバーリスト・アプリ  Ver. "+ver)
print("--------------------------------")

# メンバー追加
mlist = []
newmember = Member("江頭2:50", "エガちゃんです！")
mlist.append(newmember)


### 以下に自分を追加する ###
newmember = Member("大橋諒太郎", "よろしくです！")
mlist.append(newmember)


### 以下に自分を追加する ###
newmember = Member("笹谷拓斗", "よろしく")
mlist.append(newmember)

newmember = Member("蜂屋 孝太郎", "アタオカです！")
mlist.append(newmember)

### 以下に自分を追加する ###
newmember = Member("房州優樹", "よろしくです！")
mlist.append(newmember)


### 以下に自分を追加する ###
newmember = Member("吉田 羅生", "よろしくです！")


### 以下に自分を追加する ###
newmember = Member("渡邉　雄太", "よろしく！")
mlist.append(newmember)

### 以下に自分を追加する ###
newmember = Member("岸野航", "よろしくです！")
mlist.append(newmember)


newmember = Member("岩崎泰斗", "おなかへりました")
mlist.append(newmember)

# メンバー表示
print("各メンバーから一言")
print()
for member in mlist:
    print(member.name + " ..... " + member.words)
