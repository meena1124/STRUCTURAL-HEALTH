import random
import time

# Set thresholds
VIBRATION_THRESHOLD = 5.0    # mm/s
STRAIN_THRESHOLD = 250       # microstrain

def read_vibration_sensor():
    """Simulate vibration sensor reading (0–10 mm/s)."""
    return round(random.uniform(0, 10), 2)

def read_strain_sensor():
    """Simulate strain sensor reading (100–300 microstrain)."""
    return random.randint(100, 300)

def check_anomalies(vibration, strain):
    """Check if readings exceed thresholds."""
    anomalies = []
    if vibration > VIBRATION_THRESHOLD:
        anomalies.append(f"High vibration: {vibration} mm/s")
    if strain > STRAIN_THRESHOLD:
        anomalies.append(f"High strain: {strain} µε")
    return anomalies

def monitor_structure(cycles=10, interval=1):
    """Main monitoring loop."""
    print("=== Structural Health Monitoring ===")
    for i in range(1, cycles + 1):
        vibration = read_vibration_sensor()
        strain = read_strain_sensor()
        print(f"\nCycle {i}:")
        print(f" Vibration: {vibration} mm/s")
        print(f" Strain: {strain} µε")

        anomalies = check_anomalies(vibration, strain)
        if anomalies:
            print("  ⚠️ Anomalies Detected:")
            for anomaly in anomalies:
                print(f"   - {anomaly}")
        else:
            print("  ✅ Structure is stable.")

        time.sleep(interval)

    print("\nMonitoring complete.")
if __name__ == "__main__":
    monitor_structure()
def check_anomalies(vibration, strain):
    """Check if readings exceed thresholds."""
    anomalies = []
    if vibration > VIBRATION_THRESHOLD:
        anomalies.append(f"High vibration: {vibration} mm/s")
    if strain > STRAIN_THRESHOLD:
        anomalies.append(f"High strain: {strain} µε")
    return anomalies

def monitor_structure(cycles=10, interval=1):
    """Main monitoring loop."""
    print("=== Structural Health Monitoring ===")
    for i in range(1, cycles + 1):
        vibration = read_vibration_sensor()
        strain = read_strain_sensor()
        print(f"\nCycle {i}:")
        print(f" Vibration: {vibration} mm/s")
        print(f" Strain: {strain} µε")

        anomalies = check_anomalies(vibration, strain)
        if anomalies:
            print("  ⚠️ Anomalies Detected:")
            for anomaly in anomalies:
                print(f"   - {anomaly}")
        else:
            print("  ✅ Structure is stable.")

        time.sleep(interval)

    print("\nMonitoring complete.")

if __name__ == "__main__":
    monitor_structure()

