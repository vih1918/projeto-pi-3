from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import models
import schemas
from database import engine, SessionLocal

# Cria as tabelas no banco de dados (se não existirem)

models.Base.metadata.create_all(bind=engine)
app = FastAPI(title="Sistema Veterinário")

# Esta função abre e fecha a "porta" do banco de dados para cada pedido

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ---------------------------------------------------------
# ROTAS PARA ANIMAIS
# ---------------------------------------------------------
# 1. Rota POST: CADASTRAR um novo animal

@app.post("/animais/", response_model=schemas.AnimalResponse)
def criar_animal(animal: schemas.AnimalCreate, db: Session = Depends(get_db)):

# Transforma os dados recebidos no modelo do banco de dados

   novo_animal = models.Animal(**animal.model_dump())
   db.add(novo_animal) # Adiciona o animal à sessão
   db.commit() # Salva de verdade no banco de dados
   db.refresh(novo_animal) # Atualiza a variável com o ID que o banco gerou
   return novo_animal

# 2. Rota GET: LER/LISTAR todos os animais

@app.get("/animais/", response_model=list[schemas.AnimalResponse])
def listar_animais(db: Session = Depends(get_db)):

# Busca todos os registos na tabela 'animais'

   animais = db.query(models.Animal).all()
   return animais