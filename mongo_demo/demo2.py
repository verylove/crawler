#encoding: utf-8

from selenium import webdriver
from lxml import etree


driver_path = r"D:\ProgramApp\chromedriver\chromedriver.exe"
driver = webdriver.Chrome(executable_path=driver_path)


driver.get("http://study.163.com/course/courseMain.htm?courseId=1004285004")

text = driver.page_source

html = etree.HTML(text)

times = html.xpath("//span[@class='f-fr f-thide kstime']/text()")
minutes = 0
seconds = 0
for time in times:
    minute_str,second_str = time.split(":")
    minute = int(minute_str)
    second = int(second_str)
    minutes += minute
    seconds += second
second_minutes = seconds/60
minutes += second_minutes
print(minutes)
print(minutes/60)
