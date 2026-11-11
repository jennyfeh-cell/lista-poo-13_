from datetime import datetime

class Horario:
    def __init__(self, id, data, id_profissional=0, id_cliente=None, id_servico=None):
        self._id = id
        self.set_data(data)
        self._id_profissional = id_profissional
        self._id_cliente = id_cliente
        self._id_servico = id_servico

    def get_id(self):
        return self._id

    def set_id(self, id):
        self._id = id

    def get_data(self):
        return self._data

    def set_data(self, data):
        if isinstance(data, str):
            dt = datetime.strptime(data, "%d/%m/%Y %H:%M")
        else:
            dt = data
            
        if dt.year < 2025:
            raise ValueError("Ano do horário não pode ser anterior a 2025.")
        self._data = dt

    def get_id_profissional(self):
        return self._id_profissional

    def set_id_profissional(self, id_prof):
        self._id_profissional = id_prof

    def get_id_cliente(self):
        return self._id_cliente

    def set_id_cliente(self, id_cli):
        self._id_cliente = id_cli

    def get_id_servico(self):
        return self._id_servico

    def set_id_servico(self, id_serv):
        self._id_servico = id_serv