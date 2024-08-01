import os

def record_signal(sample_rate, frequency, file_name):
    command = f"sudo hackrf_transfer -s {sample_rate} -f {frequency} -r {file_name} -n 20000000"
    print(f"Executing: {command}")
    os.system(command)

def replay_signal(sample_rate, frequency, file_name):
    command = f"sudo hackrf_transfer -s {sample_rate} -f {frequency} -t {file_name} -a 1 -x 24 -n 20000000"
    print(f"Executing: {command}")
    os.system(command)

def main3():
    sample_rate = input("Enter the sample rate in MHz: ")+"000000"
    frequency = input("Enter the frequency in MHz: ")+"000000"
    file_name = "signal"
    
    # Record the signal
    print("Recording the signal...")
    record_signal(sample_rate, frequency, file_name)
    
    # Replay the signal
    print("Replaying the signal...")
    replay_signal(sample_rate, frequency, file_name)

if __name__ == "__main__":
    main3()
