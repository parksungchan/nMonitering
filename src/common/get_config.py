import os, json
config = None


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
    dirs['common_dir'] = os.path.dirname(os.path.abspath(__file__))
    dirs['src_dir'] = os.path.dirname(dirs['common_dir'])
    dirs['pjt_dir'] = os.path.dirname(dirs['src_dir'])
    dirs['config_dir'] = os.path.join(dirs['pjt_dir'], 'config')
    dirs['data_dir'] = os.path.join(dirs['pjt_dir'], 'data')
    dirs['master_dir'] = os.path.join(dirs['pjt_dir'], 'master')
    dirs['chromedriver_dir'] = os.path.join(dirs['master_dir'], 'chromedriver')

    os.makedirs(dirs['data_dir'], exist_ok=True)

    config_path = os.path.join(dirs['config_dir'], 'config.json')
    if os.path.exists(config_path):
        with open(config_path, 'r', encoding="UTF-8") as fp:
            config_dict = json.load(fp)

        config = CustomClass(config_dict)

    config.__setattr__('dirs', CustomClass({}))
    for ds in dirs:
        config.dirs.__setattr__(ds, dirs[ds])

