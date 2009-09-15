from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter

class Index(webapp.RequestHandler):
  def get(self):
    self.response.headers['Content-Type'] = 'text/plain'
    self.response.out.write('get')
  def post(self):
    lang = self.request.get("lang")
    code = self.request.get("code")
    self.response.headers['Content-Type'] = 'text/html'
    self.response.out.write(pygmentize(lang, code))

application = webapp.WSGIApplication([('/', Index)], debug=True)

def pygmentize(lang, code):
  lexer = get_lexer_by_name(lang, stripall=True)
  formatter = HtmlFormatter(linenos=True, cssclass="highlight")
  return highlight(code, lexer, formatter)

def main():
  run_wsgi_app(application)

if __name__ == "__main__":
  main()