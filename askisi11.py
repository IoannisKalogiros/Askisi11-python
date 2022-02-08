import math
from urllib.request import Request, urlopen

def entropy(string):

    prob = [ float(string.count(c)) / len(string) for c in dict.fromkeys(list(string)) ]

    entropy = - sum([ p * math.log(p) / math.log(2.0) for p in prob ])

    return entropy


# Οι γύροι είναι από 1607229 έως 1607248

text= ""

round = "1607249"
for  i in range (20):
    req = Request('https://drand.cloudflare.com/public/' + round, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
    round = int(round) - 1
    round = str (round)
    data = urlopen(req).read()
    text = text + str(data[31:95],"utf-8")
    


print ("H entropia einai ish me:",entropy(text))