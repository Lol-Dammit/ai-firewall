def respond(action: str, packet_data: dict):
    if action == "block":
        print(f"[BLOCK] Packet: {packet_data}")
    elif action == "alert":
        print(f"[ALERT] Suspicious packet detected.")
    else:
        print(f"[ALLOW] Packet forwarded.")
