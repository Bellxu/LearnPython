import requests 
# 执行API调用并存储响应
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url) 
print("Status code:",r.status_code) 
# 将API响应存储在一个变量中
response_dict = r.json() 
print("Total Repositoriest:",response_dict['total_count'])

repo_dicts = response_dict['items']
print("Repositorires returned:",len(repo_dicts))
#watch watch第一个仓库
fisrt_repo_dict = repo_dicts[0]
print("\nKeys:",len(fisrt_repo_dict))
for key in sorted(fisrt_repo_dict.keys()):
    print(key)