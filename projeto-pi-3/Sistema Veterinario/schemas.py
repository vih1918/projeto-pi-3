from pydantic import BaseModel

# Este é o filtro para quando o funcionário for CADASTRAR um animal
# Não colocamos o 'id' aqui, porque o banco de dados gera isso sozinho!

class AnimalCreate(BaseModel):
    nome: str
    especie: str
    raca: str
    idade: int
    dono: str

# Este é o filtro para quando o sistema DEVOLVER a ficha do animal

class AnimalResponse(AnimalCreate):
    id: int

class Config:
    from_attributes = True # Permite que o Pydantic leia dados do SQLAlchemyty