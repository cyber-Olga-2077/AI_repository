from app import app
from flask import render_template
from app.forms import PredictionForm
from flask import render_template, request
from app.prediction import make_prediction


allowed_extensions = {'png', 'jpg', 'jpeg', 'webp'}


@app.route('/', defaults = {'path': ''}, methods= ["GET", "POST"])
@app.route('/<path:path>', methods= ["GET", "POST"])
def index(path):
    form = PredictionForm()

    result = [None, None]
    if form.validate_on_submit():
        file = request.files['image']
        if file.filename.split('.')[-1] in allowed_extensions:
            result = make_prediction(file)
    print(result, flush=True)
    return render_template('index.html', form=form, result=result[0], other=result[1])
