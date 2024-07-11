from constants import DATABASE_NAME
import os
#DATABASE_NAME = "data.db"

def load_data() -> list:
    try:
        database = open(DATABASE_NAME, "r")
    except FileNotFoundError:
        database = open(DATABASE_NAME, "w+")
    lines = database.readlines()
    database.close()
    data=[tuple(line.strip().split(",")) for line in lines]

    return data


def append_data(tuple_list: list) -> None:
    print(tuple_list)
    with open(DATABASE_NAME, 'a') as database:
        database.write('\n'.join('%s,%s,%s,%s,%s,%s,%s' % x for x in tuple_list))
        database.write("\n")

def delete_row_from_database(row_number: int) -> None:
    with open(DATABASE_NAME, "r") as input:
        with open("temp.txt", "w") as output:
        # iterate all lines from file
            for line in input:
                # if line starts with substring 'time' then don't write it in temp file
                if not line.strip("\n").startswith(str(row_number)):
                    output.write(line)
    # replace file with original name
    os.replace('temp.txt', DATABASE_NAME)

def edit_row_from_database(row_number: int, new_data: tuple) -> None:
    delete_row_from_database(row_number)
    append_data([(new_data)])

