from django.http import HttpResponse
def welcome(request, name):
    """
    A simple Django view that takes a name from the URL
    and returns a personalized welcome message.
    """
    html = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Hello Django</title>
            <style>
                body {
                    background-color: green;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    margin: 0;
                }
                h1 {
                    color: red;
                    font-family: Arial, sans-serif;
                    font-size: 3em;
                }
            </style>
        </head>
        <body>
            <h1>Hello, World!</h1>
        </body>
        </html>
        """
    return HttpResponse(html)
