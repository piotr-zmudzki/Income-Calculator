import shelve
from constants import DATABASE_NAME

#NOT WORKING WITH SHELVE
#brakuje zapisania do pliku
#i załadowania danych w left_frame 
#loop + zapisywanie do listy obiektów

def load_data():
    with shelve.open(DATABASE_NAME) as data:
        return dict(data)

def update_with_data(new_data):
    with shelve.open({DATABASE_NAME}) as db:
        previous_data_dict = load_data()
        print(previous_data_dict, new_data)
        merged = {**previous_data_dict, **new_data}
        print(f"merged: {merged}")
        #print(previous_data_dict, merged_dict, new_data)
        db.update(merged)