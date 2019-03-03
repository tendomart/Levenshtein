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
        self.birthdate = birthdate
        self.gender = gender
        self.tel_num = tel_num
        self.supporter_tel_num = supporter_tel_num
        self.first_enc_date = first_enc_date
        self.art_start_date = art_start_date
        self.distance_from_other_patient = None
        # By default this `Patient` is not a match
        self.match: Matcher = Matcher.NO_MATCH

    #def __init__(self, given_name):
        #self.given_name = given_name



class Matcher:
    MATCH = 0
    POSSIBLE_MATCH = 1
    NO_MATCH = -1

