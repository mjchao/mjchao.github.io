from content_generator import ContentGenerator
import os


class BlogGenerator(ContentGenerator):
    """Adds special logic to generate related-posts sections and nav for blog
    posts.
    """

    CATEGORIES_VAR = "CATEGORIES"
    RELATED_POSTS_VAR = "RELATED"

    def __init__(self, root_dir, topic_dir, overview_template, summary_template,
            content_template, nav_template, additional_vars={}):
        super(BlogGenerator, self).__init__(root_dir, topic_dir,
            overview_template, summary_template, content_template,
            additional_vars)

        # generate categories and article links in nav.
        topic_vars = ContentGenerator.ReadVarsFile(os.path.join(self._topic_dir,
            ContentGenerator.VAR_FILENAME))
        categories = topic_vars[BlogGenerator.CATEGORIES_VAR]

        categories_html = ""
        for category, articles in categories:
            articles_html = ""
            for article in articles:
                title = ContentGenerator.ReadVarsFile(os.path.join(
                    self._topic_dir, article,
                    ContentGenerator.VAR_FILENAME))["title"]
                articles_html += (
"""
  <div class="blog-nav-article">
    <a href="/blog/%s.html" class="blog-nav-article-link">
      %s
    </a>
  </div>

"""
                %(article, title))
            category_html = (
"""
<div class="blog-nav-category">
%s
</div>

"""
                %(articles_html))
            categories_html += category_html

        # overwrite the nav variable for a blog-specific nav.
        self._content_nav = ContentGenerator.FillTemplate(nav_template,
            {"CATEGORIES": categories_html})


    def EditContentVars(self, content_vars, content_name):
        content_vars["NAV"] = self._content_nav
        if BlogGenerator.RELATED_POSTS_VAR in content_vars:
            related_posts = content_vars[BlogGenerator.RELATED_POSTS_VAR]
            if type(related_posts) is not list:
                raise ValueError(
                    "%s variable for content \"%s\" is of the wrong type. "
                    "It needs to be a list of related post names."
                    %(BlogGenerator.RELATED_POSTS_VAR, content_name))
            related_posts_html = ""
            for related in related_posts:
                related_dir = os.path.join(self._root_dir, self._topic_dir,
                    related)
                if not os.path.exists(related_dir):
                    raise ValueError("%s is not a valid related post. The "
                        "directory \"%s\" does not exist"
                        %(related, related_dir))
                related_vars_file = os.path.join(related_dir,
                    ContentGenerator.VAR_FILENAME)
                related_vars = ContentGenerator.ReadVarsFile(related_vars_file)
                related_vars[ContentGenerator.CONTENT_DIR_VAR] = related
                related_vars[ContentGenerator.TOPIC_DIR_VAR] = self._topic_dir
                related_vars[ContentGenerator.ROOT_DIR_VAR] = self._root_dir
                related_summary = ContentGenerator.FillTemplate(
                    self._summary_template, related_vars)
                related_posts_html += related_summary + "\n"
            content_vars[BlogGenerator.RELATED_POSTS_VAR] = related_posts_html

