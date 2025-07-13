import openai
import json
import os


class DevianaCore:
    def __init__(self, api_key: str = None, memory_file: str = "deviana_memory.json"):
            self.api_key = api_key or "sk-..."  # Replace with your OpenAI API key
                    openai.api_key = self.api_key
                            self.memory_file = memory_file
                                    self.memory = self.load_memory()

                                        def load_memory(self):
                                                if not os.path.exists(self.memory_file):
                                                            return {
                                                                            "conversations": [],
                                                                                            "user_profile": {},
                                                                                                            "business_ideas": []
                                                                                                                        }
                                                                                                                                with open(self.memory_file, "r") as f:
                                                                                                                                            return json.load(f)

                                                                                                                                                        def save_memory(self):
                                                                                                                                                                # Save memory to the JSON file
                                                                                                                                                                        with open(self.memory_file, "w") as f:
                                                                                                                                                                                    json.dump(self.memory, f, indent=4)

                                                                                                                                                                        def generate_response(self, user_message: str) -> str:
                                                                                                                                                                                try:
                                                                                                                                                                                            self.memory["conversations"].append({
                                                                                                                                                                                                            "role": "user",
                                                                                                                                                                                                                            "content": user_message
                                                                                                                                                                                                                                        })
                                                                                                                                                                                                                                                    self.save_memory()

                                                                                                                                                                                                                                                # Generate a response from OpenAI
                                                                                                                                                                                                                                                            response = openai.ChatCompletion.create(
                                                                                                                                                                                                                                                                            model="gpt-4",
                                                                                                                                                                                                                                                                                            messages=[
                                                                                                                                                                                                                                                                                                                {"role": "system", "content": "You are Deviana, a smart AI assistant that helps users build and manage business empires."},
                                                                                                                                                                                                                                                                                                                                    *self.memory["conversations"]
                                                                                                                                                                                                                                                                                                                                                    ],
                                                                                                                                                                                                                                                                                                                                                                    temperature=0.7