import random

from jsninjify.models import Buzzword, Descriptive, Word
from flask import Response, current_app as app, render_template, request, json, send_from_directory

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/secret', methods=['GET'])
def secret_get():
    code = request.args.get('code')

    if not code:
        return render_template('secret.html', code = False)

    else:
        code = code.lower()
        print(code)
        if code == "↑↑↓↓←→←→ba":
            return send_from_directory(app.config['UPLOAD_FOLDER'], "secret")
        else:
            return render_template('secret.html', code = True)


########## API ##########
@app.route('/ninjify', methods=['GET'])
def ninji_get():
    buzzwords = request.args.get('x')
    
    if (buzzwords):
        buzzwords = buzzwords.lower()
        if not (";" and "--") in buzzwords:
            #select words assiated to buzwords
            descriptive = list(Buzzword
                    .select(Word.word).distinct()
                    .join(Descriptive)
                    .join(Word)
                    .where(Buzzword.buzzword << buzzwords.split(","))
                    .dicts())

            #if none found
            if len(descriptive) == 0:
                response = Response(status=400, content_type="application/json", response=json.dumps({ "error": "Buzzwords not found." }))
            else:
                ninjaName = ""
                
                #select up to 4 words out of the ones that were found
                previouslyChosen = []
                for i in range(random.randrange(1, 3)):
                    chosen = descriptive[random.randrange(len(descriptive))]["word"]

                    while chosen in previouslyChosen:
                        chosen = descriptive[random.randrange(len(descriptive))]["word"]

                    ninjaName += chosen + " "
                    previouslyChosen.append(chosen)

                response = Response(status=200, content_type="application/json", response=json.dumps({ "ninjaname" : ninjaName}))
        else:
            response = Response(status=403, content_type="application/json", response=json.dumps({ "error": "No injections here."}))
    else:
        response = Response(status=400, content_type="application/json", response=json.dumps({ "error": "Missing Buzzwords."}))

    return response

@app.route('/ninjify', methods=['POST'])
def ninji_post():
    return Response(status=501, content_type="application/json", response=json.dumps({ "error": "Can't add yet."}))

@app.route('/ninjify', methods=['PUT'])
def ninji_put():
    return Response(status=501, content_type="application/json", response=json.dumps({ "error": "Can't update yet."}))

@app.route('/ninjify', methods=['DELETE'])
def ninji_del():
    return Response(status=501, content_type="application/json", response=json.dumps({ "error": "Can't remove yet."}))