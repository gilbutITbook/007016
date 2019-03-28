import tkinter
def change(widget, colors):
    """키가 'red', 'green', 'blue'인 딕셔너리에 저장된 RGB색 값으로
    위젯의 전경색을 업데이트한다. 색 값이 유효한지 확인하지 *않는다*.
    """
	
    new_val = '#'
    for name in ('red', 'green', 'blue'):
        new_val += colors[name].get()
    widget['bg'] = new_val

# 애플리케이션을 생성한다.
window = tkinter.Tk()
frame = tkinter.Frame(window)
frame.pack()

# 빨강, 초록, 파랑을 위한 텍스트 엔트리 위젯을 설정하고,
# 나중에 사용하기 위해 연관된 변수를 딕셔너리에 저장한다.
colors = {}
for (name, col) in (('red', '#FF0000'),
                    ('green', '#00FF00'),
                    ('blue', '#0000FF')):
    colors[name] = tkinter.StringVar()
    colors[name].set('00')
    entry = tkinter.Entry(frame, textvariable=colors[name], bg=col,
                          fg='white')
    entry.pack()
	
# 현재 색을 표시한다.
current = tkinter.Label(frame, text='     ', bg='#FFFFFF')
current.pack()

# 사용자가 색을 업데이트할 수 있는 방법을 제공한다.
update = tkinter.Button(frame, text='Update',
                        command=lambda: change(current, colors))
update.pack()
tkinter.mainloop()
