import csv

class Guitar:
	def __init__(self, database):
		self = None
		self.database = database 	#????????????????????????????????
		self.artist = None
		self.song_name = None
		self.song_rating = None
		self.song_hits = None
		self.page_type = None
		self.difficulty = None
		self.key = None
		self.capo = None
		self.tuning = None
"""
maybe 2 csv files and 1 txt file
	-the txt would be for explaining how to search through the database by listing the different filters
	-one csv would be the guitar database
	-the other csv would be the questions asked on the command line

simple or advanced search
	-simple search would give a choice of searching by artist, key, tuning, difficulty
	-advanced search is a list of questions
		-what difficulty do you want
		-what key
		-what tuning
"""

	def load_database(self):
		with open("guitarDB.csv", 'r') as file:
			database_reader = csv.reader(file)

			headers = next(database_reader)
		
			song_tuple_list = []

			for row in database_reader:
				song_tuple_list.append(tuple(row))
			#however is this part correct....that is to be seen

	def load_questions(self):
		questions_list = []

		with open("project_questions.csv", 'r') as file:
			question_reader = csv.reader(file)
			for row in question_reader:
				question = row[0]
				questions_list.append(question)

		return questions_list

	def print_instructions(self):
		with open("project_instructions.txt", 'r') as file:
			instructions = file.read()
			print(instructions)

	def ask_questions(self):
		# need to decide if i want users to respond with words or integers

	def output_format(self):
		# want to print out 5-10 options before asking if they want more
		# EXAMPLE PRINT: Jeff Buckley - Hallelujah, Novice, Key: Db, Capo: 1st Fret, Tuning: E A D G B E


def main():
	print_instructions()

if __name__ == "__main__":
    main()