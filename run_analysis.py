import json, os, datetime
result = {'timestamp': str(datetime.datetime.now()), 'status': 'ok'}
with open('analysis_result.json', 'w') as f:
    json.dump(result, f)
print('Done.')
