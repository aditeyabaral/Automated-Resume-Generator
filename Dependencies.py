import pyodbc
import re, string
from datetime import date
import ResumeGenerator

connection = pyodbc.connect('Driver={SQL Server};'
                      'Server=LAPTOP-HOLIG319;'
                      'Database=DBMS;'
                      'Trusted_Connection=yes;'
                      'MARS_Connection = YES;')

def createMember():
    cur = connection.cursor()

    memberList = cur.execute("SELECT MEMBER_ID FROM MEMBER").fetchall()
    if memberList == []:
        memberCount = 1
    else:
        mList = [i[0] for i in memberList]
        memberCount = int(max(mList)[4:10]) + 1
    memberID = "MEM#" + str(memberCount).zfill(6)
    
    name = input("Name : ")
    while not all(x.isalpha() or x == "" or x == " " for x in name):
        print("Invalid format. Please enter a valid name.")
        name = input("Name : ")

    password = input("Password (At least 8 characters long) : ")
    while len(password) < 8:
        print("Invalid format. Password has to be atleast 8 characters long.")
        password = input("Password: ")

    email = input("Email ID : ")
    pattern = r'^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    while not(re.search(pattern, email)):
        print("Invalid format. Please enter a valid email address.")
        email = input("Email ID : ")

    phone = input("Phone : ")
    while not(phone.isdigit() and len(phone) == 10):
        print("Invalid format. Please enter valid 10 digit phone number.")
        phone = input("Phone : ")

    address = input("Residential Address or NA: ")
    if address.upper() == 'NA':
        address = None

    bio = input("Enter bio or NA: ")
    if bio.upper() == 'NA':
        bio = None

    gitHub = input("Enter Github URL or NA: ")
    if gitHub.upper() == 'NA':
        gitHub = None

    linkedIn = input("Enter LinkedIn URL or NA: ")
    if linkedIn.upper() == 'NA':
        linkedIn = None

    cur.execute("INSERT INTO MEMBER VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", (memberID, password, name, email, phone, address, bio, gitHub, linkedIn))

    connection.commit()
    cur.close()
    return memberID

def school():
    cur = connection.cursor()

    schoolName = input("School name : ").upper()
    while not all(x.isalpha() or x == "" or x == " " or x.isdigit() or x in string.punctuation for x in schoolName):
        print("Invalid format. Please enter valid school name.")
        schoolName = input("School name : ").upper()
    
    location = input("Location of school : ").upper()
    while not all(x.isalnum() or x == "" or x == " " or x.isdigit() or x in string.punctuation for x in location):
        print("Invalid format. Please enter valid location.")
        location = input("Location of school : ").upper()

    checkSchool = cur.execute("SELECT NAME FROM SCHOOL WHERE NAME = ? AND LOCATION = ?", (schoolName, location)).fetchall()
    if checkSchool == []:
        schoolList = cur.execute("SELECT SCHOOL_ID FROM SCHOOL").fetchall()
        if schoolList == []:
            schoolCount = 1
        else:
            sList = [i[0] for i in schoolList]
            schoolCount = int(max(sList)[4:10]) + 1
        schoolID = "SCH#" + str(schoolCount).zfill(6)
        cur.execute("INSERT INTO SCHOOL VALUES (?, ?, ?)", (schoolID, location, schoolName))
    else:
        schoolID = cur.execute("SELECT SCHOOL_ID FROM SCHOOL WHERE NAME = ? AND LOCATION = ?", (schoolName, location)).fetchall()[0][0]
    
    connection.commit()
    cur.close()
    return schoolID

def schooling(memberID):
    cur = connection.cursor()

    for passingLevel in [10, 12]:
        print("Enter schooling details for Grade {}\n".format(str(passingLevel)))
        schoolID = school()

        stream = input("Enter stream (Science, Commerce, Arts or Humanities) : " )
        while stream not in ['Science', 'Commerce', 'Arts', 'Humanities']:
            print("Invalid format. Please enter valid stream.")
            stream = input("Enter stream (Science, Commerce, Arts or Humanities) : ")

        passingYear = int(input("Enter passing year : "))
        while not(len(str(passingYear)) == 4):
            print("Invalid format. Please enter valid passing year.")
            passingYear = int(input("Enter passing year : "))

        score = float(input("Enter percentage : "))
        while not(0.0 <= score <= 100.0):
            print("Invalid format. Please enter valid score.")
            score = float(input("Enter percentage : "))
        
        cur.execute("INSERT INTO SCHOOLING VALUES (?, ?, ?, ?, ?, ?)", (memberID, schoolID, passingLevel, stream, passingYear, score))
        print()

    connection.commit()
    cur.close()

