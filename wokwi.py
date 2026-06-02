from machine import Pin
import time
# LEDs
green = Pin(4, Pin.OUT)
yellow = Pin(5, Pin.OUT)
red = Pin(2, Pin.OUT)

# Push Button (GPIO15 -> GND)
button = Pin(15, Pin.IN, Pin.PULL_UP)

cycle_count = 0

def all_off():
    green.off()
    yellow.off()
    red.off()

def emergency_mode():
    print("EMERGENCY")

    # Immediately GREEN
    green.on()
    yellow.off()
    red.off()

    time.sleep(5)

    # Wait for button release
    while button.value() == 0:
        time.sleep(0.05)

    # Bonus: Intersection Clear
    print("RED (Intersection Clear)")
    green.off()
    yellow.off()
    red.on()

    time.sleep(2)

    all_off()

# Startup: All LEDs OFF
all_off()

print("Traffic Light System Started")

while True:

    # Emergency check before cycle
    if button.value() == 0:
        emergency_mode()
        continue

    # Bonus: ALL OFF state
    print("ALL OFF")
    all_off()
    time.sleep(1)

    # red
    print("red")
    green.off()
    yellow.off()
    red.on()

    for _ in range(50):  # 5 seconds
        if button.value() == 0:
            emergency_mode()
            break
        time.sleep(0.1)
    else:

        # YELLOW
        print("YELLOW")
        green.off()
        yellow.on()
        red.off()

        for _ in range(20):  # 2 seconds
            if button.value() == 0:
                emergency_mode()
                break
            time.sleep(0.1)
        else:

            # green
            print("green")
            green.on()
            yellow.off()
            red.off()

            for _ in range(50):  # 5 seconds
                if button.value() == 0:
                    emergency_mode()
                    break
                time.sleep(0.1)
            else:
                cycle_count += 1
                print("Cycles Completed:", cycle_count)