import random
from datetime import date
import pyodbc
import string

connection = pyodbc.connect('Driver={SQL Server};'
                      'Server=LAPTOP-HOLIG319;'
                      'Database=DBMS;'
                      'Trusted_Connection=yes;'
                      'MARS_Connection = YES;')
print("Connection made!")

last = ['Atwal', 'Mittal', 'Acharya', 'Bhatnagar', 'Kumar', 'Chand', 'Narayan', 'Som', 'Ganesan', 'Manne', 'Chaudry', 'Andra', 'Borra', 'Dutta', 'Bajaj', 'Nori', 'Choudhry', 'Guha', 'Kulkarni', 'Saini', 'Meda', 'Mandal', 'Nath', 'Sathe', 'Ben', 'Parmer', 'Maharaj', 'Mammen', 'Sandal', 'Dube', 'Goel', 'Patil', 'Walia', 'Prashad', 'Sachdeva', 'Tank', 'Vora', 'Devan', 'Verma', 'Lall', 'Loke', 'Rau', 'Basu', 'Sridhar', 'Jha', 'Rout', 'Shroff', 'Konda', 'Parmar', 'Kalita', 'Arora', 'Chopra', 'Mehra', 'Viswanathan', 'Khatri', 'Sethi', 'Mani', 'Varughese', 'Grover', 'Sem', 'Behl', 'Talwar', 'Bose', 'Ganesh', 'Basak', 'Sarma', 'Chawla', 'Das', 'Kade', 'Korpal', 'Randhawa', 'Sandhu', 'Ray', 'Mann', 'Venkataraman', 'Bava', 'Buch', 'Chada', 'Gokhale', 'Baria', 'Datta', 'Bal', 'Menon', 'Shan', 'Yogi', 'Mital', 'Chacko', 'Samra', 'Soman', 'Ravi', 'Brahmbhatt', 'Lanka', 'Tailor', 'Seth', 'Ramakrishnan', 'Oza', 'Dhaliwal', 'Goyal', 'Mohanty', 'Bahl', 'Sachar', 'Radhakrishnan', 'Karpe', 'Pant', 'Babu', 'Banerjee', 'Bakshi', 'Prasad', 'Pillai', 'Sengupta', 'Mand', 'Arya', 'Suri', 'Wagle', 'Thaman', 'Handa', 'Mehta', 'Ratta', 'Agrawal', 'Kadakia', 'Grewal', 'Kapur', 'Dar', 'Chandra', 'Bhasin', 'Pandit', 'Chakrabarti', 'Deshpande', 'Loyal', 'Ganguly', 'Khare', 'Din', 'Pau', 'Naidu', 'Gupta', 'Cheema', 'Sagar', 'Dugar', 'Swaminathan', 'Pai', 'Tak', 'Lata', 'Padmanabhan', 'Pandya', 'Dasgupta', 'Saran', 'Sarkar', 'Dhillon', 'Nagar', 'Iyengar', 'Goswami', 'Vaidya', 'Mehan', 'Jain', 'Shenoy', 'Mitter', 'Issac', 'Deol', 'Tata', 'Kapadia', 'Hegde', 'Naik', 'Mukhopadhyay', 'Murty', 'Raju', 'Aurora', 'Chokshi', 'Anand', 'Prabhakar', 'Bhatti', 'Swamy', 'De', 'Jayaraman', 'Dora', 'Mane', 'Krishnamurthy', 'Dyal', 'Bhattacharyya', 'Virk', 'Karan', 'Mall', 'Nazareth', 'Bains', 'Khurana', 'Shah', 'Gole', 'Memon', 'Wali', 'Balan', 'Yadav', 'Kothari', 'Seshadri', 'Doshi', 'Nagy', 'Prabhu', 'Joshi', 'Mahal', 'Jani', 'Thakkar', 'Devi', 'Gala', 'Sarraf', 'Malhotra', 'Magar', 'Bhardwaj', 'Ramachandran', 'Mander', 'Zachariah', 'Pal', 'Varma', 'Sidhu', 'Panchal', 'Kumer', 'Divan', 'Saha', 'Sule', 'Puri', 'Singh', 'Prakash', 'Sahota', 'Rajan', 'Raval', 'Khosla', 'Deshmukh', 'Subramaniam', 'Apte', 'Biswas', 'Kapoor', 'Rattan', 'Dewan', 'Nair', 'Solanki', 'Chatterjee', 'Mangat', 'Dua', 'Ghose', 'Gade', 'Badami', 'Nagarajan', 'Rastogi', 'Pathak', 'Ramanathan', 'Golla', 'Garde', 'Batra', 'Kuruvilla', 'Ramesh', 'Bansal', 'Parekh', 'Goda', 'Dhawan', 'Saraf', 'Taneja', 'Lal', 'Tripathi', 'Rana', 'Sheth', 'Chaudhry', 'Singhal', 'Savant', 'Peri', 'Rege', 'Hari', 'Parikh', 'Hayer', 'Pingle', 'Bahri', 'Chahal', 'Varkey', 'Gill', 'Vyas', 'Vohra', 'Agate', 'Tiwari', 'Kant', 'Nigam', 'Nanda', 'Trivedi', 'Balakrishnan', 'Mahajan', 'Mishra', 'Bhalla', 'Narain', 'Srinivasan', 'Hora', 'Ramaswamy', 'Kaul', 'Sama', 'Mangal', 'Madan', 'Cherian', 'Matthai', 'Jaggi', 'Dubey', 'Gour', 'Chana', 'Edwin', 'Anne', 'Kala', 'Uppal', 'Bandi', 'Choudhary', 'Modi', 'More', 'Gopal', 'Wadhwa', 'Rajagopalan', 'Pradhan', 'Nayak', 'Kohli', 'Sampath', 'Mannan', 'Kamdar', 'Mohan', 'Chadha', 'Salvi', 'Setty', 'Bhat', 'Dani', 'Ahuja', 'Gola', 'Gulati', 'Minhas', 'Boase', 'Mehrotra', 'Yohannan', 'Krishna', 'Sankaran', 'Deep', 'Dada', 'Balay', 'Sami', 'Vasa', 'Sen', 'Chaudhuri', 'Rama', 'Luthra', 'Chandran', 'Bath', 'Sood', 'Bhatia', 'Chad', 'Meka', 'Garg', 'Khalsa', 'Aggarwal', 'Manda', 'Bawa', 'Om', 'Barman', 'Varty', 'Dave', 'Natarajan', 'Sha', 'Lala', 'Bhavsar', 'Johal', 'Shukla', 'Chaudhari', 'Kar', 'Palla', 'Mathai', 'Bir', 'Bhandari', 'Agarwal', 'Comar', 'Krishnan', 'Bora', 'Narang', 'Bobal', 'Chander', 'Kata', 'Chhabra', 'Thaker', 'Gara', 'Balasubramanian', 'Raja', 'Mallick', 'Patla', 'Oak', 'Karnik', 'Doctor', 'Pall', 'Chowdhury', 'Sahni', 'Suresh', 'Banik', 'Gaba', 'Choudhury', 'Murthy', 'Badal', 'Saxena', 'Thakur', 'Amble', 'Kurian', 'Srivastava', 'Hayre', 'Mukherjee', 'Dugal', 'Dutt', 'Parsa', 'Dixit', 'Sankar', 'Gera', 'Desai', 'Zacharia', 'Sanghvi', 'Dhar', 'Roy', 'Ahluwalia', 'Sarin', 'Bali', 'Sharma', 'Tandon', 'Date', 'Ranganathan', 'Narula', 'Vala', 'Hans', 'Sekhon', 'Raj', 'Sastry', 'Mutti', 'Bhatt', 'Kannan', 'Dhingra', 'Chaudhary', 'Pandey', 'Rai', 'Sodhi', 'Natt', 'Khanna', 'Bumb', 'Ram', 'Chauhan', 'Shankar', 'Lalla', 'Shanker', 'Purohit', 'Muni', 'Nayar', 'Pillay', 'Wable', 'Barad', 'Bhargava', 'Dara', 'Borah', 'Shere', 'Char', 'Krish', 'Chakraborty', 'Upadhyay', 'Dass', 'Shetty', 'Gandhi', 'Tella', 'Kunda', 'Venkatesh', 'Rao', 'Sibal', 'Srinivas', 'Sangha', 'Sabharwal', 'Kari', 'Nadkarni', 'Deo', 'Varghese', 'Dash', 'Sachdev', 'Dayal', 'Mathur', 'Dey', 'Sinha', 'Patel', 'Sarna', 'Sehgal', 'Sundaram', 'Borde', 'Sura', 'Keer', 'Kakar', 'Jhaveri', 'Sani', 'Bhakta', 'Wason', 'Morar', 'Bhagat', 'Sunder', 'Merchant', 'Narasimhan', 'Bail', 'Batta', 'Mitra', 'Kale', 'Brar', 'Kaur', 'Koshy', 'Vig', 'Rajagopal', 'Subramanian', 'Sant', 'Dalal', 'Munshi', 'Sur', 'Bajwa', 'Kanda', 'Toor', 'Nadig', 'Sawhney', 'Iyer', 'Chanda', 'Kara', 'Bera', 'Walla', 'Majumdar', 'Ghosh', 'Sane', 'Mistry', 'Raman', 'Kibe', 'Bala', 'Lad', 'Kalla', 'Soni', 'Sharaf', 'Tara', 'Kashyap', 'Bedi', 'Mody', 'Narayanan', 'Ratti', 'Nagi', 'Halder', 'Bassi', 'Warrior', 'Butala', 'Raghavan', 'Ravel', 'Kota', 'Oommen', 'Palan', 'Reddy', 'Misra']
first = ['Shivani', 'Hem', 'Bhuv', 'Sadhil', 'Mahika', 'Anaisha', 'Kevin', 'Vinay', 'Mehar', 'Jay', 'Lavanya', 'Diya', 'Sanjana', 'Meher', 'Aaradhya', 'Ranbir', 'Rishit', 'Raj', 'Mansi', 'Krisha', 'Harini', 'Lopamudra', 'Indrani', 'Zoya', 'Jaideep', 'Aditi', 'Naagesh', 'Drishti', 'Nimit', 'Jyothsna', 'Rebecca', 'Pooja', 'Jayanti', 'Yashwant', 'Mridul', 'Nehrika', 'Atiksh', 'Joseph', 'Asmee', 'Gurdeep', 'Lalit', 'Rudra', 'Uma', 'Parv', 'Sarah', 'Kavya', 'Tanvi', 'Alisha', 'Aditya', 'Samir', 'Ashish', 'Pranav', 'Kashvi', 'Karun', 'Farha', 'Shridevi', 'Ishita', 'Rushil', 'Vaishnavi', 'Bipasha', 'Viti', 'Pahal', 'Yug', 'Daljeet', 'Ishank', 'Ruchika', 'Nirav', 'Shweta', 'Shrishti', 'Pranay', 'Akshat', 'Aahva', 'Uttam', 'Girish', 'Falguni', 'Sanchit', 'Zara', 'Kimaya', 'Jeet', 'Ishranth', 'Gaurav', 'Anjali', 'Aruna', 'Varun', 'Sandeep', 'Kahaan', 'Rohan', 'Sparsh', 'Aarav', 'Bhavna', 'Tara', 'Mayra', 'Reyansh', 'Kairav', 'Anant', 'Ved', 'Nilaksh', 'Siddharth', 'Om', 'Geetha', 'Anubhav', 'Kshitij', 'Dilip', 'Ekta', 'Rachit', 'Ishana', 'Kabir', 'Neysa', 'Manvik', 'Bhagyashree', 'Hiya', 'Saloni', 'Ritesh', 'Aishwarya', 'Chiranjeev', 'Rajiv', 'Tushar', 'Gian', 'Taara', 'Pavati', 'Sneha', 'Chaaya', 'Adhira', 'Sachin', 'Bhaskar', 'Gayatri', 'Prisha', 'Rishaan', 'Aadiv', 'Aparna', 'Alex', 'Raunak', 'Shreya', 'Maya', 'Amoli', 'Leela', 'Mirai', 'Sai', 'Jash', 'Vikas', 'Avni', 'Pavan', 'Vipul', 'Lathika', 'Urvashi', 'Taahira', 'Taksh', 'Kaia', 'Shanaya', 'Larisa', 'Zuber', 'Sanjay', 'Jhanvi', 'Luv', 'Chhavi', 'Gautam', 'Eesha', 'Naksh', 'Vivaan', 'Meera', 'Taarush', 'Upasna', 'Dasya', 'Sahana', 'Yash', 'Mishka', 'Bikram', 'Parth', 'Naitee', 'Ananya', 'Anushka', 'Adah', 'Manan', 'Vihaan', 'Tarun', 'Navya', 'Jagan', 'Ayaan', 'Ryka', 'Anika', 'Deepika', 'Akanksh', 'Garima', 'Carina', 'Arjun', 'Udit', 'Sarthak', 'Keya', 'Saanvi', 'Laksh', 'Ira', 'Indiresh', 'Kanika', 'Naishadh', 'Mohammad', 'Idhant', 'Saisha', 'Chetas', 'Nargis']

