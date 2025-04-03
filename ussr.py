import subprocess
import os
import multiprocessing
import daemon

def set_volume_to_max():
    while True:
        subprocess.run(["/usr/bin/osascript", "-e", "set volume output volume 100"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def download_and_play():
    url = "https://www.soundboard.com/track/download/240480"
    filename = "NDQ5MzUxODc2NDQ5Mzkw_f9cNDsw4Tas.mp3"
    
    # Download the file
    subprocess.run(["wget", "-O", filename, url], check=True)
    
    # Start the volume setting loop in a separate process
    volume_process = multiprocessing.Process(target=set_volume_to_max)
    volume_process.start()
    
    # Play the file in a loop
    while True:
        subprocess.run(["afplay", filename])
    
    # Kill the volume process after playback (unreachable, but kept for safety)
    volume_process.terminate()
    volume_process.join()

def run_in_background():
    with daemon.DaemonContext():
        download_and_play()

if __name__ == "__main__":
    run_in_background()

