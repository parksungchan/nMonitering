import datetime, os
import crolling as crolling
from common import crolling_util as crolling_util

logPath = 'logKey'
sIdx = 1
eIdx = 2

if __name__=='__main__':
    now = datetime.datetime.now()
    nowStr = str(now).replace('-', '').replace(' ', '_').replace(':', '').replace('.', '_')
    file_path = os.path.dirname(os.path.abspath(__file__))
    dirlist = sorted(os.listdir(file_path), reverse=True)
    crolling_util.make_dir(file_path + '/' + logPath)
    now = datetime.datetime.now()
    nowStr = str(now).replace('-', '').replace(' ', '_').replace(':', '').replace('.', '_')
    # searchArr = []
    crolling_util.printS('Start:' + nowStr)


    findKeyArr = crolling.BW_CP1
    crolling_util.get_rank_multi(sIdx, eIdx, findKeyArr, itemKeyArr=None, logPath='logKey')


    crolling_util.printS('')
    end = datetime.datetime.now()
    endStr = str(end).replace('-', '').replace(' ', '_').replace(':', '').replace('.', '_')
    crolling_util.printS('End:' + endStr)
    crolling_util.printS('Sub:' + str(end - now))

    print('#################################################################################################')
    print('#################################################################################################')
    print('#################################################################################################')
    for search in crolling.searchArr:
        print(search)