emailyear = [str(i).zfill(2) for i in range(1,100)]
emaildomains = ["@yahoo.com","@gmail.com","@gmail.com","@gmail.com","@gmail.com"]
emailtype = lambda x:[x.split()[0]+x.split()[-1]+random.choice(emailyear)+random.choice(emaildomains),
            x.split()[0]+random.choice(emailyear)+random.choice(emaildomains),
            x.split()[-1]+random.choice(emailyear)+random.choice(emaildomains),
            x.split()[0][0]+x.split()[-1][0]+random.choice(emailyear)+random.choice(emaildomains)]

profile = lambda x: [x.split()[0]+x.split()[1],x.split()[0]+x.split()[0][-1]*random.randrange(1,5),x.split()[1]+x.split()[1][-1]*random.randint(1,5),
                x.split()[0]+x.split()[1]+str(random.randint(100,999))]

cur = connection.cursor()

uni = ["PES University", "RV College of Engineering", "MSRIT",
        "MS Ramaiah Institute of Technology", "DSCE", "BMS College of Engineering","RVCE","PESU", "IIT Bombay","Amrita College of Engineering",
        "BMSIT", "VIT Vellore","Dayananda Sagar College of Engineering","BITS Pilani","BITS Pilani Hyderabad","BITS Pilani Goa",
        "NIT Dharwad","NITK","NIT Surathkal","IIT Delhi","IIT Ropar","SRMIT","SRM Institute of Technology","VIT Chennai","MIT",
        "Manipal Insitute of Technology"]

