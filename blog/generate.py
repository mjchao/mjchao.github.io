import os
import json

ROOT = "/"
CURDIR = os.path.join(ROOT, "blog")
BLOG_POST_TEMPLATE = "post.template"
BLOG_SUMMARY_TEMPLATE = "summary.template"
RELATED_POSTS_VAR = "RELATED"

with open(BLOG_POST_TEMPLATE, "r") as f:
    post_template = f.read()

with open(BLOG_SUMMARY_TEMPLATE, "r") as f:
    summary_template = f.read()

blogdirs = set()
for x in os.walk("."):
    subdir = x[0]
    # ignore current dir
    if subdir == ".":
        continue
    if subdir.startswith("./"):
        subdir = subdir[2:]

    blogdirs.add(subdir)

for blogdir in blogdirs:
    with open("%s/vars.json" %(blogdir)) as f:
        vars = json.load(f)

    # provide DIR variable by default, which is the directory in which the
    # blog data was stored.
    vars["BLOGDIR"] = os.path.join(CURDIR, blogdir)

    # Prevent substiting {{RELATED}} directly as a list. We want to
    # substitute in the actual summaries, so that requires some special logic
    # later.
    if RELATED_POSTS_VAR in vars:
        related_posts = vars[RELATED_POSTS_VAR]
        del vars[RELATED_POSTS_VAR]
    else:
        related_posts = []

    # generate the blog summary
    summary_html = summary_template
    for k in vars:
        summary_html = summary_html.replace("{{%s}}" %(k), "%s" %(vars[k]))

    with open("%s.summary.html" %(blogdir), "w") as f:
        f.write(summary_html)

    # generate the blog content
    post_html = post_template
    for k in vars:
        post_html = post_html.replace("{{%s}}" %(k), "%s" %(vars[k]))

    # add summaries of related posts to the bottom of the blog post
    related_posts_html = ""
    for related in related_posts:
        if related not in blogdirs:
            print ("ERR: %s in %s.RELATED is not a valid post. Ignoring..."
                    %(related, blogdir))
            continue
        related_posts_html += (
                "<div w3-include-html=\"%s.summary.html\"></div>\n"
                %(os.path.join(CURDIR, related)))
    post_html = post_html.replace("{{%s}}" %(RELATED_POSTS_VAR),
            related_posts_html)

    with open("%s.html" %(blogdir), "w") as f:
        f.write(post_html)

