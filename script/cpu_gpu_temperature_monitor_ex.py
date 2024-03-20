import subprocess
import time

def get_cpu_temperatures():
    try:
        output = subprocess.check_output(['sensors']).decode('utf-8')
        temperature_lines = [line.strip() for line in output.split('\n') if 'Core' in line]
        cpu_temperatures = []
        for line in temperature_lines:
            temperature = float(line.split('+')[1].split('°C')[0])
            cpu_temperatures.append(temperature)
        return cpu_temperatures
    except subprocess.CalledProcessError:
        return []

def get_gpu_temperatures():
    try:
        output = subprocess.check_output(['nvidia-smi', '--query-gpu=temperature.gpu', '--format=csv,noheader']).decode('utf-8')
        gpu_temperatures = [float(temp.strip()) for temp in output.strip().split('\n')]
        return gpu_temperatures
    except subprocess.CalledProcessError:
        return []

def monitor_temperatures(interval=5):
    print("Monitoring CPU and GPU temperatures...")
    try:
        while True:
            cpu_temperatures = get_cpu_temperatures()
            gpu_temperatures = get_gpu_temperatures()

            if cpu_temperatures:
                print("CPU Temperatures:")
                for core, temp in enumerate(cpu_temperatures):
                    print(f"Core {core}: {temp}°C")

            if gpu_temperatures:
                print("GPU Temperatures:")
                for index, temp in enumerate(gpu_temperatures):
                    print(f"GPU {index}: {temp}°C")

            time.sleep(interval)
    except KeyboardInterrupt:
        print("Monitoring stopped.")

if __name__ == "__main__":
    monitor_temperatures()

