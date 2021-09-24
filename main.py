import argparse

def main(database: str,url_list_file:str):
    print("We are going to work with "+database)
    print("We are going to scan "+url_list_file)

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("db","--database",help="SQLite File ")
    parser.add_argument("-i","input",help="File cointaining")
    args = parser.parse_args()
    database_file = args.database
    