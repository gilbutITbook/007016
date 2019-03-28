# 모델.
counter = tkinter.IntVar()
counter.set(0)

# 매개변수가 있는 컨트롤러 한 개
def click(variable, value):
    variable.set(variable.get() + value)
