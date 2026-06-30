class CourseApp:

    def __init__(self, services):
        self.running = True
        self.service = services

    def start(self):
        while self.running:
            self.menu_course()
            choice = input("Votre choix : ")
            self.handle_choice(choice)

    def menu_course(self):
        print()
        print("=== Studio Bookking Manager ===\n")
        print("1. Créer un cours\n")
        print("2. Afficher les cours\n")
        print("3. Inscrire une personne à un cours\n")
        print("4. Afficher les cours complets\n")
        print("5. Quitter\n")

    def handle_choice(self, choice):
        match choice:
            case "1":
                self.menu_add_course()
            case "2":
                self.menu_all_course()
            case "3":
                self.menu_register_course()
            case "4":
                self.menu_complet_course()
            case "5":
                print("\nFermeture de l'application.")
                self.running = False
            case _:
                print("Choix invalide")

    def menu_all_course(self):
        courses = self.service.get_all_course()
        self.all_course(courses)

    def menu_complet_course(self):
        courses = self.service.get_complet_course()
        self.display_complet_course(courses)

    def menu_add_course(self):
        name_course = input("Nom du cours : ")
        name_coach = input("Non du coach : ")
        capacity_of_participants = input("Nombre de participants maximum : ")
        price = input("Prix du cours : ")

        if not name_coach.isalpha():
            print("Le nom du coach ne doit contenir que des lettres")
            return

        try:
            capacity_of_participants = float(capacity_of_participants)
        except ValueError:
            print("Nombre invalide")
            return
        try:
            price = float(price)
        except ValueError:
            print("Prix invalide")
            return

        success, message = self.service.add_course(name_course, name_coach, capacity_of_participants, price)
        if not success:
            print("\nERREUR !")
        print(message)

    def menu_register_course(self):
        course_id = input("Identifiant du cours : ")
        try:
            course_id = int(course_id)
        except ValueError:
            print("\nIdentifiant invalide")
            return
        success, message = self.service.register_to_course(course_id)
        print(message)

    def all_course(self, courses):
        if len(courses) == 0:
            print("Aucun cours à afficher.")
            return
        for course in courses:
            places_restantes = course.capacity_of_participants - course.registered_count
            prix_euros = course.price / 100
            ca_potentiel = (course.capacity_of_participants * course.price) / 100
            ca_actuel = (course.registered_count * course.price) / 100
            print()
            print(f"#{course.id} - {course.name_course}")
            print(f"Coach : {course.name_coach}")
            print(f"Places : {course.registered_count} / {course.capacity_of_participants}")
            print(f"Places restantes : {places_restantes}")
            print(f"Prix du cours : {prix_euros:.2f} €")
            print(f"CA potentiel : {ca_potentiel:.2f} €")
            print(f"CA actuel : {ca_actuel:.2f} €")

    def display_complet_course(self, courses):
        if len(courses) == 0:
            print("Aucun cours complet.")
            return
        print("\nCours complets :")
        for course in courses:
            print()
            print(f"#{course.id} - {course.name_course}")
            print(f"Coach : {course.name_coach}")
            print(f"Places : {course.registered_count} / {course.capacity_of_participants}")