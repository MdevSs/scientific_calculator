memory_slots = {
  "A": "0",
  "B": "0",
  "C": "0",
  "D": "0",
  "E": "0",
  "F": "0",
  "G": "0",
  "X": "0",
  "Y": "0",
  "M": "0"
}

def vld_slots():
    """Return list of valid slot keys."""
    return list(memory_slots.keys())

def is_valid_slot(slot: str) -> bool:
    if not slot or not isinstance(slot, str):
        return False
    return slot.strip().upper() in memory_slots

def set_memory(slot: str, value: str) -> bool:
    if not isinstance(slot, str):
        return False
    s = slot.strip().upper()
    if s in memory_slots:
        memory_slots[s] = value
        return True
    return False

def get_memory(slot: str):
    if not isinstance(slot, str):
        return None
    return memory_slots.get(slot.strip().upper(), None)