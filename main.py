from fastapi import FastAPI
from pydantic import BaseModel
from devaina_core import DevainaCore

# Initialize FastAPI app
app = FastAPI()

# Initialize Deviana core with your OpenAI API key
devaina = DevainaCore(api_key="your-openai-key-here")  # Replace securely

# Input model for POST request
class UserInput(BaseModel):
    message: str

    # Route to handle user messages and return Deviana's response
    @app.post("/deviana/respond")
    def deviana_response(user_input: UserInput):
        reply = devaina.generate_response(user_input.message)
    returpn {"response": reply}

            # Basic root route
            @app.get("/")
            def root():
                return {"message": "Welcome to Deviana AI — Your business empire assist