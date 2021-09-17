from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    # return "<p>Hello, World!</p>"
    return '''<!doctype html>        <!-- Using getbootstrap.com HTML Starter template --> 
    <html lang="en">
    <head>
        <!-- Required meta tags -->
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">

        <!-- Bootstrap CSS -->
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-F3w7mX95PdgyTmZZMECAngseQB83DfGTowi0iMjiWaeVhAn4FJkqJByhZMI3AhiU" crossorigin="anonymous">

        <title>Hello, world!</title>
    </head>
    <body>
        <h1>Hello, world!</h1>

        <!-- USING BOOTSTRAP ALERT COMPONENT -->
        
        <div class="alert alert-primary" role="alert">
    A simple primary alert—check it out!
    </div>
    <div class="alert alert-secondary" role="alert">
    A simple secondary alert—check it out!
    </div>
    <div class="alert alert-success" role="alert">
    A simple success alert—check it out!
    </div>
    <div class="alert alert-danger" role="alert">
    A simple danger alert—check it out!
    </div>
    <div class="alert alert-warning" role="alert">
    A simple warning alert—check it out!
    </div>
    <div class="alert alert-info" role="alert">
    A simple info alert—check it out!
    </div>
    <div class="alert alert-light" role="alert">
    A simple light alert—check it out!
    </div>
    <div class="alert alert-dark" role="alert">
    A simple dark alert—check it out!
    </div>

        <!-- Optional JavaScript; choose one of the two! -->

        <!-- Option 1: Bootstrap Bundle with Popper -->
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-/bQdsTh/da6pkI1MST/rWKFNjaCP5gBSY4sEBT38Q/9RBh9AH40zEOg7Hlq2THRZ" crossorigin="anonymous"></script>

        <!-- Option 2: Separate Popper and Bootstrap JS -->
        <!--
        <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.3/dist/umd/popper.min.js" integrity="sha384-W8fXfP3gkOKtndU4JGtKDvXbO53Wy8SZCQHczT5FMiiqmQfUpWbYdTil/SxwZgAN" crossorigin="anonymous"></script>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.1/dist/js/bootstrap.min.js" integrity="sha384-skAcpIdS7UcVUC05LJ9Dxay8AXcDYfBJqt1CJ85S/CFujBsIzCIv+l9liuYLaMQ/" crossorigin="anonymous"></script>
        -->
    </body>
    </html>'''      # Using getbootstrap.com HTML Starter template

if __name__ == "__main__":
    app.run(debug=True)     # Using debug feature of 'flask'
    