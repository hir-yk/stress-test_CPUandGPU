# System Stress and Temperature Monitoring Tools

This repository contains two Python scripts for stressing and monitoring the temperatures of CPU and GPU on a system.

## cpu_gpu_stress.py

`cpu_gpu_stress.py` is a script designed to apply a specified load to the CPU and GPU to test their performance and cooling systems.

### Description

The script uses the `stress-ng` tool to stress the CPU and the `gpu_burn` tool to stress the GPU. It allows you to specify the load percentage for each component.

### Usage

To use the script, you need to pass two arguments: the CPU load percentage and the GPU load ratio. Both should be integers between 0 and 100.

```
python3 cpu_gpu_stress.py
```

For example, to apply a 50% load to the CPU and a 75% load to the GPU, run:

```
python3 cpu_gpu_stress.py 50 75
```

### Prerequisites

- `stress-ng` must be installed on your system for CPU stress testing.
- `gpu_burn` must be installed on your system for GPU stress testing.

### Warning

Excessive stress testing can potentially damage your hardware. Use this script with caution and monitor your system's temperatures closely.

## cpu_gpu_temperature_monitor.py

`cpu_gpu_temperature_monitor.py` is a script that monitors and displays the temperatures of the CPU and GPU at regular intervals.

### Description

The script uses the `sensors` command to retrieve CPU temperatures and the `nvidia-smi` command for NVIDIA GPU temperatures.

### Usage

To start monitoring temperatures, simply run the script without any arguments:

```
pytnon3 cpu_gpu_temperature_monitor.py
```

By default, the script updates the temperature readings every 5 seconds. To stop the monitoring, use the keyboard interrupt (Ctrl+C).

### Prerequisites

- The `sensors` command must be available on your system for CPU temperature monitoring.
- The `nvidia-smi` command must be available on your system for NVIDIA GPU temperature monitoring. For other GPU brands, you may need to use different tools.

### Note

Ensure that your system has the necessary sensors and that they are properly configured to provide accurate temperature readings.

## License

This project is licensed under the Apache License 2.0  - see the [LICENSE](LICENSE) file for details.
