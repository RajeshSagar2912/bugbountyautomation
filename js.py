import requests
import waybackurls
import gau

# Take the domain input from the user
domain = input("Enter the domain: ")

# Get all the URLs for this domain using waybackurls and gau
urls = waybackurls.waybackurls(domain).urls()
urls.extend(gau.gau(domain))

# Write the URLs to urls.txt
with open("urls.txt", "w") as f:
    for url in urls:
        f.write(url + "\n")

# Sort all the URLs having JavaScript files extension .js from urls.txt
js_urls = [url for url in urls if url.endswith(".js")]

# Write the JavaScript URLs to js.txt
with open("js.txt", "w") as f:
    for url in js_urls:
        f.write(url + "\n")

# Filter .js files using "httpx -content-type | grep 'application/javascript'" and save them in js.txt
filtered_js_urls = []
for url in js_urls:
    headers = {"Content-Type": "application/javascript"}
    r = requests.get(url, headers=headers)
    if r.headers["Content-Type"] == "application/javascript":
        filtered_js_urls.append(url)

# Write the filtered JavaScript URLs to js.txt
with open("js.txt", "w") as f:
    for url in filtered_js_urls:
        f.write(url + "\n")

# Do nuclei template scan
!nuclei -t templates/api-keys.yaml -l js.txt
