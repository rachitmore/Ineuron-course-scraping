import logging
from flask import Flask, render_template, request
from flask_cors import CORS, cross_origin
from scrapper import course_search,all_courses
from mongodb import mongodbconnection as mcon
# from mysql import mysqlconnection as scon

logging.basicConfig(filename="application.log",
                    format='%(asctime)s %(message)s', filemode='w', level=logging.DEBUG)

# ineuronsqldb = scon(username = "root", password = "mysql@123"
#                     ,db_name = "Ineuron_Course", table_name = "Course_table")
# data_column = "(Title text, Mode text, Description text, Curriculum text, Price int)" 
# ineuronsqldb.create_table(data_column)

ineuronmdb = mcon(username = 'rachitmore3', password = 'rachitmore3'
                ,db_name = "Ineuron_Course",db_collection_name = "Course_Collection" )


app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
@cross_origin()
def homepage():
    return render_template("index.html",)


@app.route("/all courses" , methods = ['POST'])
@cross_origin()
def all_course_page():
        courses = all_courses()
        return render_template("result1.html",courses=courses)

@app.route("/courses" , methods = ['POST', 'GET'])
@cross_origin()
def index():
    if request.method == 'POST':
        courses = []
        logging.info("Empty list has been created")
        

        searchString = request.form['content']
        course_details = course_search(searchString) 
        
        title,mode,description,curriculum,price = course_details
        logging.info("Tuple unpacking has been done ")
        
        mydict = {"Course Title": title, "Course Mode": mode, "Description": description ,
                  "Course Curriculum": curriculum,"Course Price":price}
        courses.append(mydict)
        logging.info("Dictionary has been created for course")

        # value = f'({title}","{mode}","{description}","{curriculum}","{price})'
        # ineuronsqldb.insert_data(value)
        
        ineuronmdb.insert(mydict)
        logging.info("User input is taken and results Generated")

        return render_template("result.html",courses=courses)


if __name__ == "__main__":
    app.config['DEBUG'] = True
    app.run(host='0.0.0.0', port=8000)
