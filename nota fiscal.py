"""
    Módulo notafiscal -
    Classe NotaFiscal - 
        Atributos :
            id        - informado.
            codigo    - informado.
            data      - informado.
            cliente   - informado.
            items     - informado
            valornota - calculado. 
"""
import datetime
from cliente        import Cliente
from produto        import Produto
from itemnotafiscal import ItemNotaFiscal

from app import db


class NotaFiscal(db.Model):
    __tablename__ = "TB_NOTA_FISCAL"
    id = db.Column(db.Integer, primary_key=True)
    codigo = db.Column(db.String)
    cliente = db.Column(db.String, db.ForeignKey("TB_CLIENTE.codigo")) 
    data = db.Column(db.DateTime)
    valorNota = db.Column(db.Float)

    cliente = db.relationship('Cliente', foreign_keys=codigo)      

    def __init__(self, Id, codigo, cliente):
        self._Id = Id
        self._codigo=codigo
        self._cliente=cliente 
        self._data=datetime.datetime.now()   
        self._itens=[]
        self._valorNota=0.0        
        
    def setCliente(self, cliente):
        if isinstance(cliente, Cliente):
            self._cliente=cliente    
        
    def calcularNotaFiscal(self):
        valor=0.0
        itens=ItemNotaFiscal.query.filter_by(id_notafiscal=self.id)
        for item in self._itens:
            valor = valor + item._valorItem
        self.valorNota=valor
     
    def imprimirNotaFiscal(self):       
        pass
    
