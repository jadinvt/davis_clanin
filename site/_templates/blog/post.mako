<%page args="post"/>

<% 
   category_links = []
   for category in post.categories:
       if post.draft:
           #For drafts, we don't write to the category dirs, so just write the categories as text
           category_links.append(category.name)
       else:
           category_links.append("<a href='%s'>%s</a>" % (category.path, category.name))
%>

<article>
  <div class="blog_post">
    <header>
      <div id="${post.slug}"></div>
      <h2 class="blog_post_title"><a href="${post.permapath()}" rel="bookmark" title="Permanent Link to ${post.title}">${post.title}</a></h2>
      <p><small>
      % if post.previous:
        <a href="${post.previous.path}" class="previous"><< ${post.previous.date.strftime("%B %d")}</a>
      % endif
      <span class="blog_post_date">${post.date.strftime("%B %d, %Y at %I:%M %p")}</span> 
      % if post.next:
        <a href="${post.next.path}" class="next">${post.next.date.strftime("%B %d")} >></a>
      % endif  
      </small></p>
    </header>
    <hr/>
    <div class="post_prose">
      ${self.post_prose(post)}
    </div>
    <div class="prev_next">
      % if post.previous:
        <a href="${post.previous.path}" class="previous"><< ${post.previous.date.strftime("%B %d, %Y")}</a>
      % endif
      % if post.next:
         <a href="${post.next.path}" class="next">${post.next.date.strftime("%B %d, %Y")} >></a>
      % endif  
    </div>

    % if bf.config.blog.disqus.enabled:
       <div id="disqus_thread"></div>
       <script type="text/javascript">
       /* * * CONFIGURATION VARIABLES: EDIT BEFORE PASTING INTO YOUR WEBPAGE * * */
       var disqus_shortname = 'davisclanin'; // required: replace example with your forum shortname

       /* * * DON'T EDIT BELOW THIS LINE * * */
       (function() {
          var dsq = document.createElement('script'); dsq.type = 'text/javascript'; dsq.async = true;
          dsq.src = '//' + disqus_shortname + '.disqus.com/embed.js';
          (document.getElementsByTagName('head')[0] || document.getElementsByTagName('body')[0]).appendChild(dsq);
          })();
      </script>
      <noscript>Please enable JavaScript to view the <a href="http://disqus.com/?ref_noscript">comments powered by Disqus.</a></noscript>
      <a href="http://disqus.com" class="dsq-brlink">comments powered by <span class="logo-disqus">Disqus</span></a>
    % endif
    
   </div>
</article>

<%def name="post_prose(post)">
${post.content}
</%def>
