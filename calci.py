import tkinter as tk

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")

        self.result_var = tk.StringVar()
        self.result_var.set("")

        self.entry = tk.Entry(root, textvariable=self.result_var, font=('Arial', 18), bd=10, insertwidth=4, width=20, justify='right')
        self.entry.grid(row=0, column=0, columnspan=4)

        self.create_buttons()

    def create_buttons(self):
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3)
        ]

        for (text, row, column) in buttons:
            button = tk.Button(self.root, text=text, padx=40, pady=20, font=('Arial', 14), command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=column)

    def on_button_click(self, value):
        if value == '=':
            try:
                result = eval(self.result_var.get())
                self.result_var.set(result)
            except Exception as e:
                self.result_var.set("Error")
        elif value == 'C':
            self.result_var.set("")
        else:
            self.result_var.set(self.result_var.get() + value)

def main():
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
