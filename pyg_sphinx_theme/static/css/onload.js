$(document).ready(function() {
  // Remove "Build with Sphinx" text in the footer:
  var elem = $("footer div[role='contentinfo']").get(0);
  while (elem.nextSibling)
    elem.nextSibling.remove();

  // Copy text in code blocks:
  var $highlight = $("div.rst-content div.highlight");
  $highlight.append("<span class='copy fa fa-clipboard' title='Copy to clipboard'/>");
  $highlight.click(function() {
    navigator.clipboard.writeText($(this).parent().text().slice(0, -2));
  });
});
