import sqlite3
conn = sqlite3.connect('b_users.sqlite')
cur = conn.cursor()
cur.execute("""
CREATE TABLE IF NOT EXISTS Users(
TG_ID INTEGER ,
F_Name STRING ,
Phone_Num INTEGER,
BDATE STRING,
Litsey STRING,
INST STRING,
EDU STRING,
EDU_PLACE STRING,
L_JOB STRING,
DOM STRING,
L_DOM STRING,
EDU_LANG STRING,
FILIAL STRING,
NEWJOB STRING,
WORKTIME STRING,
SALARY STRING,
OQI STRING,
QQ STRING,
BB STRING,
TT STRING,
Lang INTEGER ,
Stage INTEGER

)
""")
first_insert = """
INSERT INTO Users VALUES ("{}", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "{}" )
"""

upd_TT = """
UPDATE Users 
SET TT = "{}" 
WHERE TG_ID = "{}"
"""
select_TT = """
SELECT TT
From Users
WHERE TG_ID = "{}"
"""

upd_BB = """
UPDATE Users 
SET BB = "{}" 
WHERE TG_ID = "{}"
"""
select_BB = """
SELECT BB
From Users
WHERE TG_ID = "{}"
"""


upd_QQ = """
UPDATE Users 
SET QQ = "{}" 
WHERE TG_ID = "{}"
"""
select_QQ = """
SELECT QQ
From Users
WHERE TG_ID = "{}"
"""

upd_OQI = """
UPDATE Users 
SET OQI = "{}" 
WHERE TG_ID = "{}"
"""
select_OQI = """
SELECT OQI
From Users
WHERE TG_ID = "{}"
"""

upd_INST = """
UPDATE Users 
SET INST = "{}" 
WHERE TG_ID = "{}"
"""
select_INST = """
SELECT INST
From Users
WHERE TG_ID = "{}"
"""

upd_Litsey = """
UPDATE Users 
SET Litsey = "{}" 
WHERE TG_ID = "{}"
"""
select_Litsey = """
SELECT Litsey
From Users
WHERE TG_ID = "{}"
"""


upd_LJOB = """
UPDATE Users 
SET L_JOB = "{}" 
WHERE TG_ID = "{}"
"""
select_LJOB = """
SELECT L_JOB
From Users
WHERE TG_ID = "{}"
"""

upd_DOM = """
UPDATE Users 
SET DOM = "{}" 
WHERE TG_ID = "{}"
"""
select_DOM = """
SELECT DOM
From Users
WHERE TG_ID = "{}"
"""

upd_L_DOM = """
UPDATE Users 
SET L_DOM = "{}" 
WHERE TG_ID = "{}"
"""
select_L_DOM = """
SELECT L_DOM
From Users
WHERE TG_ID = "{}"
"""

upd_EDU_LANG = """
UPDATE Users 
SET EDU_LANG = "{}" 
WHERE TG_ID = "{}"
"""
select_EDU_LANG = """
SELECT EDU_LANG
From Users
WHERE TG_ID = "{}"
"""

upd_FILIAL = """
UPDATE Users 
SET FILIAL = "{}" 
WHERE TG_ID = "{}"
"""
select_FILIAL = """
SELECT FILIAL
From Users
WHERE TG_ID = "{}"
"""

upd_NEWJOB = """
UPDATE Users 
SET NEWJOB = "{}" 
WHERE TG_ID = "{}"
"""
select_NEWJOB = """
SELECT NEWJOB
From Users
WHERE TG_ID = "{}"
"""

upd_WORKTIME = """
UPDATE Users 
SET WORKTIME = "{}" 
WHERE TG_ID = "{}"
"""
select_WORKTIME = """
SELECT WORKTIME
From Users
WHERE TG_ID = "{}"
"""

upd_SALARY = """
UPDATE Users 
SET SALARY = "{}" 
WHERE TG_ID = "{}"
"""
select_SALARY = """
SELECT SALARY 
From Users
WHERE TG_ID = "{}"
"""

upd_EDU = """
UPDATE Users 
SET EDU = "{}" 
WHERE TG_ID = "{}"
"""
select_EDU = """
SELECT EDU
From Users
WHERE TG_ID = "{}"
"""

select_EDU_PLACE = """
SELECT EDU_PLACE
From Users
WHERE TG_ID = "{}"
"""
upd_EDU_PLACE = """
UPDATE Users 
SET EDU_PLACE = "{}" 
WHERE TG_ID = "{}"
"""
select_BDATE= """
SELECT BDATE
From Users
WHERE TG_ID = "{}"
"""
upd_BDATE = """
UPDATE Users 
SET BDATE = "{}" 
WHERE TG_ID = "{}"
"""
select_BDATE = """
SELECT BDATE
From Users
WHERE TG_ID = "{}"
"""


upd_DOM = """
UPDATE Users 
SET DOM = "{}" 
WHERE TG_ID = "{}"
"""
select_DOM = """
SELECT DOM
From Users
WHERE TG_ID = "{}"
"""



get_id = """
SELECT TG_ID 
FROM Users
Where TG_ID = "{}"
"""
upd_name = """
UPDATE Users 
SET F_Name = "{}" 
WHERE TG_ID = "{}"
"""
select_name = """
SELECT F_Name
From Users
WHERE TG_ID = "{}"
"""

update_phone_num = """
UPDATE Users 
SET Phone_Num = "{}"
WHERE TG_ID = "{}"
"""
select_num = """
SELECT Phone_Num 
FROM Users
WHERE TG_ID = "{}"
"""


lang = """
UPDATE Users
SET lang = "{}"
WHERE TG_ID = "{}"
"""
lang_select = """
SELECT Lang
FROM Users
WHERE TG_ID = "{}"
"""

stagee = """
UPDATE Users
SET Stage = "{}"
WHERE TG_ID = "{}"
"""
stage = """
SELECT Stage
FROM Users
WHERE TG_ID = "{}"
"""

conn.commit()