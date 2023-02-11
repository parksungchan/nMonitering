import os, sys
config = None


class CustomClass:
    def __init__(self, config_dict):
        for con in config_dict:
            if type(config_dict[con]) is dict:
                self.__setattr__(con, CustomClass(config_dict[con]))
            else:
                self.__setattr__(con, config_dict[con])


def get_cofig_init(config_info):
    global config
    config = CustomClass({})

    # dir list
    dirs = {}
    if getattr(sys, 'frozen', False):
        # .exe로 실행한 경우,.exe를 보관한 디렉토리의 full path를 취득
        dirs['common_dir'] = os.path.split(os.path.dirname(os.path.abspath(sys.executable)))[0]
    else:
        dirs['common_dir'] = os.path.split(os.path.realpath(__file__))[0]

    dirs['src_dir'] = os.path.dirname(dirs['common_dir'])
    dirs['pjt_dir'] = os.path.dirname(dirs['src_dir'])
    dirs['config_dir'] = os.path.join(dirs['pjt_dir'], 'config')
    dirs['data_dir'] = os.path.join(dirs['pjt_dir'], 'data')
    dirs['master_dir'] = os.path.join(dirs['pjt_dir'], 'master')
    dirs['chromedriver_dir'] = os.path.join(dirs['master_dir'], 'chromedriver')
    dirs['data_sub_dir'] = os.path.join(dirs['data_dir'], os.path.basename(config_info['run_path']).replace('.py', ''))
    dirs['result_nv_key'] = os.path.join(dirs['data_dir'], '10.result_nv_key')
    dirs['result_nv_seq'] = os.path.join(dirs['data_dir'], '20.result_nv_seq')
    os.makedirs(dirs['data_dir'], exist_ok=True)

    config = CustomClass(config_info)

    config.__setattr__('dirs', CustomClass({}))
    for ds in dirs:
        config.dirs.__setattr__(ds, dirs[ds])