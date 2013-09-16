<%inherit file="_templates/site.mako" />
<table>
% for photo in photos:
  <tr><td><a href="${photo.get_name()}.html">
    <img src="/img/${photo.get_name()}" height="175"></a></td></tr>
% endfor
</table>
