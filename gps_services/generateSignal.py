from datetime import datetime
import subprocess
import psutil
import time

year_t = datetime.now().strftime("%Y")
year_t_m = str(year_t)[-2:]
date_t = datetime.now().strftime("%j")


def generate_signal() :
    subprocess.run(["gcc", "gpssim.c", "-lm", "-O3", "-o", "gps-sdr-sim","-DUSER_MOTION_SIZE=4000"], cwd="/home/gisnaefde/sii/gps-sdr-sim")
    subprocess.run(["./gps-sdr-sim", "-b", "8", "-e", f"brdc{date_t}0.{year_t_m}n", "-l","55.75911686948662,", "37.616404140886715,", "100"], cwd="/home/gisnaefde/sii/gps-sdr-sim")