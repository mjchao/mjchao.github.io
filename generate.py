"""Generates index.html, about.html, skills.html, projects.html and all the
skills and projects subpages.
"""
import json
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

SKILLS_HTML = os.path.join(CURDIR, "skills.html")
SKILLS_TEMPLATE = os.path.join(TEMPLATES_DIR, "skills.template.html")
SKILL_PAGE_TEMPLATE = os.path.join(TEMPLATES_DIR, "skill.template.html")
SKILLS_DIR = os.path.join(CURDIR, "skills")

global_vars = {}

def ReadFile(filename):
    with open(filename, "r") as f:
        return f.read().decode("utf-8")

def WriteFile(filename, content):
    with open(filename, "w") as f:
        f.write(content.encode("utf-8"))

def FillTemplate(template_text, vars):
    filled_template = template_text
    for k in vars:
        filled_template = filled_template.replace(
                "{{%s}}" %(k), "%s" %(vars[k]))
    return filled_template

def ReadVarsFile(filename):
    with open(filename) as f:
        return json.load(f)

def ConcatVars(*vars):
    concated_vars = {}
    for v in vars:
        concated_vars.update(v)
    return concated_vars

# ===== Load Nav HTML ==== #
with open(NAV_HTML, "r") as f:
    nav_html = f.read().decode("utf-8")

global_vars["NAV"] = nav_html

# ====== Generate index.html ===== #
index_template = ReadFile(INDEX_TEMPLATE)
index_vars = ConcatVars(global_vars)
index_html = FillTemplate(index_template, index_vars)
WriteFile(INDEX_HTML, index_html)

# ===== Generate about.html ====== #
about_template = ReadFile(ABOUT_TEMPLATE)
about_vars = ConcatVars(global_vars)
about_html = FillTemplate(about_template, about_vars)
WriteFile(ABOUT_HTML, about_html)

# ==== Generate skills pages and skills.html  ===== #

"""
# determine all the skills that need their individual pages generated.
skill_dirs = set()
for x in os.walk(SKILLS_DIR):
    subdir = x[0]
    # ignore the working directory
    if subdir == SKILLS_DIR:
        continue
    if subdir.startswith("./"):
        subdir = subdir[2:]
    skill_dirs.add(subdir)

# generate individual skill pages
skill_page_template = ReadFile(SKILL_PAGE_TEMPLATE)
for skill_dir in skill_dirs:
    vars = ReadVarsFile(os.path.join(skill_dir, "vars.json"))
    vars["CONTENT"] = ReadFile(os.path.join(skill_dir, "content.html"))
    skill_page_vars = ConcatVars(global_vars, vars)
    skill_page_html = FillTemplate(skill_page_template, skill_page_vars)
    WriteFile("%s.html" %(skill_dir), skill_page_html)

# link the individual skill pages to skills.html which lists all the individual
# skills
skills_template = ReadFile(SKILLS_TEMPLATE)
skills_vars = ConcatVars(global_vars)
skills_html = FillTemplate(skills_template, skills_vars)
WriteFile(SKILLS_HTML, skills_html)
"""
skills_template = ReadFile(SKILLS_TEMPLATE)
skills_vars = ConcatVars(global_vars)
skills_html = FillTemplate(skills_template, skills_vars)
WriteFile(SKILLS_HTML, skills_html)

