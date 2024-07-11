from modules import data_manager
from datetime import datetime

try:
    data_manager.append_data([(9, 4, 2, -7, "Kassrsta","2024-07-11", datetime.now().strftime("%H:%M:%S"))])

    print("done")
except Exception as e:
    print(e)

