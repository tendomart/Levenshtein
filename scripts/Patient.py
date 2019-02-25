class Patient :
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

