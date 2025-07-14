from fastapi import FastAPI
from pydantic import BaseModel
from deviana_core import DevianaCore

# Initialize FastAPI app
app = FastAPI()

# Initialize Deviana core with your OpenAI API key
deviana = DevianaCore(api_key="your-openai-key-here")  # Replace securely

# Input model for POST request
class UserInput(BaseModel):
    message: str

# Route to handle user messages and return Deviana's response
@app.post("/deviana/respond")
def deviana_response(user_input: UserInput):
    reply = deviana.generate_response(user_input.message)
    return {"response": reply}

# Basic root route
@app.get("/")
def root():
    return {"message": "Welcome to Deviana AI — Your business empire"}