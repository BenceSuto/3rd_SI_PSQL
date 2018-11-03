import database_common


@database_common.connection_handler
def get_mentor_and_school_names(cursor):
    cursor.execute("""
                    SELECT mentors.first_name, mentors.last_name, schools.name, schools.country
                    FROM mentors
                    INNER JOIN schools ON mentors.id=schools.contact_person
                    ORDER BY mentors.id;
                   """)
    return cursor.fetchall()


@database_common.connection_handler
def get_all_mentor_and_school_names(cursor):
    cursor.execute("""
                    SELECT mentors.first_name, mentors.last_name, schools.name, schools.country
                    FROM mentors
                    FULL OUTER JOIN schools ON mentors.id=schools.contact_person
                    ORDER BY mentors.id;
                   """)
    return cursor.fetchall()


@database_common.connection_handler
def get_mentors_by_country(cursor):
    cursor.execute("""
                    SELECT schools.country, COUNT(mentors.first_name)
                    FROM mentors
                    INNER JOIN schools ON mentors.id=schools.contact_person
                    GROUP BY schools.country;
                   """)
    return cursor.fetchall()


@database_common.connection_handler
def get_schools_by_contacts(cursor):
    cursor.execute("""
                    SELECT schools.name, COUNT(mentors.first_name)
                    FROM mentors
                    RIGHT JOIN schools ON mentors.id=schools.contact_person
                    GROUP BY schools.name;
                   """)
    return cursor.fetchall()


@database_common.connection_handler
def get_all_data_from_applicants(cursor):
    cursor.execute("""
                    SELECT applicants.first_name, applicants.application_code, applicants_mentors.creation_date 
                    FROM applicants
                    RIGHT JOIN applicants_mentors ON applicants.id=applicants_mentors.applicant_id
                    WHERE applicants_mentors.creation_date > '2016-01-01'
                    ORDER BY applicants_mentors.creation_date;
                   """)
    return cursor.fetchall()


@database_common.connection_handler
def get_all_data_from_applicants_and_mentors(cursor):
    cursor.execute("""
                    SELECT applicants.first_name, applicants.application_code, applicants_mentors.creation_date 
                    FROM applicants
                    RIGHT JOIN applicants_mentors ON applicants.id=applicants_mentors.applicant_id
                    ORDER BY applicants_mentors.creation_date;
                   """)
    return cursor.fetchall()
