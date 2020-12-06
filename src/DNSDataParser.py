import json
import sys

MAX_LINES = 1000000

def convertForwardInput(file, recordType, out):
    lines = 0
    with open(file) as DNSFile:
        with open(out, 'w') as outFile:
            for line in DNSFile:
                lines += 1
                if lines > MAX_LINES:
                    break
                j = json.loads(line)
                if j['type'] != recordType:
                    continue
                kv = (j['name'], j['value'])
                outFile.write(kv[0] + ":" + kv[1] + "\n")

args = sys.argv[1:]
infile = args[0]
recordType = args[1]
outFile = args[2]
convertForwardInput(infile, recordType, outFile)