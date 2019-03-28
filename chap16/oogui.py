import tkinter

class Counter:
    """객체 지향 프로그래밍을 사용한 간단한 카운터 GUI"""
    def __init__(self, parent):
	
        """GUI를 생성한다."""

        # 프레임워크
        self.parent = parent
        self.frame = tkinter.Frame(parent)
        self.frame.pack()

        # 모델
        self.state = tkinter.IntVar()
        self.state.set(1)

        # 현재 상태를 표시하는 레이블
        self.label = tkinter.Label(self.frame, textvariable=self.state)
        self.label.pack()

        # 애플리케이션을 제어하는 버튼들
        self.up = tkinter.Button(self.frame, text='up', command=self.up_click)
        self.up.pack(side='left')
        self.right = tkinter.Button(self.frame, text='quit',
                                        command=self.quit_click)
        self.right.pack(side='left')

    def up_click(self):
        """'up' 버튼에 대한 클릭을 처리"""
        
        self.state.set(self.state.get() + 1)

    def quit_click(self):
        """'quit' 버튼에 대한 클릭을 처리"""
        
        self.parent.destroy()
if __name__ == '__main__':
    window = tkinter.Tk()
    myapp = Counter(window)
    window.mainloop()
    
    