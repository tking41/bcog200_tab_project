import csv
from songs import Guitar

def load_song_tuples(database):
    with open(database, 'r') as file:
        database_reader = csv.reader(file)
        headers = next(database_reader)
        song_tuple_list = []
        for row in database_reader:
            song_tuple_list.append(tuple(row))
        return song_tuple_list

def simulate_and_run(guitar, song_tuple_list, test_tuple):
    guitar.ask_questions = lambda: test_tuple[:2]  
    print("Simulated Responses: {}\n".format(test_tuple))
    guitar.output_format(song_tuple_list, test_tuple[:2]) 

def main():
    guitar = Guitar("guitarDB.csv")
    song_tuple_list = load_song_tuples(guitar.database)
    test_tuples = [("A", "B", "A"), ("B", "C", "B"), ("C", "A")]

    for i, test_tuple in enumerate(test_tuples):
        simulate_and_run(guitar, song_tuple_list, test_tuple)

if __name__ == "__main__":
    main()
