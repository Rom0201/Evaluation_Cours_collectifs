from course_service import CourseService
from course_app import CourseApp
from database import DataBase

def main():
    database = DataBase()
    database.create_tables()
    
    services = CourseService(database)
    app = CourseApp(services)
    app.start()

if __name__== "__main__":
 main()
