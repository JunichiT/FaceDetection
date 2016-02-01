#!/usr/bin/env python
import time

for line in open('~/Desktop/smile_tmp/score.txt', 'r'):
    scoreList = line[:-1].split('\n')

average = sum(scoreList)/len(scoreList)

## yyyy/mm/dd format
date_in_format = time.strftime("%Y/%m/%d"))
project_num = 1 # dummy
req_url = 'http://pom.l-u-l.tk/api/photo_score'
req.add_header('Content-Type', 'application/json')

data = {
date: date_in_format
project_id: project_num
value: average
}

response = requests.post(req_url, data=json.dumps(data), headers=headers)
