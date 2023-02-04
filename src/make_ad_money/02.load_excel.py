import os
import pandas as pd
from src.common.get_config import get_cofig_init
get_cofig_init()
from src.common.get_config import config

money_dir_list = [x for x in os.listdir(config.dirs.data_dir) if x.find('money_') > -1]

for md in money_dir_list:
    money_dir = os.path.join(config.dirs.data_dir, md)
    file_list = os.listdir(money_dir)
    for file in file_list:
        file_path = os.path.join(money_dir, file)

        print(file_path)




