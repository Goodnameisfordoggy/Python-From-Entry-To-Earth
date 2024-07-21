import tkinter as tk

root = tk.Tk()
root.geometry("200x100")

# 创建凸起按钮
raised_btn = tk.Button(root, text="Raised", relief=tk.RAISED)
raised_btn.pack(pady=10)

# 创建凹陷按钮
sunken_btn = tk.Button(root, text="Sunken", relief=tk.SUNKEN)
sunken_btn.pack(pady=10)

# 创建平面按钮
flat_btn = tk.Button(root, text="Flat", relief=tk.FLAT)
flat_btn.pack(pady=10)

root.mainloop()