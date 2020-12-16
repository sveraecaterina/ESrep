import tweepy, time, urllib

#Authenticate to Twitter
auth = tweepy.OAuthHandler("<apikey>", "<apisecretkey>")
auth.set_access_token("<access token>", "<accesstokensecret>")

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

#Access file with randomized lyrics
filename=open('lyrics.txt','r')
f=filename.readlines()
f = [j for j in f if j != '\n']
filename.close()

#Tweet a line every hour
for line in file:
     api.update_status(line)
     print(line)
     time.sleep(3600) #Sleep for 1 hour

#Initial testing of connection and keys
try: 
    api.verify_credentials()
    print("Authentication OK") 
except:
    print("Error during authentication")