schools = {"Bishop Cotton Girls' School":["Residency Road"], "New Horizon Public School":["Indiranagar"],"St Josephs":["Residency Road"],
            "DPS":["Whitefiled", "Electronic City", "Malleswaram"],"National Public School":["Indiranagar","Rajajinagar","Koramangala","Yeshwanthpur","HSR",
            "Jayanagar"],"Baldwin Boys' High School":["Richmond Road"], "Baldwin Girls' High School":["Richmond Road"], "Sishu Griha":["Thippasandra"],
            "NCFE":["Jeevanbhimanagar","CV Raman Nagar"],"Cathedral High School":["Residency Road"],"Air Force School":["Old Airport Road"],"CMR PU":["Kalyan Nagar"],
            "RCIS":["Kalyan Nagar"],"HAL Public School":["Old Airport Road"],"Army Public School":["Residency Road","Richmond Road"]}


degreesB = {"BTech":["ECE","EEE","CV","MECH","BT","CHEM","METALLURGICAL"], 
            "BSc":["Math","Physics","Chemistry","Statistics","Political Science","Computer Science"],
            "BBA":["BA"],
            "LLB":["Law","Business"],
            "BE":["ECE","EEE","CV","MECH","BT","CHEM","METALLURGICAL","IT","Networking"],
            "BCom":["Commerce","CA","Business"],
            "BDes":["Product Design","UI Design","Industrial Design"],
            "BA":["Arts","Humanities","Science"]}
