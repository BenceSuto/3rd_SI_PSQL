from flask import Flask, render_template

import data_manager

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/mentors')
def mentor_and_school_names():
    datas = data_manager.get_mentor_and_school_names()
    return render_template('mentor_and_school.html', names=datas)


@app.route('/all-school')
def all_school_names():
    school_names = data_manager.get_all_mentor_and_school_names()
    return render_template('school_names.html', school_names=school_names)


@app.route('/mentors-by-country')
def mentors_by_country():
    mentors = data_manager.get_mentors_by_country()
    return render_template('mentors_by_country.html', mentors=mentors)


@app.route('/contacts')
def schools_by_contacts():
    contact = data_manager.get_schools_by_contacts()
    return render_template('schools_by_contact.html', contact=contact)


@app.route('/applicants')
def applicants_data():
    applicants = data_manager.get_all_data_from_applicants()
    return render_template('applicants_data.html', applicants=applicants)


@app.route('/applicants-and-mentors')
def applicants_and_mentors_data():
    applicants_and_mentors = data_manager.get_all_data_from_applicants_and_mentors()
    return render_template('applicants_and_mentors.html', applicants=applicants_and_mentors)



if __name__ == '__main__':
    app.run(debug=True)
