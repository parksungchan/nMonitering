import datetime
import src.01_nv_key

start = datetime.datetime.now()
nv_down_excel()
time.sleep(2)
nv_load_excel()
print('[Start] ', start)
print('[Complete] ', datetime.datetime.now())
print('[Total] ', datetime.datetime.now() - start)