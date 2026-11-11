class Cliente:
    def __init__(self, id, nome, email, senha):
        self._id = id
        self.set_nome(nome)
        self.set_email(email)
        self.set_senha(senha)

    def get_id(self):
        return self._id

    def set_id(self, id):
        self._id = id

    def get_nome(self):
        return self._nome

    def set_nome(self, nome):
        if not nome or nome.strip() == "":
            raise ValueError("Nome não pode ser vazio.")
        self._nome = nome.strip()

    def get_email(self):
        return self._email

    def set_email(self, email):
        if not email or email.strip() == "":
            raise ValueError("E-mail não pode ser vazio.")
        self._email = email.strip()

    def get_senha(self):
        return self._senha

    def set_senha(self, senha):
        if not senha or senha.strip() == "":
            raise ValueError("Senha não pode ser vazia.")
        self._senha = senha