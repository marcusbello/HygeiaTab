
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import models
from database import engine
from routers import patient, medical_record, authentication, treatment, medication


app = FastAPI(
    title="HygeiaTab API",
    description="HygeiaTab API Description",
    version="1.0.0",
    docs_url="/docs",  # Set the URL path for the docs page
    redoc_url="/redoc",  # Set the URL path for the ReDoc page
    openapi_url="/openapi.json"  # Set the URL path for the OpenAPI JSON
)

origins = ["http://localhost:4200"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

models.Base.metadata.create_all(bind=engine)

app.include_router(patient.router)
app.include_router(medical_record.router)
app.include_router(treatment.router)
app.include_router(medication.router)
app.include_router(authentication.router)


@app.get("/", tags=['Healthcheck'])
async def root():
    return {"message": "Hello World"}
