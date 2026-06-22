import hashlib
import time
import json

def generate_ephemeral_route(data="test_packet"):
    timestamp = str(int(time.time()))
    # Create ephemeral route ID
    route_id = hashlib.sha256((data + timestamp).encode()).hexdigest()[:16]
    route_info = {
        "route_id": route_id,
        "timestamp": timestamp,
        "expires_in": "60 seconds",
        "status": "ACTIVE - No static surface"
    }
    print("🌻 Sunflower Shield ESR Activated")
    print(json.dumps(route_info, indent=2))
    return route_info

if __name__ == "__main__":
    print("=== SUNFLOWER PROTOCOL DEMO ===")
    for i in range(3):  # Run 3 times to show ephemerality
        generate_ephemeral_route(f"packet_{i}")
        time.sleep(2)
    print("Demo complete. Routes are ephemeral and dynamic.")
