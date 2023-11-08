import tkinter as tk

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        root.title("Calculator")
        self.display = tk.Entry(root, width=20)
        self.display.grid(row=0, column=0, columnspan=4)
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]
        row, col = 1, 0
        for button_text in buttons:
            tk.Button(root, text=button_text, command=lambda text=button_text: self.on_button_click(text)).grid(row=row, column=col)
            col += 1
            if col > 3:
                col = 0
                row += 1
    def on_button_click(self, button_text):
        if button_text == "=":
            try:
                expression = self.display.get()
                result = str(eval(expression))
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, result)
            except Exception:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
        else:
            current_text = self.display.get()
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, current_text + button_text)
if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
