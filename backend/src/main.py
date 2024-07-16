from fastapi import FastAPI, Request


app = FastAPI(title="Cryptify")

app.include_router()