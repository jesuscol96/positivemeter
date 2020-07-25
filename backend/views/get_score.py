from flask import render_template, request, jsonify
from AI import process_text

def get_score():
    if request.method == 'POST':
        if 'text' in request.form:
            #Get request count
            try:
                request_count_file = open('assets/request_count.txt','r')
                request_count = int(request_count_file.read())
            except:
                request_count = 0
            else:
                request_count_file.close()
            #Process text
            score = process_text(request.form['text'])
            #Update request count
            request_count_file = open('assets/request_count.txt','w')
            request_count_file.write(str(request_count+1))
            request_count_file.close()
            return jsonify({'score': score})
        else:
            return 'error'
    else:
        return 'error'

def get_request_count():
    try:
        request_count_file = open('assets/request_count.txt','r')
        request_count = int(request_count_file.read())
    except:
        request_count = 0
    else:
        request_count_file.close()
    return jsonify({'request_count': request_count})