def degreeInfo(typeGraduation, degree, major):  
    cur = connection.cursor()

    checkDegree = cur.execute("SELECT TYPE_OF_GRADUATION FROM DEGREE_INFO WHERE TYPE_OF_GRADUATION = ? AND DEGREE = ? AND MAJOR = ?", (typeGraduation, degree, major)).fetchall()
    if checkDegree == []:
            degreeList = cur.execute("SELECT DEGREE_ID FROM DEGREE_INFO").fetchall()
            if degreeList == []:
                degreeCount = 1
            else:
                dList= [i[0] for i in degreeList]
                degreeCount = int(max(dList)[4:10]) + 1
            degreeID = "DEG#" + str(degreeCount).zfill(6)
            cur.execute("INSERT INTO DEGREE_INFO VALUES (?, ?, ?, ?)", (degreeID, typeGraduation, degree, major))
    else:
            degreeID = cur.execute("SELECT DEGREE_ID FROM DEGREE_INFO WHERE TYPE_OF_GRADUATION = ? AND DEGREE = ? AND MAJOR = ?", (typeGraduation, degree, major)).fetchall()[0][0]

    connection.commit()
    cur.close()
    return degreeID
        
def higherEducation(memberID):
    cur = connection.cursor()

    while True:
        typeGraduation = input("Enter type of graduation i.e. (Bachelor's / Master's / Doctorate) or NA : ").upper()

        if typeGraduation=='NA':
            break

        while not all(x.isalpha() or x == "" or x == "'" for x in typeGraduation):
            print("Invalid format. Please enter valid type of graduation.")
            typeGraduation = input("Enter type of graduation i.e. (Bachelor's / Master's / Doctorate)")

        degree = input("Enter degree : ").upper()
        while not all(x.isalpha() or x == "" or x == " " or x == "." for x in degree):
            print("Invalid format. Please enter valid degree.")
            degree = input("Enter degree : ")

        major = input("Enter major : ").upper()
        while not all(x.isalpha() or x == "" or x == " " for x in major):
            print("Invalid format. Please enter valid major.")
            major = input("Enter major : ")

        degreeID = degreeInfo(typeGraduation, degree, major)

        universityName = input("Name of University : ").upper()
        while not all(x.isalpha() or x == "" or x == " " or x.isdigit() or x in string.punctuation for x in universityName):
            print("Invalid format. Please enter valid university name.")
            universityName = input("Name of University : ").upper()

        gpa = float(input("Enter GPA between 0 and 10 : "))
        while not(0.0 <= gpa <= 10.0):
            print("Invalid format. Please enter valid GPA.")
            gpa = float(input("Enter GPA between 0 and 10 : "))

        cur.execute("INSERT INTO HIGHER_EDUCATION VALUES (?, ?, ?, ?)", (memberID, degreeID, gpa, universityName))

        ch = input("Have you finished entering higher education information?[y/n]: ")
        if ch.upper() == 'Y':
            break
        
    connection.commit()
    cur.close()

def skills(memberID):
    cur = connection.cursor()

    while True:
        skill = input("Enter skill or NA: ")

        if skill.upper() == 'NA':
            break

        while not all(x.isalpha() or x == "" or x == " " or x.isdigit() or x in string.punctuation for x in skill):
                print("Invalid format. Please enter valid skill.")
                skill = input("Enter skill : ")

        experienceLevel = int(input("Enter experience level between 0 and 10 : "))
        while not(0 <= experienceLevel <= 10):
            print("Invalid format. Please enter valid experience level.")
            experienceLevel = int(input("Enter experience level between 0 and 10 : "))

        cur.execute("INSERT INTO SKILLS VALUES (?, ?, ?)", (memberID, skill, experienceLevel))

        ch = input("Have you finished entering your skills?[y/n]: ")
        if ch.upper() == 'Y':
            break
    
    connection.commit()
    cur.close()
    
