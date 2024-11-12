import tweepy
import requests
import time

#get twitter api and access to account
def main():
    try:
        consumer =str(input("Consumer Key here: "))
        secret =str(input("Consumer Secret here: "))
        token = str(input("Access Token here: "))
        sectettoken =str(input("Secret Access Token here: "))

        client = tweepy.Client(
        consumer_key= consumer,consumer_secret= secret, access_token = token, access_token_secret = sectettoken, wait_on_rate_limit=True
        
        )
        

    except:
        print("Invalid input")
        main()

    githubtoken = str(input("GitHub token: "))
    owner = str(input("Owner: "))
    repo = str(input("Repo: "))
    latest_commit = ""

    while True:
        url = f"https://api.github.com/repos/{owner}/{repo}/commits"
        headers = {"Authorization": f"token {githubtoken}"}

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            commits = response.json()
            
            if commits:
                last_commit = f"Latest Commit: {commits[0]['commit']['message']}, Repo: https://github.com/{owner}/{repo}"
                
                if last_commit != latest_commit:
                    latest_commit = last_commit
                    response = client.create_tweet( text = last_commit)
                    print("tweeted")

                else:
                    print("didnt tweet")
                   
        time.sleep(10*60)
#check commits of a specific project 

#tweet those commit messages 
main()