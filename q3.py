import pandas as pd
test = pd.read_csv('/Users/shalini/Documents/neh-grants-2010-2019-csv-1.csv')

def question_three(conn):
    df3 = (pd.DataFrame(test, columns = ["AppNumber","ApplicantType","Institution","OrganizationType","InstCity","InstState","InstPostalCode"
    "InstCountry","CongressionalDistrict","Latitude","Longitude","CouncilDate","YearAwarded","ProjectTitle", "Program","Division",
    "ApprovedOutright","ApprovedMatching","AwardOutright","AwardMatching","OriginalAmount"	,"SupplementAmount",
    "BeginGrant","EndGrant","ProjectDesc","ToSupport","PrimaryDiscipline","SupplementCount","Supplements","ParticipantCount","Participants"	
    "DisciplineCount","Disciplines"]))
    df3 = pd.read_sql_query("SELECT InstState, COUNT(ProjectTitle) AS Count_Of_Projects, SUM(ApprovedOutright+(ApprovedMatching-AwardMatching)) AS Grants FROM test GROUP BY InstState",conn)
    #print(df3)
    df3.to_json(r'/Users/shalini/Documents/testoutput3.json',orient='records')