from facepp import *
import time, sys, json
from pprint import pformat

# encode to UTF-8
def encode(obj):
    if type(obj) is unicode:
        return obj.encode('utf-8')
    if type(obj) is dict:
        return {encode(k): encode(v) for (k, v) in obj.iteritems()}
    if type(obj) is list:
        return [encode(i) for i in obj]
    return obj

# function that print whole json data with proper indent
def print_result(result):
    result = encode(result)
    print '\n'.join(['  ' + i for i in pformat(result, width = 75).split('\n')])

# find smiling rate value from json
def findSmilingRate(obj):
    faces = obj['face']
    smileValues = []
    for face in faces:
	    attribute  = face['attribute']
            smiling = attribute['smiling']
            #print_result(smiling['value'])
	    smileValues.append(smiling['value'])
    return smileValues

# judge how the detected person is smiling, from smiling rate
def judge(rate):
    if rate >= 60:
        return 'Smiling'
    else:
        return 'Not Smiling'
    
# My api key and secret
key = 'e1d9111d1021ecdc58805f48310256c3'
secret = 'AUc39DCH4CP0hPrm54ZQo22HWpO_6aSJ'

# Deprecated key/secret
#key = '809f6680f12e0dfa67d4f4cc480e62c9'
#secret = 'Gl0di5A7B-0nK0HkMgo8znCdgLHaCB2O'

# set api conf
api = API(key,secret)

# get result from server
# get image path from command line
imagePath = sys.argv[1]
jsonData = api.detection.detect(img=File(imagePath))

#print_result(jsonData)

smilingRates = findSmilingRate(jsonData)

for rate in smilingRates:
	#print judge(rate)
	"""Suit the value range 0...1"""
	print rate/100

#print_result(jsonData)

#print 'end'

