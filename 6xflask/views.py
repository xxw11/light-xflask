import json

from app import View, App, render_template, session


class Index(View):
    def GET(self,request):
        session['hello'] = 2
        return  render_template("index.html")
    def POST(self,request):
        return json.dumps({'1':'hello'})

class Test(View):

    def GET(self,request):
        print(session['hello'])
        return  render_template("test.html")
    def POST(self, request):
        return json.dumps({'2': 'hello'})

urls={'/':Index,
      '/test':Test}

if __name__ == '__main__':
    app=App()
    app.secret_key = 'password'
    app.add_url_rule(urls)
    app.run()