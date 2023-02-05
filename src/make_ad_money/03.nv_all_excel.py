import time

from src.common.make_ad_utils import nv_down_excel
from src.common.make_ad_utils import nv_load_excel

nv_down_excel()
time.sleep(2)
nv_load_excel()
