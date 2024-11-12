import tweepy
import requests 
import time

def auth():
    try:
        consumer =str(input("Consumer Key here: "))
        secret =str(input("Consumer Secret here: "))
        token = str(input("Access Token here: "))
        sectettoken =str(input("Secret Access Token here: "))
    
    
        client = tweepy.Client(
            consumer_key= consumer,consumer_secret= secret, access_token = token, access_token_secret = sectettoken
        
     )
    except:
        print("Invalid input")
        return None
