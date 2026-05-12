from pydantic import BaseModel
from typing import Optional

class AnimalCreate(BaseModel):
    nome:    str
    especie: str
    raca:    str
    idade:   int
    dono:    str

class AnimalResponse(AnimalCreate):
    id: int
    class Config:
        from_attributes = True

class TutorCreate(BaseModel):
    nome:     str
    telefone: str
    cpf:      Optional[str] = None
    email:    Optional[str] = None
    endereco: Optional[str] = None
    pets:     str = "Nenhum"

class TutorResponse(TutorCreate):
    id: int
    class Config:
        from_attributes = True

class VeterinarioCreate(BaseModel):
    nome:          str
    especialidade: str
    telefone:      str
    crmv:          Optional[str] = None

class VeterinarioResponse(VeterinarioCreate):
    id: int
    class Config:
        from_attributes = True

class ServicoCreate(BaseModel):
    nome:      str
    categoria: str
    valor:     float

class ServicoResponse(ServicoCreate):
    id: int
    class Config:
        from_attributes = True

class AgendamentoCreate(BaseModel):
    horario:     str
    nome_pet:    str
    motivo:      str
    veterinario: str
    status:      str = "agendado"
    observacoes: str = ""

class AgendamentoResponse(AgendamentoCreate):
    id: int
    class Config:
        from_attributes = True