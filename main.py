import random, string
from flask import Flask, render_template, request
from flask_apscheduler import APScheduler
from scrap import loop_for_company
app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)

# initialize scheduler
scheduler = APScheduler()
# if you don't wanna use a config, you can set options here:
# scheduler.api_enabled = True
scheduler.init_app(app)


# interval example
@scheduler.task('interval', id='job_1', seconds=60*60*24, misfire_grace_time=900)
def job1():
    loop_for_company("datacm")

@scheduler.task('interval', id='job_2', seconds=60*60*24, misfire_grace_time=900)
def job2():
    loop_for_company('arht-media-inc-')

@scheduler.task('interval', id='job_3', seconds=60*60*24, misfire_grace_time=900)
def job3():
    loop_for_company('peakfintech')

scheduler.start()
  

ok_chars = string.ascii_letters + string.digits


@app.route('/')  # What happens when the user visits the site
def base_page():

	random_num = random.randint(1, 100000)  # Sets the random number
	return render_template(
		'base.html',  # Template file path, starting from the templates folder. 
		random_number=random_num  # Sets the variable random_number in the template
	)


@app.route('/2')
def page_2():
	rand_ammnt = random.randint(10, 100)
	random_str = ''.join(random.choice(ok_chars) for a in range(rand_ammnt))
	return render_template('site_2.html', random_str=random_str)


if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
		host='0.0.0.0',  # Establishes the host, required for repl to detect the site
		port=random.randint(2000, 9000)  # Randomly select the port the machine hosts on.
	)