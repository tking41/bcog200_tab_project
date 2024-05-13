import csv

class Guitar:
    def __init__(self, database):
        self.database = database

    def load_database(self):
        with open(self.database, 'r') as file:
            database_reader = csv.reader(file)
            headers = next(database_reader)
            song_tuple_list = []
            for row in database_reader:
                song_tuple_list.append(tuple(row))
            return song_tuple_list

    def print_instructions(self):
        with open("project_instructions.txt", 'r') as file:
            instructions = file.read()
            print(instructions)

    def ask_questions(self, song_tuple_list):
        valid_response = False 
        while not valid_response:
            accepted_response = ["A", "B", "C"] 
            difficulty = input("What difficulty do you want to search for? \n\tA. Novice\n\tB. Intermediate\n\tC. Advanced\n")

            if difficulty in accepted_response:
                valid_response = True
                break
            print("Invalid Response. Please try again.")

        valid_response = False
        while not valid_response:
            accepted_response = ["A", "B", "C"] 
            amount = input("How many song recommendations would you like? \n\tA. 5\n\tB. 10\n\tC. 15\n")
            if amount in accepted_response:
                valid_response = True
                break
            print("Invalid Response. Please try again.")

        responses_tuple_list = (difficulty, amount)
        filtered_songs, num_recommendations = self.output_format(song_tuple_list, responses_tuple_list)

        valid_response = False
        if difficulty != "C": #Since there are only 5 advanced songs, this question does not get asked if they chose C
            accepted_response = ["A", "B"]  
            while not valid_response:
                response = input("Would you like more recommendations? \n\tA. Yes\n\tB. No\n")
                if response in accepted_response:
                    valid_response = True
                else:
                    print("Invalid Response. Please try again.")
                if response == "B":
                    break

        #Takes the original number of song recs the user chose, so it skips over the songs that already printed, and prints the next 10
        next_recommended_songs = filtered_songs[num_recommendations:num_recommendations + 10]   

        #The "Additional Recommendations" will not be printed if they chose the advanced level
        if difficulty != "C":
            print("\nAdditional Recommendations:\n")
            for song in next_recommended_songs:
                print(f"{song[0]} - {song[1]}, Key:{song[6]}, Capo:{song[7]}, Tuning:{song[8]}")
            print()

    def output_format(self, song_tuple_list, responses_tuple_list):
        difficulty, amount = responses_tuple_list
        difficulty_mapping = {"A": "Novice", "B": "Intermediate", "C": "Advanced"}

        #Makes a tuple with a list of songs that matches the difficulty the user selected 
        filtered_songs = [song for song in song_tuple_list if song[5].strip().lower() == difficulty_mapping[difficulty].lower()]

        #Assigns integers to the answers the user input for the number of recommendations they want and saves them as a variable
        if amount == "A":
            num_recommendations = 5
        elif amount == "B":
            num_recommendations = 10
            if difficulty == "C" and amount == "B":
            	print("There are only 5 advanced songs in this database.\n")
        else:  # Assuming "C" for 15 recommendations
            num_recommendations = 15
            if difficulty == "C" and amount == "B":
            	print("There are only 5 advanced songs in this database.\n")

        #Uses the variable of the number of recs to get the number of filtered songs to save
        recommended_songs = filtered_songs[:num_recommendations] 

        print("Recommended Songs for", difficulty_mapping[difficulty], "Players:\n")
        for song in recommended_songs:
            print(f"{song[0]} - {song[1]}, Key:{song[6]}, Capo:{song[7]}, Tuning:{song[8]}") 
        print() #aesthetic reasons

        return filtered_songs, num_recommendations

def main():
    guitar = Guitar("guitarDB.csv")  
    song_tuple_list = guitar.load_database()
    guitar.print_instructions()
    responses_tuple_list = guitar.ask_questions(song_tuple_list) 
    

if __name__ == "__main__":
    main()
