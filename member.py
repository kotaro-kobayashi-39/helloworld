ver = "0.2"

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

<<<<<<< HEAD
### 以下に自分を追加する ###
newmember = Member("吉田 瑠希也", "よろしくお願いします！")
=======

### 以下に自分を追加する ###
newmember = Member("大河原翔太", "よろしくお願いいたします。")
>>>>>>> 9ae056577c236d5a048cd4b1be0a7715ed9d2063
mlist.append(newmember)


# メンバー表示
print("各メンバーから一言")
print()
for member in mlist:
    print(member.name + " ..... " + member.words)