degreesM = {"MTech":["ECE","EEE","CV","MECH","BT","CHEM","METALLURGICAL"], 
            "MS":["Math","Physics","Chemistry","Statistics","Political Science","Computer Science"],
            "MPhil":["Math","Physics","Chemistry","Statistics","Political Science","Computer Science"],
            "MBA":["BA"]}
degreesD = {"PhD":["Computer Science","Machine Learning","Mathematics","Science","Quantum Mechanics","Math","Physics","Chemistry","Statistics","Political Science",
                    "BA","Commerce, CA","Business","Arts","Humanities","Science"]}
            
degrees = {"Bachelor's": degreesB,"Master's":degreesM,"Doctorate":degreesD}

loc = ["Bangalore","Mumbai","New Delhi","Kolkata","Lucknow","Chennai","Hyderabad","Pune","Allahabad"]
jtitles = ["Regional Manager","HR","Marketing Strategist","SWE","Summer Intern","Research Intern","Consultant","Data Analyst","SDE"]
employers = ["Google","Microsoft","Apple","Intel","Amazon","Flipkart","Dunder Mifflin","Uber","Facebook"]

skills = ["Python","C","C++","Java","R","Ruby","Rust","Android App Dev","iOS App Dev","HTML/CSS","PHP","Machine Learning","Deep Learning","NLP",
        "Django","Flask","Node.js","Javascript","Bootstrap","UNIX","MATLAB","Octave","Computer Vision","Julia","Debate","Public Speaking","Art",
        "Painting","Reading","Data Science","Data Analysis","Database","Seetching","Fine Art","Acrylic Art","Oil Paints","Literature","Content Writing"]


