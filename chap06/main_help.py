'''
이 모듈은 공룡 여부를 추측합니다.
'''

def is_dinosaur(name):
    '''
    공룡 이름이면 True, 아니면 False를 반환합니다.
    '''
    return name in ['Tyrannosaurus', 'Triceratops']
if __name__ == '__main__':
    help(__name__)
