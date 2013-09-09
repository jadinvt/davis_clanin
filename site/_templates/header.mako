<header>
  <div id="header" class="header_gradient theme_font">
    <h1>
      <a href="${bf.util.site_path_helper(trailing_slash=True)}">
        ${bf.config.blog.name}
      </a>
    </h1>
    <h2>${bf.config.blog.description}</h2>
  </div>
  <div id="navigation" class="grid_12">
    <%
    def nav_class(path):
       if path == "/":
          return "selected"
       else:
          return ""
    %>
    <%
    def blog_nav_class(path):
      render_path = bf.template_context.render_path
      if render_path.startswith(path) or render_path == path:
         return "selected"
      else:
         return ""
    %>
    <ul class="theme_font">
      <li>
        <% path = bf.util.site_path_helper(trailing_slash=True) %>
        <a href="${path}" class="${nav_class(path)}">Home</a>
      </li>
      <li>
        <%
          path = bf.util.site_path_helper(
                     bf.config.blog.path)
        %>
        <a href="${path}" class="${blog_nav_class(path)}">Journal</a>
      </li>

      <li>
        <%
          path = bf.util.site_path_helper(
                     bf.config.site.birth_story.path)
        %>
                 <a href="${path}" class="${blog_nav_class(path)}">Birth Story/FAQ</a>
        </li>
      
      <li>
        <%
          path = bf.util.site_path_helper(
                     bf.config.blog.path, "archive", trailing_slash=True)
        %>
        <a href="${path}" class="${nav_class(path)}">Archives</a>
      </li>


    </ul>

  </div>
</header>
