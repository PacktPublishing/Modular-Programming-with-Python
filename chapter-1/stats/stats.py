# stats.py

def init():
    global _stats
    _stats = {}

def event_occurred(event):
    global _stats
    try:
        _stats[event] = _stats[event] + 1
    except KeyError:
        _stats[event] = 1

def get_stats():
    global _stats
    return sorted(_stats.items())
