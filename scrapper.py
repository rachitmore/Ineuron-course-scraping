import logging
import json
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as bs

logging.basicConfig(filename="Scrapper.log",
                    format='%(asctime)s %(message)s', filemode='w', level=logging.DEBUG)

def all_courses():
    try:
        ineuron_course = "https://ineuron.ai/courses"
        
        uclient = uReq(ineuron_course)
        logging.info("Sent request to fetch url page")
        
        ineuron_page = uclient.read()
        logging.info("Url read")
           
        uclient.close()
        logging.info("File closed")
        
        soup = bs(ineuron_page,"html.parser")
        logging.info("Soup created")
        
        course_description = soup.findAll("script")
        logging.info("Found Script from soup")

        course = course_description[25]
        
        ineuron_course_json = json.loads(course.get_text())
        logging.info("File loaded in json")
        
        course_list = list(ineuron_course_json['props']['pageProps']['initialState']['init']['courses'].keys())
        logging.info("Course list has been created")
        
        return course_list
    except Exception as e:
        logging.error(e)

def course_search(course):
    try:
        course = course.replace(" ","-")
        ineuron_course = "https://ineuron.ai/course/"
        course_page = ineuron_course + course
        
        
        uclient = uReq(course_page)
        logging.info("Url responded")
        
        
        ineuron_page = uclient.read()
        logging.info("Read HTML page")
        
        
        uclient.close()
        logging.info("File closed")

        
        soup = bs(ineuron_page,"html.parser")
        logging.info("Soup has been made")

        
        course_html = soup.findAll("script")
        logging.info("Found script in soup")
        course = course_html[23]

        
        ineuron_course_json = json.loads(course.get_text())
        logging.info("Json file has been loaded")

        
        course_description = ineuron_course_json["props"]["pageProps"]["data"]["details"]["description"]
        logging.info("Got course description from json file")

        
        course_title = ineuron_course_json["props"]["pageProps"]["data"]["details"]["seo"]["keywords"]
        logging.info("Got course title from json file")

        
        course_mode = ineuron_course_json["props"]["pageProps"]["data"]["details"]["mode"]
        logging.info("Got course mode from json file")

        
        course_curriculum = ineuron_course_json["props"]["pageProps"]["data"]["meta"]['curriculum']
        logging.info("Got course curriculum from json file")

        course_price = ineuron_course_json["props"]["pageProps"]["data"]["details"]['pricing']["IN"]
        
        curriculum_description = []
        for i in course_curriculum:
            lst=[]
            for m in course_curriculum[i]["items"]:
                lst.append(m['title'])
            d=f'{course_curriculum[i]["title"]} : {lst}'
            curriculum_description.append(d)

        logging.info("List has been created for curriculum description ")

        course_details = course_title,course_mode,course_description,curriculum_description,course_price
        logging.info("Tuple has been created for course details")
        
        return course_details

    except Exception as e:
        logging.error(e)

