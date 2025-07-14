import datetime

def get_timestamp():
    """Returns the current time as a readable string."""
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def summarize_text(text, limit=50):
    """Shortens long strings with an ellipsis."""
    return text if len(text) <= limit else text[:limit] + "..."

def log_event(event):
    """Prints a log message with timestamp."""
    print(f"[{get_timestamp()}] {event}")