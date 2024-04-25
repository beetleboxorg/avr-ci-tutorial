import serial
import time

def connect_to_device(port, baudrate=9600, timeout=1):
    try:
        ser = serial.Serial(port, baudrate=baudrate, timeout=timeout)
        print(f"Connected to {port}")
        return ser
    except serial.SerialException:
        print(f"Failed to connect to {port}. Retrying...")
        return None

def main(runtime):
    port = '<usb_port_of_avr_microcontroller>'  # Change this to the appropriate port of your USB device eg /dev/ttyACM0
    start_time = time.time()
    while time.time() - start_time < runtime:
        ser = connect_to_device(port)
        if ser is not None:
            try:
                while time.time() - start_time < runtime:
                    data = ser.readline().decode().strip()
                    if data:
                        print("Received:", data)
            except serial.SerialException:
                print(f"Connection to {port} lost. Attempting to reconnect...")
            finally:
                ser.close()
        time.sleep(1)  # Wait before attempting to reconnect

if __name__ == "__main__":
    runtime = 60  # Set the runtime in seconds
    main(runtime)
