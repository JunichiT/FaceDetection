#!/usr/bin/env python

for line in open('~/Desktop/smile_tmp/score.txt', 'r'):
    scoreList = line[:-1].split('\n')

average = sum(scoreList)/len(scoreList)

req_str = 'http://pom.l-u-l.tk/api' + average #合ってなさそう
req = urllib2.Request(req_str)
