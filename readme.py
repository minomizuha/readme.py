import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from datetime import datetime

def generate_readme():
    version = version_var.get()
    license_type = license_var.get()
    platform = platform_var.get()
    redistribution = redistrib_var.get()
    reproduction = reproduction_var.get()
    
    # 現在の日付取得
    current_date = datetime.now().strftime("%Y-%m-%d")
    
    content = f"""README
============

【 作者名 】　{author_var.get()}
【 ソフト名 】　{software_name_var.get()}
【 バージョン 】　Ver{version}
【 作成日 】　{current_date}
【 種別 】　{license_type}
【 開発言語 】　{language_var.get()}
【 対応機種 】　{platform}
【 著作権者 】　{copyright_var.get()}
【 再配布 】　{redistribution}
【 転載 】　{reproduction}
【 ホームページ 】　{homepage_var.get()}
【 連絡先 】　{contact_var.get()}
============

【 はじめに 】
{intro_text.get('1.0', 'end')}
【 ﾌｧｲﾙ構成 】
{file_structure_text.get('1.0', 'end')}
【 ｲﾝｽﾄｰﾙ 】
{install_text.get('1.0', 'end')}
【 ｱﾝｲﾝｽﾄｰﾙ 】
{uninstall_text.get('1.0', 'end')}
【 使い方 】
{usage_text.get('1.0', 'end')}
【 著作権 】
{copyright_section_text.get('1.0', 'end')}
【 免責 】
{disclaimer_text.get('1.0', 'end')}
【 謝辞 】
{acknowledgments_text.get('1.0', 'end')}
【 開発履歴 】
{history_text.get('1.0', 'end')}
============
"""
    
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
        messagebox.showinfo("保存完了", "READMEが保存されました！")

# GUI構築
root = tk.Tk()
root.title("README生成ソフト")

root.iconbitmap('icon.ico')

# 3つのフレームを作成
frame1 = ttk.Frame(root, padding=10)
frame1.grid(row=0, column=0, sticky="NS")

frame2 = ttk.Frame(root, padding=10)
frame2.grid(row=0, column=1, sticky="NS")

frame3 = ttk.Frame(root, padding=10)
frame3.grid(row=0, column=2, sticky="NS")

# 基本情報入力用フィールド (左列)
author_var = tk.StringVar()
software_name_var = tk.StringVar()
version_var = tk.StringVar()
license_var = tk.StringVar(value="フリーウェア")
language_var = tk.StringVar()
platform_var = tk.StringVar(value="Windows")
copyright_var = tk.StringVar()
redistrib_var = tk.StringVar(value="不可")
reproduction_var = tk.StringVar(value="不可")
homepage_var = tk.StringVar()
contact_var = tk.StringVar()

fields = [
    ("作者名", author_var),
    ("ソフト名", software_name_var),
    ("バージョン", version_var),
    ("種別", license_var),
    ("開発言語", language_var),
    ("対応機種", platform_var),
    ("著作権者", copyright_var),
    ("再配布", redistrib_var),
    ("転載", reproduction_var),
    ("ホームページ", homepage_var),
    ("連絡先", contact_var),
]

for i, (label, var) in enumerate(fields):
    ttk.Label(frame1, text=label).grid(row=i, column=0, sticky=tk.W, padx=5, pady=5)
    ttk.Entry(frame1, textvariable=var).grid(row=i, column=1, sticky=tk.EW, padx=5, pady=5)

# テキストエリア (中列)
middle_fields = [
    ("はじめに", "intro_text"),
    ("ﾌｧｲﾙ構成", "file_structure_text"),
    ("ｲﾝｽﾄｰﾙ", "install_text"),
    ("ｱﾝｲﾝｽﾄｰﾙ", "uninstall_text"),
    ("使い方", "usage_text"),
]

middle_texts = {}

for label, name in middle_fields:
    ttk.Label(frame2, text=label).pack(anchor=tk.W)
    text_widget = tk.Text(frame2, wrap=tk.WORD, height=5)
    text_widget.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
    middle_texts[name] = text_widget

# テキストエリア (右列)
right_fields = [
    ("著作権", "copyright_section_text"),
    ("免責", "disclaimer_text"),
    ("謝辞", "acknowledgments_text"),
    ("開発履歴", "history_text"),
]

right_texts = {}

for label, name in right_fields:
    ttk.Label(frame3, text=label).pack(anchor=tk.W)
    text_widget = tk.Text(frame3, wrap=tk.WORD, height=5)
    text_widget.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
    right_texts[name] = text_widget

# 変数を登録
intro_text = middle_texts["intro_text"]
file_structure_text = middle_texts["file_structure_text"]
install_text = middle_texts["install_text"]
uninstall_text = middle_texts["uninstall_text"]
usage_text = middle_texts["usage_text"]

copyright_section_text = right_texts["copyright_section_text"]
disclaimer_text = right_texts["disclaimer_text"]
acknowledgments_text = right_texts["acknowledgments_text"]
history_text = right_texts["history_text"]

# ボタン
ttk.Button(root, text="README生成", command=generate_readme).grid(row=1, column=0, columnspan=3, pady=10)

root.mainloop()
