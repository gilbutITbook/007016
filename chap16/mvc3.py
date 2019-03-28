import tkinter

window = tkinter.Tk()

# 모델
counter = tkinter.IntVar()
counter.set(0)

# 보편적인 컨트롤러
def click(var, value):
    var.set(var.get() + value)

# 뷰
frame = tkinter.Frame(window)
frame.pack()
button = tkinter.Button(frame, text='Up', command=lambda: click(counter, 1))
button.pack()

button = tkinter.Button(frame, text='Down', command=lambda: click(counter, -1))
button.pack()

label = tkinter.Label(frame, textvariable=counter)
label.pack()

window.mainloop()
