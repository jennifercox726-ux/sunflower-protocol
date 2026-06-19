from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn

app = FastAPI(title="Sunflower Protocol Sovereign API")

# Your first security layer!
API_KEY_CREDIT = "SOVEREIGN_ONE_2026"

class ProtocolRequest(BaseModel):
    key: str
    query: str

@app.get("/")
def read_root():
    return {"status": "Sunflower Protocol Online", "vault": "Secure"}

@app.post("/process")
def process_protocol(request: ProtocolRequest):
    if request.key != API_KEY_CREDIT:
        raise HTTPException(status_code=403, detail="Invalid Access Key.")
    
    return {
        "success": True, 
        "data": f"Sunflower Protocol processed: {request.query}",
        "message": "Sovereign data delivered."
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
