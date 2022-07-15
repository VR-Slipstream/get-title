import subprocess as sp, requests, argparse, re

parser = argparse.ArgumentParser(description="RegEx Help")
parser.add_argument("-url", type=str, help="target URL", required=True)

b = parser.parse_args()

if "https://" in b.url or "http://" in b.url:
    html = requests.get(b.url, timeout=10).text
    title = re.findall(r"\<title\>(.*?)<\/title\>", html)
    print(title[0])

else:
    print("Wrong Input. Look for -h/--help")
