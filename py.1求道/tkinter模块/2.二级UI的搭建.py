import tkinter as tk


class App:
    def __init__(self, master):
        self.master = master
        self.master.title("Main Window")
        self.create_widgets()

    def create_widgets(self):
        self.btn_open = tk.Button(self.master, text="Open", command=self.open_window)
        self.btn_open.pack(padx=10, pady=10)

    def open_window(self):
        window = tk.Toplevel(self.master)
        window.title("Sub Window")

        lbl_hello = tk.Label(window, text="Hello, world!")
        lbl_hello.pack(padx=10, pady=10)


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()