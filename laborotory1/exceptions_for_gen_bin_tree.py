class BinaryTreeException(Exception):
    def __init__(self, message="Ошибка в бинарном дереве"):
        super().__init__(message)

class InvalidHeightException(BinaryTreeException):
    def __init__(self, h):
        super().__init__(f"Некорректная высота: {h}. Высота должна быть неотрицательным целым числом.")

class InvalidRootException(BinaryTreeException):
    def __init__(self, root):
        super().__init__(f"Некорректный корень: {root}. Корень должен быть числом.")