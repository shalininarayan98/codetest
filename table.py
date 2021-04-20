def sqlite_table(conn):
    c = conn.cursor()
    c.execute('''CREATE TABLE test (AppNumber text,ApplicantType text,Institution text,OrganizationType text,
    InstCity text,InstState text,InstPostalCode text,InstCountry text,CongressionalDistrict text,Latitude text,Longitude text,
    CouncilDate datetime,YearAwarded date,ProjectTitle text,Program text,Division text,ApprovedOutright int,ApprovedMatching int,
    AwardOutright int,AwardMatching int,OriginalAmount int,SupplementAmount int,BeginGrant datetime,EndGrant datetime,
    ProjectDesc text,ToSupport text,PrimaryDiscipline int,SupplementCount int,Supplements text,ParticipantCount int,
    Participants text,DisciplineCount int,Disciplines text)''')

    conn.commit()