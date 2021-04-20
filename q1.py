import pandas as pd
from decouple import config

FilePath= config('LOCATION')
test = pd.read_csv(FilePath)

def question_one(conn):
    df = (pd.DataFrame(test, columns = ["AppNumber","ApplicantType","Institution","OrganizationType","InstCity","InstState","InstPostalCode"
    "InstCountry","CongressionalDistrict","Latitude","Longitude","CouncilDate","YearAwarded","ProjectTitle", "Program","Division",
    "ApprovedOutright","ApprovedMatching","AwardOutright","AwardMatching","OriginalAmount"	,"SupplementAmount",
    "BeginGrant","EndGrant","ProjectDesc","ToSupport","PrimaryDiscipline","SupplementCount","Supplements","ParticipantCount","Participants"	
    "DisciplineCount","Disciplines"]))
    df = pd.read_sql_query("WITH RECURSIVE split(AppNumber, InstState, Participants, str) AS (SELECT AppNumber,InstState, '', Participants||';' FROM test UNION ALL SELECT AppNumber, InstState, substr(str, 0, instr(str, ';')),substr(str, instr(str, ';')+1) FROM split WHERE str!='') SELECT AppNumber,InstState, Participants FROM split WHERE Participants LIKE '%[Co Project Director]' AND InstState = 'NE';", conn)
    #print(df)
    df.to_json(r'/Users/shalini/Documents/testoutput1.json',orient='records')

#original attempt below but getting error with connecting to db
'''
def question_one(conn):
    df = (pd.DataFrame(test, columns = ["AppNumber","ApplicantType","Institution","OrganizationType","InstCity","InstState","InstPostalCode"
    "InstCountry","CongressionalDistrict","Latitude","Longitude","CouncilDate","YearAwarded","ProjectTitle", "Program","Division",
    "ApprovedOutright","ApprovedMatching","AwardOutright","AwardMatching","OriginalAmount"	,"SupplementAmount",
    "BeginGrant","EndGrant","ProjectDesc","ToSupport","PrimaryDiscipline","SupplementCount","Supplements","ParticipantCount","Participants"	
    "DisciplineCount","Disciplines"]))

    input_state = input("What state? : ")

    df = pd.read_sql_query("WITH RECURSIVE split(AppNumber, InstState, Participants, str) AS (SELECT AppNumber,InstState, '', Participants||';' FROM test UNION ALL SELECT AppNumber, InstState, substr(str, 0, instr(str, ';')),substr(str, instr(str, ';')+1) FROM split WHERE str!='') SELECT AppNumber,InstState, Participants FROM split WHERE Participants LIKE '%[Co Project Director]' AND InstState = '?';",conn, (input_state))
'''