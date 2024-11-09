import tweepy


#get twitter api and access to account
def main():
    try:
        consumer =str(input("Consumer Key here: "))
        secret =str(input("Consumer Secret here: "))
        token = str(input("Access Token here: "))
        sectettoken =str(input("Secret Access Token here: "))

    except:
        print("Invalid input")

    client = tweepy.Client(
        consumer_key= consumer,consumer_secret= secret, access_token = token, access_token_secret = sectettoken
        
    )
    tweet = input("send a tweet")
    response = client.create_tweet( text = tweet)

#check commits of a specific project 

#tweet those commit messages 
main()
