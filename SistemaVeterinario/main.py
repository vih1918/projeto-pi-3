from fastapi import FastAPI, Depends, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
import models, schemas
from database import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Clínica Veterinária")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

templates = Jinja2Templates(directory="templates")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/", response_class=HTMLResponse)
def pagina_inicial(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")

@app.post("/animais/", response_model=schemas.AnimalResponse)
def criar_animal(animal: schemas.AnimalCreate, db: Session = Depends(get_db)):
    obj = models.Animal(**animal.model_dump())
    db.add(obj); db.commit(); db.refresh(obj)
    return obj

@app.get("/animais/", response_model=list[schemas.AnimalResponse])
def listar_animais(db: Session = Depends(get_db)):
    return db.query(models.Animal).all()

@app.delete("/animais/{animal_id}")
def deletar_animal(animal_id: int, db: Session = Depends(get_db)):
    obj = db.get(models.Animal, animal_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Animal não encontrado")
    db.delete(obj); db.commit()
    return {"ok": True}

@app.post("/tutores/", response_model=schemas.TutorResponse)
def criar_tutor(tutor: schemas.TutorCreate, db: Session = Depends(get_db)):
    obj = models.Tutor(**tutor.model_dump())
    db.add(obj); db.commit(); db.refresh(obj)
    return obj

@app.get("/tutores/", response_model=list[schemas.TutorResponse])
def listar_tutores(db: Session = Depends(get_db)):
    return db.query(models.Tutor).all()

@app.delete("/tutores/{tutor_id}")
def deletar_tutor(tutor_id: int, db: Session = Depends(get_db)):
    obj = db.get(models.Tutor, tutor_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Tutor não encontrado")
    db.delete(obj); db.commit()
    return {"ok": True}

@app.post("/veterinarios/", response_model=schemas.VeterinarioResponse)
def criar_veterinario(vet: schemas.VeterinarioCreate, db: Session = Depends(get_db)):
    obj = models.Veterinario(**vet.model_dump())
    db.add(obj); db.commit(); db.refresh(obj)
    return obj

@app.get("/veterinarios/", response_model=list[schemas.VeterinarioResponse])
def listar_veterinarios(db: Session = Depends(get_db)):
    return db.query(models.Veterinario).all()

@app.delete("/veterinarios/{vet_id}")
def deletar_veterinario(vet_id: int, db: Session = Depends(get_db)):
    obj = db.get(models.Veterinario, vet_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Veterinário não encontrado")
    db.delete(obj); db.commit()
    return {"ok": True}

@app.post("/servicos/", response_model=schemas.ServicoResponse)
def criar_servico(servico: schemas.ServicoCreate, db: Session = Depends(get_db)):
    obj = models.Servico(**servico.model_dump())
    db.add(obj); db.commit(); db.refresh(obj)
    return obj

@app.get("/servicos/", response_model=list[schemas.ServicoResponse])
def listar_servicos(db: Session = Depends(get_db)):
    return db.query(models.Servico).all()

@app.delete("/servicos/{servico_id}")
def deletar_servico(servico_id: int, db: Session = Depends(get_db)):
    obj = db.get(models.Servico, servico_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Serviço não encontrado")
    db.delete(obj); db.commit()
    return {"ok": True}

@app.post("/agendamentos/", response_model=schemas.AgendamentoResponse)
def criar_agendamento(agenda: schemas.AgendamentoCreate, db: Session = Depends(get_db)):
    obj = models.Agendamento(**agenda.model_dump())
    db.add(obj); db.commit(); db.refresh(obj)
    return obj

@app.get("/agendamentos/", response_model=list[schemas.AgendamentoResponse])
def listar_agendamentos(db: Session = Depends(get_db)):
    return db.query(models.Agendamento).all()

@app.delete("/agendamentos/{agenda_id}")
def deletar_agendamento(agenda_id: int, db: Session = Depends(get_db)):
    obj = db.get(models.Agendamento, agenda_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Agendamento não encontrado")
    db.delete(obj); db.commit()
    return {"ok": True}