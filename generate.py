"""Generates index.html, about.html, skills.html, projects.html and all the
skills and projects subpages.
"""
import os

# ========= File paths ======= #
ROOT = "."
CURDIR = ROOT
TEMPLATES_DIR = os.path.join(ROOT, "templates")


NAV_HTML = os.path.join(ROOT, "nav.html")

INDEX_HTML = os.path.join(CURDIR, "index.html")
INDEX_TEMPLATE = os.path.join(TEMPLATES_DIR, "index.template.html")

ABOUT_HTML = os.path.join(CURDIR, "about.html")
ABOUT_TEMPLATE = os.path.join(TEMPLATES_DIR, "about.template.html")

# ===== Load Nav HTML ==== #
with open(NAV_HTML, "r") as f:
    nav_html = f.read().decode("utf-8")

def InsertNavIntoTemplate(template_text):
    return template_text.replace("{{NAV}}", nav_html)

# ====== Generate index.html ===== #
with open(INDEX_TEMPLATE, "r") as f:
    index_template = f.read().decode("utf-8")

# convert index template into actual index.html
index_html = InsertNavIntoTemplate(index_template)

# write index.html
with open(INDEX_HTML, "w") as f:
    f.write(index_html)

# ===== Generate about.html ====== #
with open(ABOUT_TEMPLATE, "r") as f:
    about_template = f.read().decode("utf-8")

# convert nav template into actual nav.html
about_html = InsertNavIntoTemplate(about_template)

# write about.html
with open(ABOUT_HTML, "w") as f:
    f.write(about_html)

