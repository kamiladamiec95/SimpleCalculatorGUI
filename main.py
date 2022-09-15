from tkinter import *

root = Tk()
root.title("Simple Calculator")

window_width = 400
window_height = 500

center_screen_width = root.winfo_screenwidth()/2
center_screen_height = root.winfo_screenheight()/2

set_window_center_width = int(center_screen_width - window_width/2)
set_window_center_height = int(center_screen_height - window_height/2)

root.geometry(f"{window_width}x{window_height}+{set_window_center_width}+{set_window_center_height}")
root.resizable(False, False)

# root.rowconfigure(0, weight=1)
# root.rowconfigure(1, weight=3)

result = Label(root, background="white", relief="sunken")
result.grid(column=0, row=0, columnspan=3, sticky="WE")

button_dict = {}
# keyboard = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
# column = 0

column = 0
row = 1
x = 1
y = 4

for _ in range (0,3):
    for number in range(x, y):
        # row = 2
        button_dict[number] = Button(root, text=number)
        button_dict[number].grid(column=column, row=row, padx=10, pady=10, ipadx=30, ipady=30)
        column += 1
        print(column)
    column = 0
    row += 1
    x += 3
    y += 3



# button_7 = Button(root, text="7")
# button_7.grid(column=0, row=1, padx=10, pady=10, ipadx=30, ipady=30)
#
# button_8 = Button(root, text="8")
# button_8.grid(column=1, row=1, padx=10, pady=10, ipadx=30, ipady=30)
#
#
# button_9 = Button(root, text="9")
# button_9.grid(column=2, row=1, padx=10, pady=10, ipadx=30, ipady=30)
#
#
# button_4 = Button(root, text="4")
# button_4.grid(column=0, row=2, padx=10, pady=10, ipadx=30, ipady=30)
#
# button_5 = Button(root, text="5")
# button_5.grid(column=1, row=2, padx=10, pady=10, ipadx=30, ipady=30)
#
#
# button_6 = Button(root, text="6")
# button_6.grid(column=2, row=2, padx=10, pady=10, ipadx=30, ipady=30)
#
#
# button_1 = Button(root, text="1")
# button_1.grid(column=0, row=3, padx=10, pady=10, ipadx=30, ipady=30)
#
# button_2 = Button(root, text="2")
# button_2.grid(column=1, row=3, padx=10, pady=10, ipadx=30, ipady=30)
#
#
# button_3 = Button(root, text="3")
# button_3.grid(column=2, row=3, padx=10, pady=10, ipadx=30, ipady=30)
#asd

root.mainloop()