# INSERT SCHOOL INFO
'''
schoolList = cur.execute("SELECT SCHOOL_ID FROM SCHOOL").fetchall()
if schoolList == []:
    start = 1
else:
    mList = [i[0] for i in schoolList]
    start = int(max(mList)[4:10]) + 1
for sch in schools:
    for loc in schools[sch]:
        schID = "SCH#" + str(start).zfill(6)
        start+=1
        t = (schID,loc,sch)
        cur.execute("INSERT INTO SCHOOL VALUES (?, ?, ?)", t)
        connection.commit()
'''

# ADD DEGREES
'''
dList = cur.execute("SELECT DEGREE_ID FROM DEGREE_INFO").fetchall()
if dList == []:
    start = 1
else:
    mList = [i[0] for i in dList]
    start = int(max(mList)[4:10]) + 1

for dtype in degrees:
    for deg in degrees[dtype]:
        for major in degrees[dtype][deg]:
            dID = "DEG#" + str(start).zfill(6)
            start+=1
            t = (dID,dtype.upper(),deg.upper(),major.upper())
            cur.execute("INSERT INTO DEGREE_INFO VALUES (?, ?, ?, ?)", t)
            connection.commit()
'''

# ADD JOBS

'''
jList = cur.execute("SELECT JOB_ID FROM JOB").fetchall()
if jList == []:
    start = 1
else:
    mList = [i[0] for i in jList]
    start = int(max(mList)[4:10]) + 1

for comp in employers:
    for l in loc:
        for role in jtitles:
            jID = "JOB#" + str(start).zfill(6)
            start+=1
            t = (jID,role,l,None,comp)
            cur.execute("INSERT INTO JOB VALUES (?, ?, ?, ?, ?)", t)
            connection.commit()
'''


