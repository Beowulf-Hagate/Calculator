
from flask import Flask, request, render_template

app = Flask(__name__, template_folder='', static_folder='')


@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		value = request.form.get('text')
		return render_template('index.html', value=eval(value))

	return render_template('index.html')

# TODO: A lot of error-checking to do.


if __name__ == "__main__":
	app.run()
