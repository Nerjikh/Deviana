import json
import os

class Memory:
    def __init__(self, memory_file="data/deviana_memory.json"):
        self.memory_file = memory_file
        self.knowledge = {}

    def load(self):
        if os.path.exists(self.memory_file):
            with open(self.memory_file, "r") as file:
                self.knowledge = json.load(file)
            print("🧠 Memory loaded.")
        else:
            print("⚠️ No memory found. Starting fresh.")
            self.knowledge = {}

    def save(self):
        with open(self.memory_file, "w") as file:
            json.dump(self.knowledge, file, indent=4)
        print("💾 Memory saved.")

    def remember(self, key, value):
        self.knowledge[key] = value
        self.save()

    def recall(self, key):
        return self.knowledge.get(key, "❓ I don't remember that.")