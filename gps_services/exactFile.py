import datetime
from datetime import datetime
import shutil
import gzip


# today
year_t = datetime.now().strftime("%Y")
year_t_m = str(year_t)[-2:]
date_t = datetime.now().strftime("%j")

def move_file():
    # move file
    print("start move")
    src_path = f'/home/gisnaefde/sii/gps-sdr-sim/1_download/brdc{date_t}0.{year_t_m}n.gz'
    dst_path = f'/home/gisnaefde/sii/gps-sdr-sim/2_exact/brdc{date_t}0.{year_t_m}n.gz'
    shutil.move(src_path, dst_path)
    print("move finish")

# exact file
def exact_file():
    print("start exact")
    with gzip.open(f'/home/gisnaefde/sii/gps-sdr-sim/brdc{date_t}0.{year_t_m}n.gz', 'rb') as f_in:
        with open(f'/home/gisnaefde/sii/gps-sdr-sim/brdc{date_t}0.{year_t_m}n', 'wb')as f_out:
            shutil.copyfileobj(f_in, f_out)
    print("exact finish")

