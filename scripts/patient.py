from datetime import datetime


class Patient:
    def __init__(self,
                 # names
                 given_name, middle_name, family_name,
                 # address props
                 district, county, sub_county, parish, village,
                 # others
                 birthdate, gender, tel_num, supporter_tel_num, first_enc_date, art_start_date):
        self.given_name = given_name
        self.middle_name = middle_name
        self.family_name = family_name
        self.district = district
        self.county = county
        self.sub_county = sub_county
        self.parish = parish
        self.village = village
        self.birthdate = format_date(birthdate)
        self.gender = gender
        self.tel_num = tel_num
        self.supporter_tel_num = supporter_tel_num
        self.first_enc_date = format_date(first_enc_date)
        self.art_start_date = format_date(art_start_date)
        self.distance_from_other_patient = None
        # By default this `Patient` is not a match
        self.match: Matcher = Matcher.NO_MATCH

    # Default constructor
    def __init__(self):
        pass


class Matcher:
    MATCH = 0
    POSSIBLE_MATCH = 1
    NO_MATCH = -1


def format_date(datetime_string):
    date_format = '%Y-%m-%d'
    if datetime_string:
        try:
            # Trim off the time
            date_string = datetime_string[0:9]
            return datetime.strptime(date_string, date_format).date().strftime(date_format)
        except:
            return ""

    return ""