def projects(memberID):
    cur = connection.cursor()

    while True:
        projectTitle = input("Enter project title or NA: ")

        if projectTitle.upper() == 'NA':
            break

        while not all(x.isalnum() or x == "" or x == " " or x.isdigit() or x in string.punctuation for x in projectTitle):
                print("Invalid format. Please enter valid project title.")
                projectTitle = input("Enter project title : ")

        projDescription = input("Enter project description : ")
        while not all(x.isalnum() or x == "" or x == " " or x.isdigit() or x in string.punctuation for x in projDescription):
                print("Invalid format. Please enter valid project description.")
                projDescription = input("Enter project description : ")

        cur.execute("INSERT INTO PROJECTS VALUES (?, ?, ?)", (memberID, projectTitle, projDescription))

        ch = input("Have finished entering your projects?[y/n]: ")
        if ch.upper() == 'Y':
            break

    connection.commit()
    cur.close()

def job(jobTitle, jobLocation, jobDescription, employer):
    cur = connection.cursor()

    checkJob = cur.execute("SELECT TITLE FROM JOB WHERE TITLE = ? AND LOCATION = ? AND DESCRIPTION = ? AND EMPLOYER = ?", (jobTitle, jobLocation, jobDescription, employer)).fetchall()
    if checkJob == []:
            jobList = cur.execute("SELECT JOB_ID FROM JOB").fetchall()
            if jobList == []:
                jobCount = 1
            else:
                jList = [i[0] for i in jobList]
                jobCount = int(max(jList)[4:10]) + 1
            jobID = "JOB#" + str(jobCount).zfill(6)
            cur.execute("INSERT INTO JOB VALUES (?, ?, ?, ?, ?)", (jobID, jobTitle, jobLocation, jobDescription, employer))
    else:
            jobID = cur.execute("SELECT JOB_ID FROM JOB WHERE TITLE = ? AND LOCATION = ? AND DESCRIPTION = ? AND EMPLOYER = ?", (jobTitle, jobLocation, jobDescription, employer)).fetchall()[0][0]
    
    connection.commit()
    cur.close()
    return jobID

def experience(memberID):
    cur = connection.cursor()

    while True:
        jobTitle = input("Enter job title or NA: ")

        if jobTitle.upper() == 'NA':
            break

        while not all(x.isalnum() or x == "" or x == " " or x.isdigit() or x in string.punctuation for x in jobTitle):
            print("Invalid format. Please enter valid job title.")
            jobTitle = input("Enter job title : ")

        jobLocation = input("Enter job location : ")
        while not all(x.isalnum() or x == "" or x == " " or x.isdigit() or x in string.punctuation for x in jobLocation):
            print("Invalid format. Please enter valid job location.")
            jobLocation = input("Enter job location : ")

        jobDescription = input("Enter job description : ")
        while not all(x.isalnum() or x == "" or x == " " or x.isdigit() or x in string.punctuation for x in jobDescription):
            print("Invalid format. Please enter valid job description.")
            jobDescription = input("Enter job description : ")

        employer = input("Enter employer : ")
        while not all(x.isalpha() or x == "" or x == " " or x.isdigit() or x in string.punctuation for x in employer):
            print("Invalid format. Please enter valid employer.")
            employer = input("Enter employer : ")

        jobID = job(jobTitle, jobLocation, jobDescription, employer)

        startDate = input('Enter start date (YYYY - MM - DD) : ')
        year, month, day = map(int, startDate.split('-'))
        startDate = date(year, month, day)
        startDate = startDate.strftime('%Y-%m-%d')

        endDate = input('Enter end date if applicable (YYYY - MM - DD), else enter NA : ').upper()
        if endDate.upper() != 'NA':
            year, month, day = map(int, endDate.split('-'))
            endDate = date(year, month, day)
            endDate = endDate.strftime('%Y-%m-%d')
        else:
            endDate = None
            
        cur.execute("INSERT INTO EXPERIENCE VALUES (?, ?, ?, ?)", (memberID, jobID, startDate, endDate))
        ch = input("Have you finished entering your job details?[y/n]: ")
        if ch.upper() == 'Y':
            break

    connection.commit()
    cur.close()

