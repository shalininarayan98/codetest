import pandas as pd
test = pd.read_csv('/Users/shalini/Documents/neh-grants-2010-2019-csv-1.csv')

def question_two(conn):
    df2 = (pd.DataFrame(test, columns = ["AppNumber","ApplicantType","Institution","OrganizationType","InstCity","InstState","InstPostalCode"
    "InstCountry","CongressionalDistrict","Latitude","Longitude","CouncilDate","YearAwarded","ProjectTitle", "Program","Division",
    "ApprovedOutright","ApprovedMatching","AwardOutright","AwardMatching","OriginalAmount"	,"SupplementAmount",
    "BeginGrant","EndGrant","ProjectDesc","ToSupport","PrimaryDiscipline","SupplementCount","Supplements","ParticipantCount","Participants"	
    "DisciplineCount","Disciplines"]))
    df2 = pd.read_sql_query("SELECT YearAwarded, SUM(SupplementAmount) AS Total_SupplementAmount FROM test GROUP BY YearAwarded",conn)
    #print(df2)
    df2.to_json(r'/Users/shalini/Documents/testoutput2.json',orient='records')