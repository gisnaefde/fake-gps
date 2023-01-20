import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from moveFileDownload import move_file_download
from exactFile import exact_file
from generateSignal import generate_signal
from datetime import datetime,  timedelta
import os
from remove import removeFile


# options = webdriver.FirefoxOptions()
# options.add_argument('--headless')
# driver = webdriver.Firefox(options=options)
driver = webdriver.Firefox()
# today
year_t = datetime.now().strftime("%Y")
year_t_m = str(year_t)[-2:]
date_t = datetime.now().strftime("%j")

# yesterday
year_y = (datetime.now() - timedelta(days=1)).strftime("%Y")
year_y_m = str(year_y)[-2:]
date_y = (datetime.now() - timedelta(days=1)).strftime("%j")

# before yesterday
year_by = (datetime.now() - timedelta(days=2)).strftime("%Y")
year_by_m = str(year_by)[-2:]
date_by = (datetime.now() - timedelta(days=2)).strftime("%j")

# file_today
brdc_download_file_t = f'/home/gisnaefde/sii/gps-sdr-sim/1_download/brdc{date_t}0.{year_t_m}n.gz'
brdc_gps_file_gz_t = f'/home/gisnaefde/sii/gps-sdr-sim/brdc{date_t}0.{year_t_m}n.gz'
brdc_gps_file_t = f'/home/gisnaefde/sii/gps-sdr-sim/brdc{date_t}0.{year_t_m}n'

# file yesterday
brdc_download_file_y = f'/home/gisnaefde/Downloads/brdc{date_y}0.{year_y_m}n.gz'
brdc_gps_file_gz_y = f'/home/gisnaefde/sii/gps-sdr-sim/brdc{date_y}0.{year_y_m}n.gz'
brdc_gps_file_y = f'/home/gisnaefde/sii/gps-sdr-sim/brdc{date_y}0.{year_y_m}n'

#file before yesterday
brdc_gps_file_gz_by = f'/home/gisnaefde/sii/gps-sdr-sim/brdc{date_by}0.{year_by_m}n.gz'
brdc_gps_file_by = f'/home/gisnaefde/sii/gps-sdr-sim/brdc{date_by}0.{year_by_m}n'

# file brdc
file_t = f"brdc{date_t}0.{year_t_m}n.gz"
file_y = f"brdc{date_y}0.{year_y_m}n.gz"


def download_file():
    print("start download")

    driver.get(f"https://cddis.nasa.gov/archive/gnss/data/daily/{year_t}/brdc/")
    elements = driver.find_element(By.ID, f"brdc{date_t}0.{year_t_m}n.gz")
    id = elements.get_attribute('id')
    #checking, jika file hari ini ada maka download, jika tidak download file kemarin
    if len(id) > 0:
        driver.find_element(By.ID, f"brdc{date_t}0.{year_t_m}n.gz").click()
    else:
        driver.find_element(By.ID, f"brdc{date_y}0.{year_y_m}n.gz").click()

    print("download finish")

def login():
    print("proses login")
    login = "https://urs.earthdata.nasa.gov/home"
    driver.get(login)

    try:
        # get ID
        username = driver.find_element(By.ID, "username")
        password = driver.find_element(By.ID, "password")

        # input data
        username.click()
        username.clear()
        username.send_keys("gisnaefde198")

        password.click()
        password.clear()
        password.send_keys("@Gisnaefde198")

        # klik login
        driver.find_element(By.NAME, "commit").click()

    except:
        print("input data error")

def check_span_text():
    last_span_text = ""
    while True:
        # menghapus file 2 hari kebelakang
        if os.path.exists(brdc_gps_file_gz_by):
            print("start")
            removeFile()
            print("remove process")
            time.sleep(5)
            print("delete success")
        else:
            print("tidak ada file untuk dihapus")

        login()

        url = "https://cddis.nasa.gov/archive/gnss/data/daily/2023/brdc/"
        driver.get(url)
        time.sleep(10)
        pre_tags = driver.find_elements(By.TAG_NAME, "pre")
        for pre_tag in pre_tags:
            div_tags = pre_tag.find_elements(By.TAG_NAME, "div")
            if div_tags:
                last_div = div_tags[-1]
                span_tags = last_div.find_elements(By.TAG_NAME, "span")
                if span_tags:
                    last_span = span_tags[-1]
                    current_span_text = last_span.text
                    if last_span_text != current_span_text:
                        print("Content berubah dari:",last_span_text, "menjadi:", current_span_text)
                        last_span_text = current_span_text
                        download_file()
                        move_file_download()
                        exact_file()
                        generate_signal()
                    else:
                        print("text span tidak berubah")
        time.sleep(60)

check_span_text()
