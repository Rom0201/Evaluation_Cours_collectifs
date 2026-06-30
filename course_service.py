from sqlalchemy import select
from models import GroupClasses

class CourseService:
    def __init__(self, database):
        self.database = database # fonction qui sert a récuperer les données de la database

    def add_course(self, name_course, name_coach, capacity_of_participants, price):
        name_course = name_course.strip()
        name_coach = name_coach.strip()
        price=(price * 100)
        
        if name_course == "":
            return (False, "\nLe nom est invalide")
        
        if name_coach == "":
            return (False, "\nLe nom du coach est invalide")
        
        if capacity_of_participants <= 0:
            return (False, '\nLe nombre doit être de 1 minimum')
        
        if price <= 0:
            return (False, '\nLe prix doit être positif')
        

        with self.database.create_session()as session:
            course = GroupClasses(
                name_course=name_course,
                name_coach=name_coach,
                capacity_of_participants=capacity_of_participants,
                price=price,
            )
         
            session.add(course)
            session.commit()
            
        return True, "\nCours ajouté avec succés."
        
    def get_all_course(self):
        with self.database.create_session() as session:
            statement = select(GroupClasses)
            courses = session.scalars(statement).all()
            return courses
    
    def get_complet_course(self):
        with self.database.create_session() as session:
            statement = select(GroupClasses).where(
             GroupClasses.status == "disponible")

            courses = session.scalars(statement).all()
            return courses