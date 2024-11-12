import requests 
def main():
    githubtoken =str(input("github token: "))
    owner =str(input("Owner: "))
    repo = str(input("Repo: "))
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    headers = {"Authorization": f"token {githubtoken}"}
    
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        commits = response.json()[0]
        if commits:
            print(f"Commit: {commits['commit']['message']}")
        else:
            print("nothing")
    else:
        print(f"Error fetching commits: {response.status_code}")

main()