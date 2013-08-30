<%inherit file="_templates/site.mako" />
<table>
% for photo in photos:
  <tr><td><a href="${photo}.html">
    <img src="/img/${photo}" height="175"></a></td></tr>
% endfor
</table>
