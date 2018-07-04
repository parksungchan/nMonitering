import datetime
import crolling as crolling
import crolling_util as crolling_util

logKeyPath = 'logSum'

sIdx = 1
eIdx = 30
########################################################################################################################
# Main Function
########################################################################################################################
now = datetime.datetime.now()
nowStr = str(now).replace('-','').replace(' ','_').replace(':','').replace('.','_')
print('Start:'+nowStr)
print('')

findKeyJson = {}
for keyJson in crolling.keySum:
    if keyJson['id'] in findKeyJson:
        findKeyJson[keyJson['id']]['mid1'].append(keyJson['mid1'])
    else:
        findKeyJson[keyJson['id']] = {'key': keyJson['key'], 'mid1':[keyJson['mid1']]}
print('')

for fkey in findKeyJson:
    findKeyArr= findKeyJson[fkey]['key']
    itemKeyArr= findKeyJson[fkey]['mid1']
    crolling_util.get_rank_common(sIdx, eIdx, findKeyArr, itemKeyArr, logKeyPath)

print('')
end = datetime.datetime.now()
endStr = str(end).replace('-', '').replace(' ', '_').replace(':', '').replace('.', '_')
print('End:' + endStr)
print('Sub:' + str(end - now))

