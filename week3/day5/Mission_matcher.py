
class MissionMatcher:
    def validate_age(self, age):
        if age < 18:
            raise Exception("Sorry, only individuals aged 18 and above can volunteer.")
        return True


    def get_preferred_district(self):
        cursor = self.cursor()
        print("Select your preferred area of volunteering:")
        print("1. Jerusalem")
        print("2. North")
        print("3. Haifa")
        print("4. Central")
        print("5. Tel Aviv")
        print("6. South")
        
        try:
            area_choice = int(input("Enter the number corresponding to your preferred area: "))
            areas = {
                1: "Jerusalem",
                2: "North",
                3: "Haifa",
                4: "Central",
                5: "Tel Aviv",
                6: "South"
            }
            if area_choice not in areas:
                print("Invalid choice. Please select a valid area.")
                return None
            return areas[area_choice]
        except ValueError:
            print("Invalid input. Please enter a number.")
            return None

    # def match_profession(self):
    #     professions = {
    #         "Doctor": [4, 10],  # Map professions to corresponding mission IDs
    #         "Vet":[24,27,29,30],
    #         "Psychologist":[16,22,18],
    #         "Driver":[1,7,15,26],
    #         "Teacher":[5,6,14],
    #         "Lawyer":[21,23],
    #         "Cook":[2],
    #         "Financier":[19,25],
    #         "Accountant":[19,25],
    #         "Translator":[12],
    #         "SMM Specialist":[8,17]
    #     }
    #     user_profession = input("Enter your profession: ")

    #     matched_missions = professions.get(user_profession, [])
    #     if matched_missions:
    #         print(f"Matching missions for profession '{user_profession}': {matched_missions}")
    #         return matched_missions
    #     else:
    #         print("No matching missions found for the provided profession.")
    #         return None
        

    # def match_car_needed(self):
    #     user_has_car = input("Do you have a car? (yes/no): ").lower()
    #     if user_has_car == "yes":
    #         matched_car_missions = car_needed = True
    #         print(f"Matching missions for users with cars: {matched_car_missions}")
    #         return matched_car_missions
    #     elif user_has_car == "no":
    #         print("You selected 'no'. Matching missions that do not require a car.")
    #         # Logic for missions that do not require a car
    #         # Replace with your actual database query or logic
    #         # Example: Retrieving missions where 'car_needed' is False
    #         matched_non_car_missions = [3, 9]  # Replace with actual mission IDs
    #         print(f"Matching missions for users without cars: {matched_non_car_missions}")
    #         return matched_non_car_missions
    #     else:
    #         print("Invalid input. Please enter 'yes' or 'no'.")
    #         return None

    # def match_preferred_volunteering_area(self):
    #     volunteering_areas = {
    #         "Medical Support and Aid": [4, 10],  # Mapping areas to corresponding mission IDs
    #         "Psychological assistance and trainings": [16, 22, 18],
    #         "Media and Communication": [8,17],
    #         "Children": [5,6,14],
    #         "Transport and Logistics": [1,7,26,15],
    #         "Office work": [9,12],
    #         "Jurisprudence": [21,23],
    #         "Finance":[19,25],
    #         "Animals": [24,27,29,30],
    #         "Housing for refugees": [11,13,20,28],
    #         "Food and clothing": [2, 3],
    #     }

    #     user_input = input("Enter your preferred volunteering area: ")
    #     matched_area_missions = volunteering_areas.get(user_input, [])

    #     if matched_area_missions:
    #         print(f"Matching missions for area '{user_input}': {matched_area_missions}")
    #         return matched_area_missions
    #     else:
    #         print("No matching missions found for the provided area.")
    #         return None
       

    # def match_skills(self):
    #     skills = {
    #         "Communication": [8,9,17,16,18],  # Mapping skills to corresponding mission IDs
    #         "Foreign languages": [12],
    #         "Cooking": [2],
    #         "Communication with animals": [29, 30],
    #         "Communication with children":[5,14],
    #         "Conduct trainings":[18]
    #     }

    #     user_input = input("Enter your skills: ")
    #     matched_skill_missions = skills.get(user_input.lower(), [])

    #     if matched_skill_missions:
    #         print(f"Matching missions for skill '{user_input}': {matched_skill_missions}")
    #         return matched_skill_missions
    #     else:
    #         print("No matching missions found for the provided skill.")
    #         return None

    # def match_preferred_time(self):
    #     # Logic to match user's preferred time of volunteering with missions' volunteering time
    #     # Return matched missions or None if no matches found
    #     pass
