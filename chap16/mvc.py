import tkinter

# 컨트롤러
def click():
    counter.set(counter.get() + 1)

if __name__ == '__main__':
    window = tkinter.Tk()
    # 모델.
    counter = tkinter.IntVar()
    counter.set(0)
    # 뷰
    frame = tkinter.Frame(window)
    frame.pack()

    button = tkinter.Button(frame, text='Click', command=click)
    button.pack()

    label = tkinter.Label(frame, textvariable=counter)
    label.pack()

    # Start the machinery!
    window.mainloop()
