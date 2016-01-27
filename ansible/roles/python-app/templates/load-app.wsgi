def application(environ, start_response):
    status = '200 OK'
    output = 'mod_wsgi is setup ok for: {{ project_name }}'

    response_headers = [('Content-type', 'text/plain'),
                        ('Content-Length', str(len(output)))]
    start_response(status, response_headers)

    return [output]
