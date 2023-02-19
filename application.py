import logging
from flask import Flask, render_template, request
from flask_cors import CORS, cross_origin
from scrapper import course_search,all_courses
from mongodb import mongodbconnection as mcon
from mysqldb import mysqlconnection as scon

#Setting up the logging to get the status 
logging.basicConfig(filename="application.log",
                    format='%(asctime)s %(message)s', filemode='w', level=logging.DEBUG)

#Setting up the MySQL database connection
ineuronsqldb = scon(db_name = "Ineuron_Course", table_name = "Course_table")
data_column = "(Title text, Mode text, Description text, Curriculum text, Price int)" 
ineuronsqldb.create_table(data_column)

#Setting up the MongoDb database connection
ineuronmdb = mcon(username = 'rachitmore3', password = 'rachitmore3'
                ,db_name = "Ineuron_Course",db_collection_name = "Course_Collection" )

#Connecting to Flask
app = Flask(__name__)
CORS(app)

#Creating Homepage
@app.route('/', methods=['GET'])
@cross_origin()
def homepage():
    """Route to render the homepage"""
    return render_template("index.html",)

#Creating All Course result page to view all courses
@app.route("/all courses" , methods = ['POST'])
@cross_origin()
def all_course_page():
        """Route to render the all courses page"""
        courses = all_courses()
        return render_template("result1.html",courses=courses)

#Creating Course details result page to the description of specific course
@app.route("/courses" , methods = ['POST', 'GET'])
@cross_origin()
def index():
    """Route to render the courses page"""
    if request.method == 'POST':
        courses = [] #Creating the empty list 
        logging.info("Empty list has been created")
        

        searchString = request.form['content'] #Fetching the form string 
        
        course_details = course_search(searchString) #Using course_search function to get the details of course 
        
        title,mode,description,curriculum,price = course_details #Unpacking tuple to variables 
        logging.info("Tuple unpacking has been done ")
        
        mydict = {"Course Title": title, "Course Mode": mode, "Description": description ,
                  "Course Curriculum": curriculum,"Course Price":price} #Creating dictionary
        
        courses.append(mydict) #Appending the dictionary to list course for result page rendering
        logging.info("Dictionary has been created for course")

        #Creating string to dump data into MySql database
        value = f'({title}","{mode}","{description}","{curriculum}","{price})' 
        ineuronsqldb.insert_data(value)
        logging.info("Result is Dumpped in MySql database")
        
        #Dumping the dictionary to MongoDb database
        ineuronmdb.insert(mydict)
        logging.info("Result is Dumpped in MongoDb database")
        logging.info("User input is taken and results Generated")

        return render_template("result.html",courses=courses)


if __name__ == "__main__":
    app.config['DEBUG'] = True
    app.run(host='0.0.0.0', port=8000)