def accomplishments(memberID):
    cur = connection.cursor()

    while True:
        accomplishment = input("Enter accomplishment or NA: ")

        if accomplishment.upper() == 'NA':
            break

        while not all(x.isalnum() or x == "" or x == " " or x.isdigit() or x in string.punctuation for x in accomplishment):
                print("Invalid format. Please enter valid accomplishment.")
                accomplishment = input("Enter accomplishment : ")

        accDescription = input("Enter accomplishment description : ")
        while not all(x.isalnum() or x == "" or x == " " or x.isdigit() or x in string.punctuation for x in accDescription):
                print("Invalid format. Please enter valid accomplishment description.")
                accDescription = input("Enter accomplishment description : ")

        cur.execute("INSERT INTO ACCOMPLISHMENTS VALUES (?, ?, ?)", (memberID, accomplishment, accDescription))

        ch = input("Have you finished entering your accomplishments?[y/n]: ")
        if ch.upper() == 'Y':
            break

    connection.commit()
    cur.close()

def certifications(memberID):
    cur = connection.cursor()

    while True:
        certificationURL = input("Enter certification URL as issued by the issuing authority or NA: ")

        if certificationURL.upper() == 'NA':
            break

        while not all(x.isalnum() or x == "" or x == " " or x.isdigit() or x in string.punctuation for x in certificationURL):
                print("Invalid format. Please enter a valid certification URL.")
                certification = input("Enter certification URL as issued by the issuing authority : ")

        certification = input("Enter certification name : ")
        while not all(x.isalnum() or x == "" or x == " " or x.isdigit() or x in string.punctuation for x in certification):
                print("Invalid format. Please enter valid certification.")
                certification = input("Enter certification : ")

        cur.execute("INSERT INTO CERTIFICATIONS VALUES (?, ?, ?)", (memberID, certificationURL, certification))

        ch = input("Have finished entering your certifications?[y/n]: ")
        if ch.upper() == 'Y':
            break

    connection.commit()
    cur.close()

def queryResults(memberID):
    cur = connection.cursor()

    bDetails = cur.execute("SELECT M.NAME, M.BIO, M.ADDRESS, M.PHONE, M.EMAIL, M.GITHUB, M.LINKEDIN FROM MEMBER M WHERE M.MEMBER_ID = ?", memberID).fetchall()
    sDetails = cur.execute("SELECT S.NAME AS SCHOOL, S.LOCATION, SCH.PASSING_LEVEL, SCH.PASSING_YEAR, SCH.STREAM, SCH.SCORE FROM MEMBER M INNER JOIN SCHOOLING SCH ON M.MEMBER_ID = SCH.MEMBER_ID INNER JOIN SCHOOL S ON SCH.SCHOOL_ID = S.SCHOOL_ID WHERE M.MEMBER_ID = ?", memberID).fetchall()
    hDetails = cur.execute("SELECT D.DEGREE, D.MAJOR, H.UNIVERSITY, H.GPA FROM MEMBER M INNER JOIN HIGHER_EDUCATION H ON M.MEMBER_ID = H.MEMBER_ID INNER JOIN DEGREE_INFO D ON H.DEGREE_ID = D.DEGREE_ID WHERE M.MEMBER_ID = ?", memberID).fetchall()
    jDetails = cur.execute("SELECT J.EMPLOYER, J.LOCATION, J.TITLE, J.DESCRIPTION, DURATION = (CASE WHEN E.END_DATE IS NULL THEN DATEDIFF(YEAR, E.START_DATE, GETDATE()) WHEN E.END_DATE IS NOT NULL THEN DATEDIFF(YEAR, E.START_DATE, E.END_DATE)END) FROM MEMBER M INNER JOIN EXPERIENCE E ON M.MEMBER_ID = E.MEMBER_ID INNER JOIN JOB J ON E.JOB_ID = J.JOB_ID WHERE M.MEMBER_ID = ?", memberID).fetchall()
    pDetails = cur.execute("SELECT P.PROJECT_NAME, P.DESCRIPTION FROM MEMBER M INNER JOIN PROJECTS P ON M.MEMBER_ID = P.MEMBER_ID WHERE M.MEMBER_ID = ?", memberID).fetchall()
    skDetails = cur.execute("SELECT SK.SKILL_NAME, SK.EXPERIENCE_LEVEL FROM MEMBER M INNER JOIN SKILLS SK ON M.MEMBER_ID = SK.MEMBER_ID WHERE M.MEMBER_ID = ?", memberID).fetchall()
    aDetails = cur.execute("SELECT A.ACCOMPLISHMENT_NAME, A.DESCRIPTION FROM MEMBER M INNER JOIN ACCOMPLISHMENTS A ON M.MEMBER_ID = A.MEMBER_ID WHERE M.MEMBER_ID = ?", memberID).fetchall()
    cDetails = cur.execute("SELECT C.CERTIFICATION_URL, C.CERTIFICATE_NAME FROM MEMBER M INNER JOIN CERTIFICATIONS C ON M.MEMBER_ID = C.MEMBER_ID WHERE M.MEMBER_ID = ?", memberID).fetchall()
    connection.commit()
    
    cur.close()
    return [bDetails, sDetails, hDetails, jDetails, pDetails, skDetails, aDetails, cDetails]

