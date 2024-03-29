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
from pelican import signals
import urllib.request, urllib.error, urllib.parse


class EmbedHttp(Directive):
    """ Embed YouTube video in posts.

    Based on the YouTube directive by Brian Hsu:
    https://gist.github.com/1422773

    VIDEO_ID is required, with / height are optional integer,
    and align could be left / center / right.

    Usage:
    .. embed_http:: URL
        :width: 640
        :height: 480
        :align: center
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
#        width = 420
#        if 'width' in self.options:
#            width = self.options['width']
        print(("========= URL: %s" % url))

        opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor())
        output_html = opener.open(url).read()
        output_html = str(output_html,'utf-8')

        return [
            nodes.raw('', output_html, format='html')]


def register():
    directives.register_directive('embedhttp', EmbedHttp)
