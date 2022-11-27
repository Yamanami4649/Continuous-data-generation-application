import tkinter
import re

# Converts input characters
def chenge_text(importText,NumberDol,NumberAlpha,EnglishDol,EnglishAlpha,executionsNumber):
    output_text.delete( 0., tkinter.END ) # 出力画面をクリアします
    return_text = '' # 出力する文字の変数をリセット
    for i in range(executionsNumber): # 指定回数分繰り返します
        chenge_text = importText
        if NumberDol: # $+数値の変換
            pattern_plus = re.findall(r'\$.*?(\d+)', importText) #プラスの場合 一致するものを配列に
            pattern_minus = re.findall(r'\$-.*?(\d+)', importText) # マイナスの場合 一致するものを配列に
            for j in range(len(pattern_plus)):
                chenge_text = chenge_text.replace('$' + str(pattern_plus[j]),str(int(pattern_plus[j]) + i),1) # 位置した数値に1足したものを入れる
            for j in range(len(pattern_minus)):
                chenge_text = chenge_text.replace('$-' + str(pattern_minus[j]),str(int(pattern_minus[j]) * -1 + i),1)
        if NumberAlpha:  # @+数値の変換 以下上と同じ
            pattern_plus = re.findall(r'@.*?(\d+)', importText)
            pattern_minus = re.findall(r'@-.*?(\d+)', importText)
            for j in range(len(pattern_plus)):
                chenge_text = chenge_text.replace('@' + str(pattern_plus[j]),str(int(pattern_plus[j]) + i),1)
            for j in range(len(pattern_minus)):
                chenge_text = chenge_text.replace('@-' + str(pattern_minus[j]),str(int(pattern_minus[j]) * -1 + i),1)
        if EnglishDol: # $+半角英字の変換
            pattern = re.findall(r'\$([a-z])', importText) #一致するものを配列に
            for j in range(len(pattern)):
                if ((ord(pattern[j]) + i) > 122): # zまで行ったらaに戻るための条件分岐
                    if (i == 0):
                        chenge_text = chenge_text.replace('$' + pattern[j],'z',1) # 初回だけ変更しない
                    else:
                        chenge_text = chenge_text.replace('$' + pattern[j],chr(ord(pattern[j]) + i - 26),1) # zをリセットしてaから始める
                else:
                    chenge_text = chenge_text.replace('$' + pattern[j],chr(ord(pattern[j]) + i),1) #通常変換
        if EnglishAlpha: # @+半角英字の変換 以下上と同じ
            pattern = re.findall(r'@([a-z])', importText)
            for j in range(len(pattern)):
                if ((ord(pattern[j]) + i) > 122):
                    if (i == 0):
                        chenge_text = chenge_text.replace('@' + pattern[j],'z',1)
                    else:
                        chenge_text = chenge_text.replace('@' + pattern[j],chr(ord(pattern[j]) + i - 26),1)
                else:
                    chenge_text = chenge_text.replace('@' + pattern[j],chr(ord(pattern[j]) + i),1)
        return_text = return_text + chenge_text # 出力する文字に追加
    output_text.insert(tkinter.END,return_text) # 出力ボックスに入れる


def main():
    root = tkinter.Tk() # 枠の生成
    root.title('連続データ生成君')
    root.geometry("600x800+10+10")
    root.maxsize(width=600,height=800) # サイズが変更できないように設定
    root.minsize(width=600, height=800)


    top_frame = tkinter.LabelFrame(root, text="ここに連続データを入力")
    top_frame.pack(padx=10,pady=10)
    import_text = tkinter.Text(top_frame, height=20)
    import_text.insert(tkinter.END,'')
    import_text.pack(padx=10,pady=10)

    middle_frame = tkinter.LabelFrame(root, text="変換設定")
    middle_frame.pack(padx=10,pady=1,fill=tkinter.BOTH)
    check_chenge_number_var = tkinter.BooleanVar(middle_frame)
    check_chenge_number = tkinter.Checkbutton(middle_frame, text="$+数値 を加算させる", variable=check_chenge_number_var,cursor='hand2')
    check_chenge_number.select()
    check_chenge_number.grid(row=0,column=0)
    check_chenge_english_var = tkinter.BooleanVar(middle_frame)
    check_chenge_english = tkinter.Checkbutton(middle_frame, text="$+半角英字 を加算させる", variable=check_chenge_english_var,cursor='hand2')
    check_chenge_english.select()
    check_chenge_english.grid(row=0,column=1)
    check_chenge_number_var_alpha = tkinter.BooleanVar(middle_frame)
    check_chenge_number_alpha = tkinter.Checkbutton(middle_frame, text="@+数値 を加算させる", variable=check_chenge_number_var_alpha,cursor='hand2')
    check_chenge_number_alpha.grid(row=0,column=2)
    check_chenge_english_var_alpha = tkinter.BooleanVar(middle_frame)
    check_chenge_english_alpha = tkinter.Checkbutton(middle_frame, text="@+半角英字 を加算させる", variable=check_chenge_english_var_alpha,cursor='hand2')
    check_chenge_english_alpha.grid(row=0,column=3)

    middle_second_frame = tkinter.LabelFrame(root, text="変換回数設定")
    middle_second_frame.pack(padx=10,pady=1,fill=tkinter.BOTH)

    tkinter.Label(middle_second_frame, text='作成個数を入力').grid(row=0, column=0)
    executions_number = tkinter.IntVar(root)
    executions_number.set(2)
    executions_number_spinbox = tkinter.Spinbox(middle_second_frame,textvariable=executions_number,from_=2,to=10000,increment=1)
    executions_number_spinbox.grid(row=0,column=1,ipadx=50)

    chenge_button = tkinter.Button(root, text="変換",
        command=lambda:chenge_text(import_text.get("1.0","end"),
                                    check_chenge_number_var.get(),
                                    check_chenge_number_var_alpha.get(),
                                    check_chenge_english_var.get(),
                                    check_chenge_english_var_alpha.get(),
                                    executions_number.get()
                                    ),
        height=1, pady=5, bg="#c0c0c0", cursor='hand2')
    chenge_button.pack(padx=5,pady=1,fill=tkinter.BOTH)

    result_frame = tkinter.LabelFrame(root, text="変換結果")
    result_frame.pack(padx=10,pady=10)
    global output_text
    output_text = tkinter.Text(result_frame, height=40)
    output_text.insert(tkinter.END,'')
    output_text.pack(padx=10,pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
