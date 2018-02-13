import os
import json

ROOT = "/"
CURDIR = os.path.join(ROOT, "blog")
BLOG_POST_TEMPLATE = "post.template"
BLOG_SUMMARY_TEMPLATE = "summary.template"

with open(BLOG_POST_TEMPLATE, "r") as f:
    post_template = f.read()

with open(BLOG_SUMMARY_TEMPLATE, "r") as f:
    summary_template = f.read()

for x in os.walk("."):
    subdir = x[0]
    # ignore current dir
    if subdir == ".":
        continue
    if subdir.startswith("./"):
        subdir = subdir[2:]

    with open("%s/vars.json" %(subdir)) as f:
        vars = json.load(f)

    # provide DIR variable by default, which is the directory in which the
    # blog data was stored.
    vars["BLOGDIR"] = os.path.join(CURDIR, subdir)

    # generate the blog summary
    summary_html = summary_template
    for k in vars:
        summary_html = summary_html.replace("{{%s}}" %(k), "%s" %(vars[k]))
    with open("%s.summary.html" %(subdir), "w") as f:
        f.write(summary_html)

    # generate the blog content
    post_html = post_template
    for k in vars:
        post_html = post_html.replace("{{%s}}" %(k), "%s" %(vars[k]))
    with open("%s.html" %(subdir), "w") as f:
        f.write(post_html)

