# src/my_agent/history_manager.py
import json
import os

HISTORY_PATH = "data/history.json"

class HistoryManager:
    def __init__(self):
        os.makedirs("data", exist_ok=True)
        if not os.path.exists(HISTORY_PATH):
            with open(HISTORY_PATH, "w", encoding="utf-8") as f:
                json.dump([], f, indent=4)

    def load_history(self):
        try:
            with open(HISTORY_PATH, "r", encoding="utf-8") as f:
                return json.load(f)
        except:
            return []

    def save_history(self, history):
        with open(HISTORY_PATH, "w", encoding="utf-8") as f:
            json.dump(history, f, indent=4, ensure_ascii=False)

    def add_entry(self, question, answer):
        history = self.load_history()
        history.append({
            "question": question,
            "answer": answer
        })
        self.save_history(history)
