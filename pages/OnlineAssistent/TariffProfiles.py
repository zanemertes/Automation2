OA_EMPLOYEE = "Angestellter"
OA_SELF_EMPLOYED = "Selbstständig"
OA_CIVIL_SERVANT = "Beamter"
OA_CIVIL_SERVANT_APPLICANT = "Beamtenanwärter"
OA_STUDENT = "Student oder in Ausbildung"
OA_PRIVATE = "privat"
OA_GOVERN = "gesetzlich"
OA_JA = "Ja"
OA_NEIN = "Nein"

job_types_UI_Online_Assitant = {OA_EMPLOYEE: 'Angestellter',
                                OA_SELF_EMPLOYED: 'Selbstständig',
                                OA_CIVIL_SERVANT: 'Beamter',
                                OA_CIVIL_SERVANT_APPLICANT: 'Beamtenanwärter',
                                OA_STUDENT: 'Student'}


# for key in job_types_UI_Online_Assitant.keys():
#    print(key)



# Angestellter has following fields: Geburtsdatum, Berufstatus, Einkommen, Versicherungstype
# Selbständig has following fields: Geburtsdatum, Berufstatus, WIE VIELE MITARBEITER HAST DU?, Versicherungstype
# Beamter has following fields: Geburtsdatum, Berufstatus, Versicherungstype
# Beamtenanwärter has following fields: Geburtsdatum, Berufstatus, Versicherungstype
# Student oder in Ausbildung has following fields: Geburtsdatum, Berufstatus, Zukünftiger Beamter, Versicherungstype
