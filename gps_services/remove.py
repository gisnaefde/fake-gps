import datetime
from datetime import date, datetime, timedelta
import os

year_by = (datetime.now() - timedelta(days=2)).strftime("%Y")
year_by_m = str(year_by)[-2:]
date_by = (datetime.now() - timedelta(days=2)).strftime("%j")

brdc_gps_file_gz_by = f'/home/gisnaefde/sii/gps-sdr-sim/brdc{date_by}0.{year_by_m}n.gz'
brdc_gps_file_by = f'/home/gisnaefde/sii/gps-sdr-sim/brdc{date_by}0.{year_by_m}n'

def removeFile():
    os.remove(brdc_gps_file_gz_by)
    os.remove(brdc_gps_file_by)