import os, copy, datetime, sys
config = None
config_info = {}

class CustomClass:
    def __init__(self, config_dict):
        for con in config_dict:
            if type(config_dict[con]) is dict:
                self.__setattr__(con, CustomClass(config_dict[con]))
            else:
                self.__setattr__(con, config_dict[con])


def get_cofig_init():
    global config
    config = CustomClass({})

    # dir list
    dirs = {}
    if getattr(sys, 'frozen', False):
        # .exe로 실행한 경우,.exe를 보관한 디렉토리의 full path를 취득
        dirs['cur_dir'] = os.path.split(os.path.dirname(os.path.abspath(sys.executable)))[0]
    else:
        dirs['cur_dir'] = os.path.split(os.path.realpath(__file__))[0]
    dirs['src_dir'] = os.path.dirname(dirs['cur_dir'])
    dirs['pjt_dir'] = os.path.dirname(dirs['src_dir'])
    dirs['config_dir'] = os.path.join(dirs['pjt_dir'], 'config')
    dirs['data_dir'] = os.path.join(dirs['pjt_dir'], 'data')
    dirs['master_dir'] = os.path.join(dirs['pjt_dir'], 'master')
    dirs['chromedriver_dir'] = os.path.join(dirs['master_dir'], 'chromedriver')

    os.makedirs(dirs['data_dir'], exist_ok=True)

    config = CustomClass(config_info)

    config.__setattr__('dirs', CustomClass({}))
    for ds in dirs:
        config.dirs.__setattr__(ds, dirs[ds])


def nv_down_seq():
    key_list = []
    get_cofig_init()
    for dr in os.listdir(config.dirs.data_dir):
        if dr.find('_key.txt') > -1:
            file_path = os.path.join(config.dirs.data_dir, dr)
            with open(file_path, 'r', encoding='UTF8') as f:
                lines = f.readlines()[1:]

            for line in lines:
                if line not in key_list:
                    key_list.append(line.replace('\n', ''))


    print('a')



nv_down_seq()
