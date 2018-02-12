import os
import json

with open("template.html", "r") as f:
    template_contents = f.read()

for x in os.walk("."):
    subdir = x[0]
    # ignore current dir
    if subdir == ".":
        continue
    if subdir.startswith("./"):
        subdir = subdir[2:]

    with open("%s/vars.json" %(subdir)) as f:
        vars = json.load(f)

    with open("%s.html" %(subdir), "w") as f:
        contents = template_contents.replace("{{CONTENTDIR}}", subdir)
        for k in vars:
            contents = contents.replace("{{%s}}" %(k), "%s" %(vars[k]))
        f.write(contents)


