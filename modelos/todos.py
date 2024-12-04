from modelos.users import User

class Todo(User):
    def __init__(self, idtodo = 0, title = '', completed = '', iduser = 0):
        super().__init__(iduser)
        self.idtodo = idtodo
        self.title = title
        self.completed = completed