def displayDetails(memberID):
    bDetails, sDetails, hDetails, jDetails, pDetails, skDetails, aDetails, cDetails = queryResults(memberID)
    
    print("Basic details ->\n")
    bFormat = "Name: {}\nBio: {}\nAddress: {}\nPhone: {}\nEmail: {}\nGitHub: {}\nLinkedIn: {}\n"
    for i in bDetails:
        print(bFormat.format(*i))

    print("Schooling details ->\n")
    sFormat = "School Name: {}\nLocation: {}\nGrade: {}\nYear of Graduation: {}\nStream: {}\nPercentage: {}%\n"
    for i in sDetails:
        print(sFormat.format(*i))

    print("Higher education details ->\n")
    higher_edFormat = "Degree: {}\nMajor: {}\nUniversity: {}\nGPA: {}\n"
    for i in hDetails:
        print(higher_edFormat.format(*i))

    print("Job details ->\n")
    jobFormat = "Employer: {}\nLocation: {}\nJob Title: {}\nJob Description: {}\nJob Duration: {} years\n"
    for i in jDetails:
        print(jobFormat.format(*i))

    print("Project details ->\n")
    projectFormat = "Project Name: {}\nProject Description: {}\n"
    for i in pDetails:
        print(projectFormat.format(*i))

    print("Skills details ->\n")
    skillFormat = "Skill: {} :: Expertise: {}"
    for i in skDetails:
        print(skillFormat.format(*i))

    print("\nAccomplishments details ->\n")
    accFormat = "Accomplishment name: {}\nDescription: {}\n"
    for i in aDetails:
        print(accFormat.format(*i))

    print("Certifiction details ->\n")
    cFormat = "Certification ID: {} :: Certification: {}\n"
    for i in cDetails:
        print(cFormat.format(*i))

def clientInfo(memberID):
    bDetails, sDetails, hDetails, jDetails, pDetails, skDetails, aDetails, cDetails = queryResults(memberID)
    name, bio, address, phone, email, github, linkedin = bDetails[0][0], bDetails[0][1], bDetails[0][2], bDetails[0][3], bDetails[0][4], bDetails[0][5], bDetails[0][6]
    if address is None:
        address = ""
    if bio is None:
        bio = ""
    if github is None:
        github = ""
    if linkedin is None:
        linkedin = ""
    web = github+'\n'+linkedin
    return {"name" : name, "bio" : bio, "address" : address, "phone" : phone, "email" : email, "web_info": web, "schooling" : sDetails, "higherEducation" : hDetails, "jobs" : jDetails, "projects" : pDetails, "skills" : skDetails, "accomplishments" : aDetails, "certifications" : cDetails}
    
def registerAccount():
    memberID = createMember()
    print("\nYour username is {}!\n".format(memberID))
    schooling(memberID)
    print()
    higherEducation(memberID)
    print()
    skills(memberID)
    print()
    projects(memberID)
    print()
    experience(memberID)
    print()
    accomplishments(memberID)
    print()
    certifications(memberID)
    print()
    return memberID

