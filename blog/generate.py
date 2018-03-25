import collections
import os
import json

# ========== File paths that may change ========= #
ROOT = "/"
CURDIR = os.path.join(ROOT, "blog")
BLOG_POST_TEMPLATE = "post.template"
BLOG_SUMMARY_TEMPLATE = "summary.template"
RELATED_POSTS_VAR = "RELATED"

NAV_TOC_LIST ="nav-toc.csv"
NAV_TEMPLATE = "nav.template"
NAV_HTML = "nav.html"
# ============================================================================ #


# ========== Generate table of contents in nav ========== #
with open(NAV_TEMPLATE, "r") as f:
    nav_template = f.read().decode("utf-8")

category_to_blogdir = collections.defaultdict(list)
with open(NAV_TOC_LIST, "r") as f:
    for entry in f:
        values = entry.rstrip("\n").split(",")
        if len(values) != 2:
            raise ValueError("Error parsing nav table of contents. " +
                    "Expecting two values <blog dir> and <category> " +
                    "but received %d values in entry \"%s\""
                    %(len(values), entry))
        blogdir = values[0]
        category = values[1]
        category_to_blogdir[category].append(blogdir)

nav_html = nav_template
for category in category_to_blogdir:
    category_html = ""

    for blogdir in category_to_blogdir[category]:
        with open(os.path.join(blogdir, "vars.json")) as f:
            vars = json.load(f)
        category_html += (
"""
<div>
  <a href="%s.html" class="post-link">
    %s
  </a>
</div>
"""
        %(blogdir, vars["title"]))
    nav_html = nav_html.replace("{{%s}}" %(category), category_html)

with open(NAV_HTML, "w") as f:
    f.write(nav_html.encode("utf-8"))
# ============================================================================ #

# ========== Generate blog post html files ========== #
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
    with open(os.path.join(blogdir, "vars.json")) as f:
        vars = json.load(f)

    # provide BLOGDIR and BLOGPOST variable by default, which is the directory
    # and blogpost
    vars["BLOGDIR"] = os.path.join(CURDIR, blogdir)
    with open(os.path.join(blogdir, "content.html"), "r") as f:
        vars["BLOGPOST"] = f.read().decode("utf-8")

    # provide NAV as well
    with open("nav.html", "r") as f:
        vars["NAV"]  = f.read().decode("utf-8")

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

    if related_posts:
        # add summaries of related posts to the bottom of the blog post
        related_posts_html = "<h2 class=\"related-header\">Related</h2>\n"
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
    else:
        post_html = post_html.replace("{{%s}}" %(RELATED_POSTS_VAR), "")

    with open("%s.html" %(blogdir), "w") as f:
        f.write(post_html.encode("utf-8"))
# ============================================================================ #

