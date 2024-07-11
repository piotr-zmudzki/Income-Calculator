from modules import data_manager
from datetime import datetime

try:
    data_manager.append_data([(7, 4, 2, 2, "Kassrsta",datetime.now().strftime("%Y-%m-%d"), datetime.now().strftime("%H:%M:%S"))])


    print("done")
except Exception as e:
    print(e)