def structureDetails(items):
    schooling = ""
    higher_ed = ""
    experience = ""
    experience = ""
    projects = ""
    skills = ""
    accomplishments = ""
    certifications = ""

    school_format = "{}, {}\n{}th Board Examinations {}\n{}, Percentage: {}%\n\n"
    higher_ed_format = "{}\n{} {}\nCGPA: {}\n\n"
    exp_format = "{} - {}, {}\n{} - {} years\n\n"
    project_format = "{}\n{}\n\n"
    skill_format = "{}\n"
    accomplish_format = "{}\n{}\n\n"
    certification_format = "{}\n"

    for i in items["schooling"][::-1]:
        schooling += school_format.format(*i)
    schooling = schooling.strip()

    for i in items["higherEducation"][::-1]:
        higher_ed += higher_ed_format.format(i[2], i[0], i[1], i[3])
    higher_ed = higher_ed.strip()

    for i in items["jobs"][::-1]:
        experience += exp_format.format(i[2], i[0], i[1], i[3], i[4])
    experience = experience.strip()

    for i in items["projects"]:
        projects += project_format.format(*i)
    projects = projects.strip()

    for i in items["skills"][::-1]:
        skills += skill_format.format(i[0])
    skills = skills.strip()

    for i in items["accomplishments"][::-1]:
        accomplishments += accomplish_format.format(*i)
    accomplishments = accomplishments.strip()

    for i in items["certifications"][::-1]:
        certifications += certification_format.format(i[1])
    certifications = certifications.strip()

    resume_values = {"name" : items["name"],
        "bio" : items["bio"],
        "address" : items["address"],
        "phone" : items["phone"],
        "email" : items["email"],
        "experience" : experience,
        "websites" : items["web_info"],
        "education" : higher_ed + '\n\n' + schooling,
        "projects" : projects,
        "skills" : skills,
        "certifications" : certifications,
        "accomplishments" : accomplishments}

    return resume_values

