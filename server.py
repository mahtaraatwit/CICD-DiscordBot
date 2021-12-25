from sanic import Sanic
from sanic import response
  
app = Sanic("Puffy-Bot")
  
  
# webapp path defined used route decorator
@app.route("/")
def run(request):
    return response.text("Online . . .")
  
  
# debug logs enabled with debug = True
app.run(host ="0.0.0.0", port = 8000, debug = True)