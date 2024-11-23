#Pull request info of a git repo

import requests

response = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")

completedetail = response.json()

pr_creators = {}

for i in range(len(completedetail)):
    creater = completedetail[i]["user"]["login"]

    if creater in pr_creators:
        pr_creators[creater] += 1
    else:
        pr_creators[creater] = 1

print("PR Creators and Counts:")

for creator,count in pr_creators.items():
    print(f"{creator}: {count} PR(s)")