def editDetails(memberID):
    print("Your current details are:")
    displayDetails(memberID)
    print("1. Name")
    print("2. Password")
    print("3. Email")
    print("4. Phone")
    print("5. Address")
    print("6. Bio")
    print("7. GitHub")
    print("8. LinkedIn")
    print("9. School Details")
    print("10. Higher Education")
    print("11. Skills")
    print("12. Projects")
    print("13. Experience")
    print("14. Accomplishments")
    print("15. Certifications")
    ch = int(input("\nEnter choice: "))
    if ch not in list(range(1,16)):
        print("Invalid choice!")
        return
    else:
        cur = connection.cursor()
        if ch == 1:
            name = input("Name : ")
            while not all(x.isalpha() or x == "" or x == " " for x in name):
                print("Invalid format. Please enter a valid name.")
                name = input("Name : ")
            new = name
            confirm = input("Confirm change? [y/n]: ")
            if confirm.upper()=='Y':
                cur.execute("UPDATE MEMBER SET NAME = ? WHERE MEMBER_ID = ?", (new,memberID))
                connection.commit()
                cur.close()
                print("Detail updated!")
            else:
                return
        elif ch == 2:
            password = input("Password (At least 8 characters long) : ")
            while len(password) < 8:
                print("Invalid format. Password has to be atleast 8 characters long.")
                password = input("Password: ")
            new = password
            confirm = input("Confirm change? [y/n]: ")
            if confirm.upper()=='Y':
                cur.execute("UPDATE MEMBER SET PASSWORD = ? WHERE MEMBER_ID = ?", (new,memberID))
                connection.commit()
                cur.close()
                print("Detail updated!")
            else:
                return
        elif ch == 3:
            email = input("Email ID : ")
            pattern = r'^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
            while not(re.search(pattern, email)):
                print("Invalid format. Please enter a valid email address.")
                email = input("Email ID : ")
            new = email
            confirm = input("Confirm change? [y/n]: ")
            if confirm.upper()=='Y':
                cur.execute("UPDATE MEMBER SET EMAIL = ? WHERE MEMBER_ID = ?", (new,memberID))
                connection.commit()
                cur.close()
                print("Detail updated!")
            else:
                return
        elif ch == 4:
            phone = input("Phone : ")
            while not(phone.isdigit() and len(phone) == 10):
                print("Invalid format. Please enter valid 10 digit phone number.")
                phone = input("Phone : ")
            new = phone
            confirm = input("Confirm change? [y/n]: ")
            if confirm.upper()=='Y':
                cur.execute("UPDATE MEMBER SET PHONE = ? WHERE MEMBER_ID = ?", (new,memberID))
                connection.commit()
                cur.close()
                print("Detail updated!")
            else:
                return
        elif ch == 5:
            address = input("Residential Address or NA: ")
            if address.upper() == 'NA':
                address = None
            new = address
            confirm = input("Confirm change? [y/n]: ")
            if confirm.upper()=='Y':
                cur.execute("UPDATE MEMBER SET ADDRESS = ? WHERE MEMBER_ID = ?", (new,memberID))
                connection.commit()
                cur.close()
                print("Detail updated!")
            else:
                return
        elif ch == 6:
            bio = input("Enter bio or NA: ")
            if bio.upper() == 'NA':
                bio = None
            new = bio
            confirm = input("Confirm change? [y/n]: ")
            if confirm.upper()=='Y':
                cur.execute("UPDATE MEMBER SET BIO = ? WHERE MEMBER_ID = ?", (new,memberID))
                connection.commit()
                cur.close()
                print("Detail updated!")
            else:
                return
        elif ch == 7:
            gitHub = input("Enter Github URL or NA: ")
            if gitHub.upper() == 'NA':
                gitHub = None
            new = gitHub
            confirm = input("Confirm change? [y/n]: ")
            if confirm.upper()=='Y':
                cur.execute("UPDATE MEMBER SET GITHUB = ? WHERE MEMBER_ID = ?", (new,memberID))
                connection.commit()
                cur.close()
                print("Detail updated!")
            else:
                return
        elif ch == 8:
            linkedIn = input("Enter LinkedIn URL or NA: ")
            if linkedIn.upper() == 'NA':
                linkedIn = None
            new = linkedIn
            confirm = input("Confirm change? [y/n]: ")
            if confirm.upper()=='Y':
                cur.execute("UPDATE MEMBER SET LINKEDIN = ? WHERE MEMBER_ID = ?", (new,memberID))
                connection.commit()
                cur.close()
                print("Detail updated!")
            else:
                return
        elif ch == 9:
            confirm = input("Confirm change? [y/n]: ")
            if confirm.upper()=='Y':
                cur.execute("DELETE FROM SCHOOLING WHERE MEMBER_ID = ?", (memberID))
                connection.commit()
                schooling(memberID)
                cur.close()
                print("Detail updated!")
            else:
                return
        elif ch == 10:
            confirm = input("Confirm change? [y/n]: ")
            if confirm.upper()=='Y':
                cur.execute("DELETE FROM HIGHER_EDUCATION WHERE MEMBER_ID = ?", (memberID))
                connection.commit()
                higherEducation(memberID)
                cur.close()
                print("Detail updated!")
            else:
                return
        elif ch == 11:
            confirm = input("Confirm change? [y/n]: ")
            if confirm.upper()=='Y':
                cur.execute("DELETE FROM SKILLS WHERE MEMBER_ID = ?", (memberID))
                connection.commit()
                skills(memberID)
                cur.close()
                print("Detail updated!")
            else:
                return
        elif ch == 12:
            confirm = input("Confirm change? [y/n]: ")
            if confirm.upper()=='Y':
                cur.execute("DELETE FROM PROJECTS WHERE MEMBER_ID = ?", (memberID))
                connection.commit()
                projects(memberID)
                cur.close()
                print("Detail updated!")
            else:
                return
        elif ch == 13:
            confirm = input("Confirm change? [y/n]: ")
            if confirm.upper()=='Y':
                cur.execute("DELETE FROM EXPERIENCE WHERE MEMBER_ID = ?", (memberID))
                connection.commit()
                experience(memberID)
                cur.close()
                print("Detail updated!")
            else:
                return
        elif ch == 14:
            confirm = input("Confirm change? [y/n]: ")
            if confirm.upper()=='Y':
                cur.execute("DELETE FROM ACCOMPLISHMENTS WHERE MEMBER_ID = ?", (memberID))
                connection.commit()
                accomplishments(memberID)
                cur.close()
                print("Detail updated!")
            else:
                return
        elif ch == 15:
            confirm = input("Confirm change? [y/n]: ")
            if confirm.upper()=='Y':
                cur.execute("DELETE FROM CERTIFICATIONS WHERE MEMBER_ID = ?", (memberID))
                connection.commit()
                certifications(memberID)
                cur.close()
                print("Detail updated!")
            else:
                return
        else:
            return
        return