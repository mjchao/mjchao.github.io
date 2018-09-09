import json
import os


class ContentGenerator(object):
    """Generates content and summaries from templates.

    The expected layout is
       <root directory>
       |
       ---- topic #1 (e.g. skills)
              |
              --------- vars.json
              |
              --------- content #1 (e.g. c++)
                            |
                            -------- vars.json
                            -------- content.html
              |
              --------- content #2 (e.g. java)
                            |
                            -------- vars.json
                            -------- content.html
              --------- content #3
                            |
                            -------- vars.json
                            -------- content.html

                    ...

       |
       ---- topic #2 (e.g. projects)
              |
              --------- vars.json
              |
              --------- content #1
                           |
                            -------- vars.json
                            -------- content.html
              --------- content #2
                           |
                            -------- vars.json
                            -------- content.html
              --------- content #3
                           |
                            -------- vars.json
                            -------- content.html

                    ...

       |
       ----- subsequent topics... (e.g. blog)

    One content generator should be assigned to one topic. For that topic,
    the content generator will create an overview page <root>/<topic>.html
    containing summaries that summarize and link to the topic's content pages.
    The generator will create content pages <root>/<topic>/<summary>.html
    containing the specific details.

    When creating a content or summary template, here are variables the content
    generator will automatically provide:
        * {{ROOT_DIR}} - path to root dir, as passed to the ContentGenerator
                         constructor
        * {{TOPIC_DIR}} - relative path of topic dir from root dir
        * {{CONTENT_DIR}} - relative path of content dir from topic dir
        * {{CONTENT}} - contents of content.html that will be pasted into
                        the content template.
    Any additional variables should be defined in your <content>/vars.json

    When creating an overview template, here are variables the content generator
    will automatically provide:
        * {{SUMMARIES}} - html of the summaries to be displayed on the overview
                          page.

    All <topic>/vars.json files are expected to have a CONTENT_ORDERING list
    that specifies how the summaries of the content pages should be ordered. If
    a content page is left out of that list, then its summary will not appear.
    """
    ROOT_DIR_VAR = "ROOT_DIR"
    VAR_FILENAME = "vars.json"

    TOPIC_DIR_VAR = "TOPIC_DIR"
    SUMMARIES_VAR = "SUMMARIES"

    CONTENT_DIR_VAR = "CONTENT_DIR"
    CONTENT_FILENAME = "content.html"
    CONTENT_VAR = "CONTENT"
    CONTENT_ORDERING_VAR = "CONTENT_ORDERING"

    def __init__(self, root_dir, topic_dir, overview_template, summary_template,
            content_template, additional_vars={}):
        """Creates a content generator.

        Args:
            root_dir: (string) Absolute or relative path to the root dir.
            topic_dir: string) Relative path to the topic dir from the root dir.
            overview_template: (string) The html template for overviews. This
                should be HTML for an entire page.
            summary_template: (string) The html template for summaries. This
                should be HTML for a single div that is pasted in the overview
                page.
            content_template: (string) The html template for content pages.
                This should be HTML for an entire page.
            additional_vars: (dict) Any additional variables that the
                ContentGenerator should add.
        """
        self._root_dir = root_dir
        self._topic_dir = topic_dir
        self._overview_template = overview_template
        self._summary_template = summary_template
        self._content_template = content_template
        self._additional_vars = additional_vars

    @staticmethod
    def ReadFile(filename):
        with open(filename, "r") as f:
            return f.read().decode("utf-8")

    @staticmethod
    def WriteFile(filename, content):
        with open(filename, "w") as f:
            f.write(content.encode("utf-8"))

    @staticmethod
    def FillTemplate(template_text, vars):
        """Fills in a template by replacing all {{VAR}} with the actual value
        of VAR.

        Args:
            template_text: (string) A tempalte with some {{VAR}}s left in it.
            vars: (dict) Maps VARs to values.

        Returns:
            (string) The template with all its {{VAR}}s filled in.
        """
        filled_template = template_text
        for k in vars:
            filled_template = filled_template.replace(
                    "{{%s}}" %(k), "%s" %(vars[k]))
        return filled_template

    @staticmethod
    def ReadVarsFile(filename):
        """Reads a json file with variables defined in it.
        """
        with open(filename) as f:
            return json.load(f)

    @staticmethod
    def ConcatVars(*vars):
        """Concatenates a list of variable dicts into a single variable dict.

        If there are duplicate variables across the dictionaries, the last
        definition is used.
        """
        concated_vars = {}
        for v in vars:
            concated_vars.update(v)
        return concated_vars

    def GetRootDir(self):
        return self._root_dir

    def GetTopicDir(self):
        return self._topic_dir

    def GetContentTemplate(self):
        return self._content_template

    def GetSummaryTemplate(self):
        return self._summary_template

    def DiscoverContentDirs(self):
        """Determines all the content pages that need to be generated. The
        returned directories are all relative from the topic dir.

        The assumption is that all directories in the topic dir must be
        content dirs. Override this function if that's not the case.
        """
        content_dirs = set()
        for x in os.listdir(self._topic_dir):
            if os.path.isdir(os.path.join(self._topic_dir, x)):
                content_dirs.add(x)
        return content_dirs

    def EditContentVars(self, conent_vars, content_dir):
        """Edits any variables before generating the content.

        Args:
            content_vars: (dict) The current content variables
            content_dir: (string) The directory containing the content data.
        """
        pass

    def Generate(self):
        """Generates all content pages, summaries, and the overview page.
        """
        # Maps the content name to the html for its summary div
        summary_htmls = {}

        content_dirs = self.DiscoverContentDirs()
        for d in content_dirs:
            content_dir = os.path.join(self._root_dir, self._topic_dir, d)
            vars_file = os.path.join(content_dir, ContentGenerator.VAR_FILENAME)
            vars = ContentGenerator.ReadVarsFile(vars_file)

            # load in predefined {{CONTENT_DIR}}, {{TOPIC_DIR}}, and
            # {{ROOT_DIR}}
            vars[ContentGenerator.CONTENT_DIR_VAR] = d
            vars[ContentGenerator.TOPIC_DIR_VAR] = self._topic_dir
            vars[ContentGenerator.ROOT_DIR_VAR] = self._root_dir

            # load in {{CONTENT}} from the content.html file.
            content_file = os.path.join(content_dir,
                    ContentGenerator.CONTENT_FILENAME)
            vars[ContentGenerator.CONTENT_VAR] = ContentGenerator.ReadFile(
                    content_file)

            # Pass additional vars second so that the user is allowed to
            # override the variables that the content generator thinks should
            # be used.
            content_vars = ContentGenerator.ConcatVars(vars,
                    self._additional_vars)
            self.EditContentVars(content_vars, content_dir)

            # Create the content page
            content_html = ContentGenerator.FillTemplate(self._content_template,
                    content_vars)
            content_page = os.path.join(self._topic_dir, "%s.html" %(d))
            ContentGenerator.WriteFile(content_page, content_html)

            # Create the summary
            summary_html = ContentGenerator.FillTemplate(self._summary_template,
                    content_vars)
            summary_htmls[d] = summary_html

        # Generate the overview page
        topic_vars_file = os.path.join(self._root_dir, self._topic_dir,
                ContentGenerator.VAR_FILENAME)
        topic_vars = ContentGenerator.ReadVarsFile(topic_vars_file)
        if ContentGenerator.CONTENT_ORDERING_VAR not in topic_vars:
            raise ValueError(
                    "%s is not a valid topic var.json file. It is required to "
                    "define a %s variable that indicates the ordering in which "
                    "content summaries should appear." %(topic_vars_file,
                        ContentGenerator.CONTENT_ORDERING_VAR))
        content_summary_ordering = topic_vars[
                ContentGenerator.CONTENT_ORDERING_VAR]

        combined_summary_html = ""
        for content_name in content_summary_ordering:
            if content_name not in summary_htmls:
                raise ValueError(
                        "In the topic var.json file \"%s\", the content \"%s\" "
                        "does not exist. You must create a directory \"%s\" "
                        "for that content." %(topic_vars_file, content_name,
                            os.path.join(self._root_dir, self._topic_dir,
                                content_name)))
            combined_summary_html += (summary_htmls[content_name] + "\n")

        overview_vars = ContentGenerator.ConcatVars(
                topic_vars,
                {
                    ContentGenerator.SUMMARIES_VAR: combined_summary_html,
                    ContentGenerator.ROOT_DIR_VAR: self._root_dir,
                    ContentGenerator.TOPIC_DIR_VAR: self._topic_dir,},
                self._additional_vars
                )
        overview_html = ContentGenerator.FillTemplate(self._overview_template,
            overview_vars)
        overview_page = os.path.join(self._root_dir,
            "%s.html" %(self._topic_dir))
        ContentGenerator.WriteFile(overview_page, overview_html)

