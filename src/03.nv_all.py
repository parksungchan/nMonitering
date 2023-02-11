import  datetime
import time

from src.common.get_utils import get_cofig_init
get_cofig_init()

'''
    네이버 광고 사이트에 각 키워드 별로 얼마의 금액이 책정되어 있는지 확인할 수 있다.
'''
from src.common.get_utils import nv_down_excel
from src.common.get_utils import nv_load_excel
from src.common.get_utils import nv_down_seq

start = datetime.datetime.now()
nv_down_excel()
time.sleep(2)
nv_load_excel()
time.sleep(2)
nv_down_seq()
print('[Start] ', start)
print('[Complete] ', datetime.datetime.now())
print('[Total] ', datetime.datetime.now() - start)