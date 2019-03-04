from flask import Flask, render_template, request
import scripts.rest as rest
import scripts.LevenshteinUtils as utils
from scripts.patient import Patient, format_date

app = Flask(__name__)


# The index page
@app.route("/")
def index():
    return render_template("index.html")


# The login page
@app.route("/login")
def get_login():
    pass


@app.route("/results")
def get_results(patient_search_results):
    print(patient_search_results)
    return render_template("results.html", results=patient_search_results)


@app.route("/do_levenshtein_search", methods=["post"])
def do_levenshtein_search():
    search_candidate = __init_patient__(request)
    return get_results(utils.do_levenshtein_search(rest.get_patients_restfully(search_candidate.given_name),
                                                   search_candidate))


def __init_patient__(request):
    candidate = Patient()
    candidate.given_name = request.form.get('given_name')
    candidate.middle_name = request.form.get('middle_name')
    candidate.family_name = request.form.get('family_name')
    candidate.gender = request.form.get('gender')
    candidate.district = request.form.get('district')
    candidate.county = request.form.get('county')
    candidate.sub_county = request.form.get('sub_county')
    candidate.parish = request.form.get('parish')
    candidate.village = request.form.get('village')
    candidate.birthdate = format_date(request.form.get('birth_date'))
    candidate.supporter_tel_num = request.form.get('supp_tel_no')
    candidate.first_enc_date = format_date(request.form.get('first_enc_date'))
    candidate.art_start_date = format_date(request.form.get('art_start_date'))
    return candidate


if __name__ == "__main__":
    app.run(debug=True, port=1100)
