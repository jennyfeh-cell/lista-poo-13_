from datetime import datetime
# Importe suas classes de Modelo e DAOs se estiverem em arquivos separados:
# from cliente import Cliente
# from profissional import Profissional
# from horario import Horario

class Service:
    # --- MÉTODOS AUXILIARES DE LISTAGEM (Integração com DAO) ---
    @staticmethod
    def cliente_listar():
        return ClienteDAO().listar()

    @staticmethod
    def profissional_listar():
        return ProfissionalDAO().listar()

    @staticmethod
    def horario_listar():
        return HorarioDAO().listar()

    # --- REGRAS DE CLIENTE ---
    @staticmethod
    def cliente_inserir(nome, email, senha):
        email_clean = email.strip().lower()
        if email_clean == "admin":
            raise ValueError("O e-mail 'admin' é reservado para o administrador.")
        
        for c in Service.cliente_listar():
            if c.get_email().lower() == email_clean:
                raise ValueError("E-mail já cadastrado por outro cliente.")
        for p in Service.profissional_listar():
            if p.get_email().lower() == email_clean:
                raise ValueError("E-mail já cadastrado por um profissional.")

        obj = Cliente(0, nome, email, senha)
        ClienteDAO().inserir(obj)

    @staticmethod
    def cliente_atualizar(id, nome, email, senha):
        email_clean = email.strip().lower()
        if email_clean == "admin":
            raise ValueError("O e-mail 'admin' é reservado para o administrador.")

        for c in Service.cliente_listar():
            if c.get_id() != id and c.get_email().lower() == email_clean:
                raise ValueError("E-mail já cadastrado por outro cliente.")
        for p in Service.profissional_listar():
            if p.get_email().lower() == email_clean:
                raise ValueError("E-mail já cadastrado por um profissional.")

        obj = Cliente(id, nome, email, senha)
        ClienteDAO().atualizar(obj)

    @staticmethod
    def cliente_excluir(id):
        for h in Service.horario_listar():
            if h.get_id_cliente() == id:
                raise ValueError("Não é possível excluir: o cliente possui horário agendado.")
        
        obj = Cliente(id, "temp", "temp@temp.com", "123")
        ClienteDAO().excluir(obj)

    # --- REGRAS DE PROFISSIONAL ---
    @staticmethod
    def profissional_inserir(nome, email, senha):
        email_clean = email.strip().lower()
        if email_clean == "admin":
            raise ValueError("O e-mail 'admin' é reservado para o administrador.")
        
        for p in Service.profissional_listar():
            if p.get_email().lower() == email_clean:
                raise ValueError("E-mail já cadastrado por outro profissional.")
        for c in Service.cliente_listar():
            if c.get_email().lower() == email_clean:
                raise ValueError("E-mail já cadastrado por um cliente.")

        obj = Profissional(0, nome, email, senha)
        ProfissionalDAO().inserir(obj)

    @staticmethod
    def profissional_atualizar(id, nome, email, senha):
        email_clean = email.strip().lower()
        if email_clean == "admin":
            raise ValueError("O e-mail 'admin' é reservado para o administrador.")

        for p in Service.profissional_listar():
            if p.get_id() != id and p.get_email().lower() == email_clean:
                raise ValueError("E-mail já cadastrado por outro profissional.")
        for c in Service.cliente_listar():
            if c.get_email().lower() == email_clean:
                raise ValueError("E-mail já cadastrado por um cliente.")

        obj = Profissional(id, nome, email, senha)
        ProfissionalDAO().atualizar(obj)

    @staticmethod
    def profissional_excluir(id):
        for h in Service.horario_listar():
            if h.get_id_profissional() == id:
                raise ValueError("Não é possível excluir: o profissional possui horários cadastrados.")
        
        obj = Profissional(id, "temp", "temp@temp.com", "123")
        ProfissionalDAO().excluir(obj)

    # --- REGRAS DE HORÁRIO ---
    @staticmethod
    def horario_inserir(data_str, id_profissional):
        dt = datetime.strptime(data_str, "%d/%m/%Y %H:%M")
        
        for h in Service.horario_listar():
            if h.get_id_profissional() == id_profissional and h.get_data() == dt:
                raise ValueError("Este profissional já possui um horário cadastrado nessa data e hora.")

        obj = Horario(0, dt, id_profissional)
        HorarioDAO().inserir(obj)

    @staticmethod
    def horario_atualizar(id, data_str, id_profissional, id_cliente=None, id_servico=None):
        dt = datetime.strptime(data_str, "%d/%m/%Y %H:%M")
        
        for h in Service.horario_listar():
            if h.get_id() != id and h.get_id_profissional() == id_profissional and h.get_data() == dt:
                raise ValueError("Conflito de agenda: o profissional já possui outro horário nessa data e hora.")

        obj = Horario(id, dt, id_profissional, id_cliente, id_servico)
        HorarioDAO().atualizar(obj)

    @staticmethod
    def horario_excluir(id):
        for h in Service.horario_listar():
            if h.get_id() == id:
                if h.get_id_cliente() is not None:
                    raise ValueError("Não é possível excluir um horário que já foi agendado por um cliente.")
                break

        obj = Horario(id, datetime(2025, 1, 1, 0, 0))
        HorarioDAO().excluir(obj)