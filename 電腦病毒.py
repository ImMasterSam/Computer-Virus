import tkinter.messagebox as msg

text1 = """這是個很嚴重的電腦病毒!!!

雖然我沒辦法對你做甚麼
但你必須自行把電腦裡的資料全部刪除!             
(╯°□°）╯︵ ┻━┻

否則你下次段考全都會不及格!
出門都會踩到狗大便!💩
"""

text2 = """你還沒有把資料刪除!!!
快給我去刪掉!!!
"""

text3 = """在你還沒有刪除資料前
別想把這個病毒關掉!!!
"""

response = msg.askokcancel("我警告你喔!", text1)

while(1):
    if(response == 1):
        msg.showwarning("想騙我啊!", text2)
        response = msg.askokcancel("我警告你喔!", text1)
    else:
        msg.showerror("取消個屁!", text3)
        response = msg.askokcancel("我警告你喔!", text1)