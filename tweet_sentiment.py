import sys
import json

sentimentData = sys.argv[1] #AFIN-111.txt
twitterData = sys.argv[2] #output.txt

def create_twitter_Dict(data):
	dict=[]
	twitter_File = open(data)
	for line in twitter_File:
		dict.append(json.loads(line))
	return dict
	
def create_sentiment_Dict(data):
    afinnfile = open(data)
    scores = {} # initialize an empty dictionary
    for line in afinnfile:
        term, score  = line.split("\t")  
        scores[term] = int(score)  # Convert the score to an integer.
    return scores

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
    scores=create_sentiment_Dict(sentimentData)
    tweets=create_twitter_Dict(twitterData)
    for tweet in tweets:
    	if "text" in tweet:
	    	words=tweet["text"].split()
    		score=0
    		for word in words:
    			word=word.rstrip('"!.?@:;,')
    			word=word.replace("\n","")

    			if not (word.encode("utf-8",'ignore')==""):
    				if word.encode('utf-8') in scores.keys():
    					score=score+ int (scores[word])
    		print words, int (score)

if __name__ == '__main__':
    main()
