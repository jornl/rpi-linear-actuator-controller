door_state = "open"
def open_door():
    print("opening door")
    door_state = "open"

def close_door():
    print("close door")
    door_state = "closed"

def handle(payload):
    print("Handling it.")
    print(str(payload))
    if door_state == "open":
        close_door()
    else:
        open_door()
