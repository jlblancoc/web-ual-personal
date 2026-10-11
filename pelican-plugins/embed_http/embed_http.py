# -*- coding: utf-8 -*-

# Copyright (c) 2016 Jose Luis Blanco
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.



from docutils import nodes
from docutils.parsers.rst import directives, Directive
import logging
import re
import urllib.error
import urllib.request

logger = logging.getLogger(__name__)


class EmbedHttp(Directive):
    """ Embed the HTML returned by a URL, fetched at build time.

    Usage:
    .. embedhttp:: URL
    """

    def align(argument):
        """Conversion function for the "align" option."""
        return directives.choice(argument, ('left', 'center', 'right'))

    required_arguments = 1
    optional_arguments = 2
    option_spec = {
        'width': directives.positive_int,
        'height': directives.positive_int,
        'align': align
    }

    final_argument_whitespace = False
    has_content = False

    def run(self):
        url = self.arguments[0].strip()
        logger.info("embedhttp: fetching %s", url)

        try:
            opener = urllib.request.build_opener(
                urllib.request.HTTPCookieProcessor())
            output_html = opener.open(url, timeout=30).read()
            output_html = str(output_html, 'utf-8')
        except (urllib.error.URLError, OSError) as e:
            # Keep the build going: show a link instead of the embedded content
            logger.warning("embedhttp: could not fetch %s: %s", url, e)
            output_html = ('<p>Could not load this content. '
                           '<a href="%s">Open it directly</a>.</p>' % url)

        output_html = strip_document_wrapper(output_html)
        return [nodes.raw('', '<div class="embedhttp">%s</div>' % output_html,
                          format='html')]


def strip_document_wrapper(html):
    """If html is a full document, keep only the head styles/scripts and
    the body contents, so it can be nested inside another page."""
    body = re.search(r'<body[^>]*>(.*)</body>', html, re.S | re.I)
    if not body:
        return html
    head = re.search(r'<head[^>]*>(.*?)</head>', html, re.S | re.I)
    head_html = head.group(1) if head else ''
    keep = re.findall(
        r'<link[^>]*rel=["\']?stylesheet[^>]*>|<style.*?</style>|<script.*?</script>',
        head_html, re.S | re.I)
    return '\n'.join(keep) + body.group(1)


def register():
    directives.register_directive('embedhttp', EmbedHttp)
