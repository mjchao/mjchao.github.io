"""Generates index.html, about.html, skills.html, projects.html and all the
skills and projects subpages.
"""
from content_generator import ContentGenerator
import os

# ========= File paths ======= #
ROOT = "."
TEMPLATES_DIR = os.path.join(ROOT, "templates")

NAV_HTML = os.path.join(ROOT, "nav.html")

INDEX_HTML = os.path.join(ROOT, "index.html")
INDEX_TEMPLATE = os.path.join(TEMPLATES_DIR, "index.template.html")

ABOUT_HTML = os.path.join(ROOT, "about.html")
ABOUT_TEMPLATE = os.path.join(TEMPLATES_DIR, "about.template.html")

SKILLS_DIR = os.path.join(ROOT, "skills")

PROJECTS_DIR = os.path.join(ROOT, "projects")

# ===== Load Nav HTML ==== #
global_vars = {}

nav_html = ContentGenerator.ReadFile(NAV_HTML)
global_vars["NAV"] = nav_html

# ====== Generate index.html ===== #
index_template = ContentGenerator.ReadFile(INDEX_TEMPLATE)
index_vars = ContentGenerator.ConcatVars(global_vars)
index_html = ContentGenerator.FillTemplate(index_template, index_vars)
ContentGenerator.WriteFile(INDEX_HTML, index_html)

# ===== Generate about.html ====== #
about_template = ContentGenerator.ReadFile(ABOUT_TEMPLATE)
about_vars = ContentGenerator.ConcatVars(global_vars)
about_html = ContentGenerator.FillTemplate(about_template, about_vars)
ContentGenerator.WriteFile(ABOUT_HTML, about_html)

# ===== Generate skills pages and skills.html  ===== #
skills_generator = ContentGenerator(
        ROOT,
        SKILLS_DIR,
        ContentGenerator.ReadFile(os.path.join(SKILLS_DIR, "overview.template")),
        ContentGenerator.ReadFile(os.path.join(SKILLS_DIR, "summary.template")),
        ContentGenerator.ReadFile(os.path.join(SKILLS_DIR, "content.template")),
        global_vars)
skills_generator.Generate()

# ===== Generate projects pages and projects.html ===== #
projects_generator = ContentGenerator(
        ROOT,
        PROJECTS_DIR,
        ContentGenerator.ReadFile(os.path.join(PROJECTS_DIR, "overview.template")),
        ContentGenerator.ReadFile(os.path.join(PROJECTS_DIR, "summary.template")),
        ContentGenerator.ReadFile(os.path.join(PROJECTS_DIR, "content.template")),
        global_vars)
projects_generator.Generate()

