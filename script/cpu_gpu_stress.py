import subprocess
import sys
import time

def stress_cpu(cpu_load):
    print(f"Starting CPU stress with {cpu_load}% load on each CPU...")
    try:
        # stress-ngを使用して全てのCPUに指定された負荷をかける
        subprocess.Popen(['stress-ng', '--cpu', '0', '--cpu-load', str(cpu_load)])
    except FileNotFoundError:
        print("Error: stress-ng tool not found. Please make sure it's installed.")
        sys.exit(1)

def stress_gpu(gpu_load_ratio):
    total_duration = 30  # Total duration for GPU stress cycle in seconds
    run_duration = total_duration * gpu_load_ratio / 100
    idle_duration = total_duration - run_duration
    print(f"Starting GPU stress cycle with {run_duration} seconds of load and {idle_duration} seconds of idle time...")

    try:
        while True:  # Repeat the stress cycle until interrupted
            # Start the GPU stress test
            print("GPU stress test is running...")
            subprocess.run(['gpu_burn', str(run_duration)])
            
            # Idle period
            print("GPU is idle...")
            time.sleep(idle_duration)
    except KeyboardInterrupt:
        print("\nStopping GPU stress test.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python stress_program.py <cpu_load> <gpu_load_ratio>")
        sys.exit(1)

    cpu_load = int(sys.argv[1])
    gpu_load_ratio = int(sys.argv[2])

    if cpu_load < 0 or cpu_load > 100 or gpu_load_ratio < 0 or gpu_load_ratio > 100:
        print("Error: Load percentage must be between 0 and 100.")
        sys.exit(1)

    stress_cpu(cpu_load)
    stress_gpu(gpu_load_ratio)

    print("Completed stress test.")
