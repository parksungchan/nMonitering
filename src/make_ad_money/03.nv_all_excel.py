import os, sys, time
pjt_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(pjt_dir)

from src.common.make_ad_utils import nv_down_excel
from src.common.make_ad_utils import nv_load_excel

nv_down_excel()
time.sleep(2)
nv_load_excel()
