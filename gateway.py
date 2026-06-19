from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
import uvicorn

app = FastAPI(title="Sunflower Protocol Sovereign API")

# Simple security check (The beginnings of your monetization!)
API_KEY_CREDIT = "SOVEREIGN_ONE_2026"

class ProtocolRequest(BaseModel):
    key: str
    query: str

@app.get("/")
def read_root():
    return {"status": "Sunflower Protocol Online", "vault": "Secure"}

@app.post("/process")
def process_protocol(request: ProtocolRequest):
    # This is where we charge the 'toll'
    if request.key != API_KEY_CREDIT:
        raise HTTPException(status_code=403, detail="Invalid Access Key. Access Denied.")
    
    # Placeholder for your core Sunflower Logic
    # In the future, this calls your actual protocol functions
    result = f"Sunflower Protocol processed: {request.query}"
    
    return {
        "success": True, 
        "data": result,
        "message": "Sovereign data delivered."
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
