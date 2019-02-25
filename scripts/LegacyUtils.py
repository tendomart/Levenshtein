import math
import pandas as pd
import Levenshtein

# properties
data_source_path: str = '../resources/Db.csv'

# initialize props
# create patient `tuple` to Levenshtein against
selected_patient = ("_0513130114210512",
                        "_1101021507051805", "_1919051821101001", "KAMPALA", "KCCA", "KAWEMPE DIVISION", "BWAISE III",
                        "KAWAALA", "1997", "M", "0704202234", "", "", "")

# columns (we'll use these to compute the Levenshtein distance)
distance_columns = ['Updated_GivenName', 'Updated_MiddleName', 'Updated_FamilyName', 'District', 'County',
                        'sub_county', 'Parish', 'village', 'Birthdate', 'Gender', 'Telephone Number',
                        'Treatment Supporter Telephone Number', 'First Encounter Date', 'ART Start Date']


# Read data from csv file
# Later change data source to openmrs_db
data = pd.read_csv(data_source_path)
data.dropna(subset=['Clinic No.', 'District'], inplace=True)

# STEP 5
# Combine THE DATA WITH ADDRESSES WITH THE and fill in the remaining spaces with NA
# dfbc - cleanup data
# nf - data that was omitted due to missing village names
# The idea is to get all the initial rows as per the original datasets combined
final_data = pd.read_csv(data_source_path)
final_dataframe = final_data
final_dataframe.dropna(subset=['Clinic No.', 'District'], inplace=True)
final_dataframe = final_dataframe.fillna("''")

fd = final_dataframe
fdx = fd
data = fd
# get duplicate phone numbers
data["is_duplicate"] = data.duplicated('Telephone Number')
data.loc[(data['is_duplicate'] == True)]


def calc_levenshtein_distance(row):
    """
    :param row: This a row of data(basically a patient entry) that will be calculated against this Patient we are
    searching
    :return: Return the levenshstein distance of the Patient in this row.

    """
    inner_value = 0
    counter = 0
    for k in distance_columns:

        if k == 'Updated_GivenName' or k == 'Updated_MiddleName' or k == 'Updated_FamilyName':
            constant = 0.5
        elif k == 'District' or k == 'County' or k == 'sub_county' or k == 'Parish' or k == 'village':
            constant = 0.05
        elif k == 'Birthdate' or k == 'ART Start Date' or k == 'First Encounter Date':
            constant = 0.01
        elif k == 'Telephone Number' or k == 'Treatment Supporter Telephone Number':
            constant = 0.075
        elif k == 'Gender':
            constant = 0.15

        inner_value += (((1 - Levenshtein.ratio(row[k], selected_patient[counter])) * constant) ** 2)
        counter += 1
    return math.sqrt(inner_value)


# Adding an event of what is done once `search` button is hit
def on_button_clicked():

    # Find the distance between the selected/chosen patient and everyone else.
    levenshtein_distances = data.apply(lambda row: calc_levenshtein_distance(row), axis=1)

    # STEP 5: WEIGHT SORTING
    # Create a new dataframe with distances.
    distance_frame = pd.DataFrame(
        data={"dist": levenshtein_distances, "idx": levenshtein_distances.index, "Clinic No.": data["Clinic No."]})
    distance_frame.sort_values("dist", inplace=True)

    # STEP 6: EVALUATION
    # Find the most similar patient's to the selected patient(the lowest distance to the sp (selected patient)
    # is sp, the second smallest is the most similar non-sp patient)
    second_smallest = distance_frame.iloc[1]["idx"]
    print(second_smallest)
    most_similar_to_sp = data.loc[int(second_smallest)]["Clinic No."]

    # Get the details
    patient = data[data["Clinic No."] == most_similar_to_sp].iloc[0]
    distance_frame = pd.DataFrame(
        data={"dist": levenshtein_distances, "idx": levenshtein_distances.index, "Clinic No.": data["Clinic No."],
              "Updated_GivenName": data["Updated_GivenName"], "Updated_MiddleName": data["Updated_MiddleName"],
              "Updated_FamilyName": data["Updated_FamilyName"], "District": data["District"], "County": data["County"],
              "sub_county": data["sub_county"], "Parish": data["Parish"], "village": data["village"],
              "Birthdate": data["Birthdate"], "Gender": data["Gender"], "Telephone Number": data["Telephone Number"],
              "Treatment Supporter Telephone Number": data["Treatment Supporter Telephone Number"],
              "First Encounter Date": data["First Encounter Date"], "ART Start Date": data["ART Start Date"]})
    distance_frame.sort_values("dist", inplace=True)

    # print distances/scores just to have an overview of the differences
    print(distance_frame.head())

    saved_df = distance_frame.head(4)

    # -----------------categorization ---------------------------------#
    def categorize_distances(row):
        category_name = ""
        try:
            distance_value = row["dist"]
            value = float(distance_value)
            if (value) == 0.000000:
                category_name = "Match"
            elif (0.000001 <= value <= 0.1):
                category_name = "Possible Match"
            elif (value > 0.1):
                category_name = "None Match"
            distance_value = ""
        except:
            category_name = "Not Categorised,Invalid Distance Value"
        return category_name

    categorised_distances = saved_df.apply(lambda row: categorize_distances(row), axis=1)
    saved_df = saved_df.assign(RecordCategory=categorised_distances.values)
    # saved_df['Category'] = Series(categorised_distances, index=saved_df.index)
    # categorised_distances.to_csv('saved_Levenshtein_distances_category.csv')
    # ---------------end of categorization----------------------------#
    saved_df.to_csv('saved_Levenshtein_distances.csv')
    print(saved_df)
    distance_framex = distance_frame


on_button_clicked()