# ADD MEMBERS
'''
schoolList = [i[0] for i in cur.execute("SELECT SCHOOL_ID FROM SCHOOL").fetchall()]
dList = [i[0] for i in cur.execute("SELECT DEGREE_ID FROM DEGREE_INFO").fetchall()]
jList = [i[0] for i in cur.execute("SELECT JOB_ID FROM JOB").fetchall()]
memberList = cur.execute("SELECT MEMBER_ID FROM MEMBER").fetchall()

if memberList == []:
    start = 1
else:
    mList = [i[0] for i in memberList]
    start = int(max(mList)[4:10]) + 1

N = 5
for i in range(start,start+N+1):
    print(i)
    memberID = "MEM#" + str(i).zfill(6)
    password = "hello123"
    username = random.choice(first)+' '+random.choice(last)
    email = random.choice(emailtype(username))
    email = email.lower()
    contactnum = [str(random.randint(7,9)) for i in range(1,4)]
    contactnum.extend([str(random.randint(1,9)) for i in range(1,7)])
    number = "".join(contactnum)
    address = None
    if random.choice([0,1,1]):
        address = random.choice(["Bangalore","Kolkata","Chennai","Mumbai","New Delhi","Patna","Pune","Allahabad"])
    bio = None
    if random.choice([0,0,0,1,1]):
        bio = random.choice(["I'm lovin' it!","Automatically generated resumes are best!","Hardworking and sincere","Student","I am best","Hire me plis",
                            "BSN","Swag","Sonobois are best","Resume builder is amazing!","Looking for summer internships","Perfectionist","Hard worker",
                            "Diligent and Understanding","Creative, sharp and hard working","Sharp mind who is looking for a challenge."])
    git = None
    if random.choice([0,1]):
        git = random.choice(profile(username))
        git = git.lower()
    
    linkedin = None
    if random.choice([0,0,0,1,1]):
        linkedin = random.choice(profile(username))
        linkedin = linkedin.lower()

    t = (memberID,password,username,email,number,address,bio,git,linkedin)
    #print(t)
    cur.execute("INSERT INTO MEMBER VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", t)
    connection.commit()

    beg = 0
    for passlevel in [10,12]:
        if passlevel == 10:
            beg = random.randint(1990,2018)
        t = (memberID,random.choice(schoolList),passlevel,random.choice(["SCIENCE","COMMERCE","ARTS","HUMANITIES"]),beg,random.randint(80,100))
        beg+=2
        #print(t)
        cur.execute("INSERT INTO SCHOOLING VALUES (?,?,?,?,?,?)",t)
        connection.commit()

    ctr = 0
    count = random.randint(0,5)
    while ctr<count:
        ctr+=1
        t = (memberID,random.choice(dList),round(random.randrange(5,10),2),random.choice(uni))
        #print(t)
        try:
            cur.execute("INSERT INTO HIGHER_EDUCATION VALUES (?,?,?,?)",t)
            connection.commit()
            pass
        except:
            ctr-=1

    ctr = 0
    count = random.randint(0,8)
    while ctr<count:
        ctr+=1
        t = (memberID,random.choice(skills),random.randint(6,10))
        #print(t)
        try:
            cur.execute("INSERT INTO SKILLS VALUES (?,?,?)",t)
            connection.commit()
            pass
        except:
            ctr-=1

    ctr = 0
    count = random.randint(0,5)
    while ctr<count:
        ctr+=1
        t = (memberID,random.choice(skills)+' '+'Project',None)
        #print(t)
        try:
            cur.execute("INSERT INTO PROJECTS VALUES (?,?,?)",t)
            connection.commit()
            pass
        except:
            ctr-=1

    ctr = 0
    count = random.randint(0,5)
    
    while ctr<count:
        ctr+=1

        start_dt = date.today().replace(day=1, month=1, year=beg).toordinal()
        end_dt = date.today().toordinal()
        while True:
            try:
                startdate = date.fromordinal(random.randint(start_dt, end_dt)).strftime('%Y-%m-%d')
                break
            except:
                pass

        enddate = None
        if random.choice([0,1]):
            start_dt = date.today().replace(day=1, month=1, year=beg).toordinal()
            end_dt = date.today().toordinal()
            while True:
                try:
                    enddate = date.fromordinal(random.randint(start_dt, end_dt)).strftime('%Y-%m-%d')
                    break
                except:
                    pass

        t = (memberID,random.choice(jList),startdate,enddate)
        #print(t)
        try:
            cur.execute("INSERT INTO EXPERIENCE VALUES (?,?,?,?)",t)
            connection.commit()
            pass
        except:
            ctr-=1

    ctr = 0
    count = random.randint(0,10)
    while ctr<count:
        ctr+=1
        t = (memberID,"".join([random.choice(string.ascii_letters+string.digits) for j in range(20)]),random.choice(skills))
        #print(t)
        try:
            cur.execute("INSERT INTO CERTIFICATIONS VALUES (?,?,?)",t)
            connection.commit()
            pass
        except:
            ctr-=1
'''

    
    







