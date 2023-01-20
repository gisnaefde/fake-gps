from datetime import datetime
import subprocess
import psutil
import time

# today
year_t = datetime.now().strftime("%Y")
year_t_m = str(year_t)[-2:]
date_t = datetime.now().strftime("%j")


def transmit():

    # cek apakah perintah selesai dengan sukses
    # if result.returncode == 0:
    print("Command completed successfully")
    # running gpssim.bin
    while True:
        for proc in psutil.process_iter():
            try:
                # Check if process name contains 'gnome-terminal'
                if 'gnome-terminal' in proc.name():
                    print("Terminal sedang running")
                    subprocess.run(["hackrf_transfer", "-t", "gpssim.bin", "-f", "1575420000", "-s","2600000", "-a", "1", "-x", "0"], cwd="/home/gisnaefde/sii/gps-sdr-sim/")
                    print("Terminal berhenti")
                    break
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
        else:
            print("Terminal berhenti running, menjalankan kembali...")
            subprocess.Popen(['gnome-terminal'])
            # Sleep for x seconds before checking again
            time.sleep(5)


    print("gps finish")
transmit()

