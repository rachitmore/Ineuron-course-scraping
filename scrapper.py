import logging
import json
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as bs

#Setting up the logging to get the status 
logging.basicConfig(filename="Scrapper.log",
                    format='%(asctime)s %(message)s', filemode='w', level=logging.DEBUG)

#Function to Scrap all course title from the ineuron.ai website 
def all_courses() -> list:
    """
    Function scrapes details from ineuron.ai website
    Returns a list of all courses available on the Ineuron website.
    """

    try:
        #Ineuron Courses website to get the access of all courses
        ineuron_html = "https://ineuron.ai/courses"
        
        #Requesting source code from website and assigning to uclient
        uclient = uReq(ineuron_html) 
        logging.info("Sent request to fetch url sourse code")
        
        #Reading the source code and assigning to variable ineuron_page
        ineuron_page = uclient.read() 
        logging.info("Url read")
           
        uclient.close() #Closing the file 
        logging.info("File closed")
        
        #Making soup of html page to fetch the details from the website assigning to soup
        soup = bs(ineuron_page,"html.parser") 
        logging.info("Soup created")
        
        course_scripts = soup.findAll("script") #Finding all script from the soup 
        logging.info("Found Script from soup")

        #To get the required script indexing the course_scripts and assigning to course_script
        course_script = course_scripts[25]  
        
        #Loading the course script text to json file 
        course_json = json.loads(course_script.get_text())
        logging.info("File loaded in json")
        
        #Creating a courses list from nested dictionaries and assigning to course list 
        courses_list = list(course_json['props']['pageProps']['initialState']['init']['courses'].keys())
        logging.info("Course list has been created")

        #Converting list to string to get the better view in result page
        s="  "
        course_string = s.join(courses_list).replace("  ",",")
        logging.info("list has been converted to string")
        
        return course_string
    
    except Exception as e:
        logging.error(e)

def course_search(course)-> str:
    """
    This function takes course as string type return tuple of course_details consist of 
    course title, course mode, course description, course curriculum and course price
    """
    try:
        #String need to repalce whitespace to -
        course = course.replace(" ","-")

        #Ineuron Course website to get the access of specific course
        course_html = "https://ineuron.ai/course/"
        
        #Concatenate the specific course url with specific course
        course_page = course_html + course
        
        #Requesting source code from website and assigning to uclient
        uclient = uReq(course_page)
        logging.info("Url responded")
        
        #Reading the source code and assigning to variable ineuron_page
        ineuron_page = uclient.read()
        logging.info("Read HTML page")
        
        #Closing file
        uclient.close()
        logging.info("File closed")

        #Making soup of html page to fetch the details from the website assigning to soup
        soup = bs(ineuron_page,"html.parser")
        logging.info("Soup has been made")

        course_scripts = soup.findAll("script")#Finding all script from the soup 
        logging.info("Found script in soup")
        
        #To get the required script indexing the course_scripts and assigning to course_script
        course_script = course_scripts[23]

        #Loading the course script text to json file
        course_json = json.loads(course_script.get_text())
        logging.info("Json file has been loaded")

        #Fetching a course description from nested dictionaries and assigning to course_description
        course_description = course_json["props"]["pageProps"]["data"]["details"]["description"]
        logging.info("Got course description from json file")

        #Fetching a course title from nested dictionaries and assigning to course_title
        course_title = course_json["props"]["pageProps"]["data"]["details"]["seo"]["keywords"]
        logging.info("Got course title from json file")

        #Fetching a courses mode from nested dictionaries and assigning to course_mode
        course_mode = course_json["props"]["pageProps"]["data"]["details"]["mode"]
        logging.info("Got course mode from json file")

        #Fetching a course curriculum from nested dictionaries and assigning to course_curriculum
        course_curriculum = course_json["props"]["pageProps"]["data"]["meta"]['curriculum']
        logging.info("Got course curriculum from json file")

        #Fetching a course price from nested dictionaries and assigning to course_price
        course_price = course_json["props"]["pageProps"]["data"]["details"]['pricing']["IN"]
        
        #creating a curriculum_description list
        curriculum = []

        #For better visualization looping course_curriculum and sagrigate the main topic and sub topic 
        # in an list and nested list 
        for i in course_curriculum:
            lst=[]
            for m in course_curriculum[i]["items"]:
                lst.append(m['title'])
            d=f'{course_curriculum[i]["title"]} : {lst}'
            curriculum.append(d)

        logging.info("List has been created for curriculum description ")

        #Creating tuple of details
        course_details = course_title,course_mode,course_description,curriculum,course_price
        logging.info("Tuple has been created for course details")
        
        return course_details

    except Exception as e:
        logging.error(e)

