
import requests

res = requests.get("https://blog.csdn.net/dzhongjie/article/details/81152983")
print(res.text)
