import datetime
from datetime import datetime
import shutil


# today
year_t = datetime.now().strftime("%Y")
year_t_m = str(year_t)[-2:]
date_t = datetime.now().strftime("%j")

# move file
def move_file_download():
    # move file
    print("start move")
    src_path = f'/home/gisnaefde/Downloads/brdc{date_t}0.{year_t_m}n.gz'
    dst_path = f'/home/gisnaefde/sii/gps-sdr-sim/brdc{date_t}0.{year_t_m}n.gz'
    shutil.move(src_path, dst_path)
    print("move finish")