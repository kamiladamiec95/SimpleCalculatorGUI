import tkinter
from math_operations import MathOperations


class Window(tkinter.Tk):

    def __init__(self, width, height, name, is_resizable):
        self.width = width
        self.height = height
        self.tk = tkinter.Tk()
        self.name = name
        self.tk.geometry(f"{self.width}x{self.height}")
        if is_resizable == 0:
            self.tk.resizable(False, False)
        elif is_resizable == 1:
            self.tk.resizable(True, True)
        # self.centralize()
        # self.tk = super().__init__()
        # print(type(self.tk))

    def centralize(self):
        center_screen_width = self.tk.winfo_screenwidth() / 2
        center_screen_height = self.tk.winfo_screenheight() / 2
        set_window_center_width = int(center_screen_width - self.width/ 2)
        set_window_center_height = int(center_screen_height - self.height / 2)
        self.tk.geometry(f"{self.width}x{self.height}+{set_window_center_width}+{set_window_center_height}")
        self.tk.title(f"{self.name}")

    def add_buttons(self, rows, columns):
        result = tkinter.Label(self.tk, background="white", relief="sunken")
        result.grid(column=0, row=0, columnspan=3, sticky="WE")
        button_dict = {}
        column = 0
        row = 1
        x = 1
        y = columns + 1
        for _ in range(0, rows):
            for number in range(x, y):
                # row = 2
                button_dict[number] = tkinter.Button(self.tk, text=number)
                button_dict[number].grid(column=column, row=row, padx=10, pady=10, ipadx=30, ipady=30)
                column += 1
                print(column)
            column = 0
            row += 1
            x += 3
            y += 3


# win1 = Window(400, 500, "asd", 1)
# win1.add_buttons(3, 3)
# win1.centralize()
# win1.mainloop()
print(MathOperations.addition(3, 2))
# print(win1.centralize())