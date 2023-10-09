from fastapi import FastAPI, Depends, Security, HTTPException
import typing as t
from fastapi.security.http import HTTPBearer, HTTPBasicCredentials, HTTPAuthorizationCredentials
import json
import db
from dotenv import load_dotenv
import os


load_dotenv()




tags_metadata = [
    {"name": "Get"},
    {"name": "Post"},
    {"name": "Put"},
    {"name": "Delete"}
]
app = FastAPI(openapi_tags=tags_metadata)


secret = os.getenv("TOKEN")

security = HTTPBearer()

@app.on_event("startup")
def check_log_dir():
    os.makedirs("log", exist_ok=True)
    open("./log/access.log", "a").close()
    open("./log/error.log", "a").close()

def get_current_user(authorization: HTTPAuthorizationCredentials = Depends(security)) -> dict:
    token = authorization.credentials
    # Here you should check if the token is valid e.g., using your database.
    # For this example, I'll assume a token "my-secret-token" is valid.
    if token == secret:
        return True
    raise HTTPException(status_code=403, detail="Invalid token")


    




@app.post("/clienti", tags=["Post"])
async def clienti(data: dict, user: dict = Depends(get_current_user)):
    
    if data:
        db.insert_cliente(data)
        return {"success": True}
    else:
        return {"success": False, "error": "No data"}
    
@app.post('/forniture', tags=["Post"])
async def forniture(data: dict, user: dict = Depends(get_current_user)):
    if data:
        db.insert_forniture(data)
        return {"success": True}
    else:
        return {"success": False, "error": "No data"}
    
    
@app.post('/contratti', tags=["Post"])
async def contratti(data: dict, user: dict = Depends(get_current_user)):
    if data:
        db.insert_contratti(data)
        return {"success": True}
    else:
        return {"success": False, "error": "No data"}
    
    
    
@app.get("/clienti", tags=["Get"])
async def get_clienti(user: dict = Depends(get_current_user)):
    """
        ordered from oldest to newest
    """
    return db.get_clienti()

@app.get("/forniture", tags=["Get"])
async def get_forniture( user: dict = Depends(get_current_user) ):
    """
        ordered from oldest to newest
    """
    return db.get_forniture()

@app.get("/contratti", tags=["Get"])
async def get_contratti( user: dict = Depends(get_current_user)):
    """
        ordered from oldest to newest
    """
    return db.get_contratti()
    
"""GET BY ID"""
    
@app.get("/clienti/{id}", tags=["Get"])
async def get_cliente_by_id(id: str, user: dict = Depends(get_current_user)):
    return db.get_cliente_by_id(id)

@app.get("/forniture/{id}", tags=["Get"])
async def get_fornitura_by_id(id: str, user: dict = Depends(get_current_user)):
    return db.get_fornitura_by_id(id)

@app.get("/contratti/{id}", tags=["Get"])
async def get_contratto_by_id(id: str, user: dict = Depends(get_current_user)):
    return db.get_contratto_by_id(id)

"""DELETE BY ID"""
@app.delete("/clienti/deleteall", tags=["Delete"])
async def delete_all_clienti(user: dict = Depends(get_current_user)):
    return db.delete_all_clienti()

@app.delete("/clienti/{id}", tags=["Delete"])
async def delete_cliente_by_id(id: str, user: dict = Depends(get_current_user)):
    return db.delete_cliente_by_id(id)

@app.delete("/forniture/{id}", tags=["Delete"])
async def delete_fornitura_by_id(id: str, user: dict = Depends(get_current_user)):
    return db.delete_fornitura_by_id(id)

@app.delete("/contratti/{id}", tags=["Delete"])
async def delete_contratto_by_id(id: str, user: dict = Depends(get_current_user)):
    return db.delete_contratto_by_id(id)
