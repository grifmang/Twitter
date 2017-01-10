import tweepy

def get_tag():
	hashtag = ''
	tag = raw_input('Enter a hashtag to search: ')
	for letter in tag:
		if not letter.isalpha():
			continue
		else:
			hashtag += letter
	return hashtag
	
def twitter():
	consumer_key = ''
	consumer_secret = ''
	access_token = ''
	access_secret = ''
	
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_secret)
	api = tweepy.API(auth)
	
	file = open('Twitteroutput.txt', 'r+')
	
	count = 1
	
	tag = get_tag()
	tags = ''
	
	for tweet in tweepy.Cursor(api.search, q=tag).items():
		file.write('-----------------Start Tweet #' + str(count) + '-----------------\n')
		file.write('Name: ' + tweet.author.name.encode('utf-8') + '\n')
		file.write('Screen Name: ' + tweet.author.screen_name.encode('utf-8') + '\n')
		file.write('Created: ' + str(tweet.created_at) + '\n')
		file.write('Tweet: ' + tweet.text.encode('utf-8') + '\n')
		file.write('-----------------End Tweet #' + str(count) + '-----------------\n')
		file.write('\n')
		count += 1
		
	file.close()

	
twitter()
