import os

WEBSITE_ROOT = "https://mjchao.github.io/"
html_urls = []
for root, dirs, files in os.walk("."):
    if root.startswith("./"):
        root = root[2:]
    if root.startswith("."):
        root = root[1:]

    for name in files:
        if name.endswith(".html"):
            if "content.html" not in name and "summary.html" not in name:
                html_urls.append(os.path.join(WEBSITE_ROOT, root, name))

with open("sitemap.txt", "w") as f:
    for url in html_urls:
        f.write(url + "\n")

