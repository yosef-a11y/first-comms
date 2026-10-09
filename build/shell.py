"""Shared shell pulled live out of index.html so the sub-pages cannot drift."""
import re, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = open(os.path.join(ROOT, 'index.html')).read()

def between(start, end, s=None):
    s = s or SRC
    i = s.index(start); j = s.index(end, i)
    return s[i:j]

SPRITE  = between('<svg width="0" height="0"', '<header class="header"').rstrip()
HEADER  = between('<header class="header"', '</header>') + '</header>'
FOOTER  = between('<footer class="footer"', '</footer>') + '</footer>'
# form: from the form-card div through its closing </div> (line after </form>)
i = SRC.index('      <div class="form-card" id="lead-form">')
j = SRC.index('</form>', i) + len('</form>')
j = SRC.index('</div>', j) + len('</div>')
FORM = SRC[i:j]

# the loader AND the config block that follows it — two <script> tags
_g = SRC.index('<script async src="https://www.googletagmanager.com/gtag/js')
_g2 = SRC.index('</script>', SRC.index('</script>', _g) + 1) + len('</script>')
GTAG    = SRC[_g:_g2]
WC      = between('<script>var $wc_load', '</script>\n</head>') + '</script>'
JSCLASS = '<script>document.documentElement.className += " js";</script>'
ICON    = between('<link rel="icon"', '>\n') + '>'
CALLBAR = between('<div class="callbar">', '</div>') + '</div>'
k = SRC.rindex('<script>')
TAIL    = SRC[k:SRC.index('</script>', k)] + '</script>'

def nav_rooted(html):
    """Sub-pages live in a directory, so in-page anchors must point at the root."""
    html = html.replace('href="#top"', 'href="/"')
    for frag in ['basics', 'rf-testing', 'services', 'why', 'faq']:
        html = html.replace(f'href="#{frag}"', f'href="/#{frag}"')
    return html.replace('href="privacy.html"', 'href="/privacy.html"')

HEADER_SUB = nav_rooted(HEADER)
FOOTER_SUB = nav_rooted(FOOTER)
