import logging
import json
from flask import Flask, render_template, request
from flask_cors import CORS, cross_origin
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as bs

ineuron_course = "https://ineuron.ai/courses"
uclient = uReq(ineuron_course)
ineuron_page = uclient.read()
uclient.close()
ineuron_html = bs(ineuron_page,"html.parser")
course_description = ineuron_html.findAll("script")
course = course_description[25]
ineuron_course_json = json.loads(course.get_text())
course_list = list(ineuron_course_json['props']['pageProps']['initialState']['init']['courses'].keys())

print(course_list)

string_search =input("enter the course name : ").replace(" ","-")
ineuron_course = "https://ineuron.ai/course/"
course_page = ineuron_course + string_search
uclient = uReq(course_page)
ineuron_page = uclient.read()
uclient.close()
soup = bs(ineuron_page,"html.parser")
course_html = soup.findAll("script")
course = course_html[23]
ineuron_course_json = json.loads(course.get_text())

course_description = ineuron_course_json["props"]["pageProps"]["data"]["details"]["description"]

course_title = ineuron_course_json["props"]["pageProps"]["data"]["details"]["seo"]["keywords"]

course_mode = ineuron_course_json["props"]["pageProps"]["data"]["details"]["mode"]
course_curriculum = ineuron_course_json["props"]["pageProps"]["data"]["meta"]['curriculum']
curriculum_description = []
for i in course_curriculum:
    lst=[]
    for m in course_curriculum[i]["items"]:
        lst.append(m['title'])
    d={course_curriculum[i]["title"]:lst}
    curriculum_description.append(d)
print(f"Course Title : {course_title}" )
print("\n")
print(f"Course Mode : {course_mode}")
print("\n")
print(f"Course Description : {course_description}")