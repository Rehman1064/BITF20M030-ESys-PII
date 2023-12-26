from Interest import Interest
import pymysql
from collections import Counter
class SMDBHandler:
    def __init__(self,host,user,password,database):
        self.host=host
        self.user = user
        self.password=password
        self.database=database
    def ins(self,uname,passwd):
        mydb = None
        mydbCursor = None
        login = False
        try:
            mydb = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            mydbCursor = mydb.cursor()
        
            sql = "INSERT INTO users(username, password) VALUES (%s,%s)"
            arg = (uname,passwd)
            mydbCursor.execute(sql, arg)
            
            mydb.commit()
            login = True
        except Exception as e:
            print(str(e))
        finally:
            if mydbCursor is not None:
                mydbCursor.close()

            if mydb is not None:
                mydb.close()
            print(login)
            return login
    def check(self, uname, password):

        mydb = None
        mydbCursor = None
    
        try:
            mydb = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            mydbCursor = mydb.cursor()

        # Check if the user exists and authentication is successful
            auth_query = "SELECT * FROM users WHERE username = %s AND password = %s"
            auth_args = (uname, password)
            mydbCursor.execute(auth_query, auth_args)
            user = mydbCursor.fetchone()

            if user:
            # User authenticated, return True
                return True
            else:
            # User not found or authentication failed, return False
                return False

        except Exception as e:
            print(str(e))
            return False

        finally:
            if mydbCursor is not None:
                mydbCursor.close()

            if mydb is not None:
                mydb.close()


    def addInterest(self, obj):
        mydb = None
        mydbCursor = None
        login = False
        try:
            mydb = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            mydbCursor = mydb.cursor()
        
            sql = "INSERT INTO interest(RollNo, Name, Email, Gender, Dob, City, Interest, Department, Degree, Subject, StartDate, EndDate) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            arg = (obj.RollNo, obj.Name, obj.Email, obj.Gender, obj.Dob, obj.City, obj.Interest, obj.Department, obj.Degree, obj.Subject, obj.StartDate, obj.EndDate)
            mydbCursor.execute(sql, arg)
            
            mydb.commit()
            login = True
        except Exception as e:
            print(str(e))
        finally:
            if mydbCursor is not None:
                mydbCursor.close()

            if mydb is not None:
                mydb.close()
            print(login)
            return login
    def getInterests(self):
        mydb = None
        mydbCursor = None
        interests = []

        try:
            mydb = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            mydbCursor = mydb.cursor()

            sql = "SELECT DISTINCT Interest FROM interest"
            mydbCursor.execute(sql)
            rows = mydbCursor.fetchall()

            interests = [row[0] for row in rows]
        except Exception as e:
            print(str(e))
        finally:
            if mydbCursor is not None:
                mydbCursor.close()

            if mydb is not None:
                mydb.close()
        return interests
    def show_all(self):

        mydb = None
        mydbCursor = None
        flag = None
        try:
            mydb = pymysql.connect(
                host=self.host, user=self.user, password=self.password, database=self.database)
            mydbCursor = mydb.cursor()
            sql = "select * from interest"
            mydbCursor.execute(sql)
            row = mydbCursor.fetchall()
            flag = row
        except Exception as e:
            print(str(e))
        finally:
            if mydbCursor != None:
                mydbCursor.close()

            if mydb != None:
                mydb.close()
            return flag
    def show_data(self):

        mydb = None
        mydbCursor = None
        flag = None
        try:
            mydb = pymysql.connect(
                host=self.host, user=self.user, password=self.password, database=self.database)
            mydbCursor = mydb.cursor()
            sql = "select * from interest"
            mydbCursor.execute(sql)
            row = mydbCursor.fetchall()
            flag = row
        except Exception as e:
            print(str(e))
        finally:
            if mydbCursor != None:
                mydbCursor.close()

            if mydb != None:
                mydb.close()
            return flag
    def get_record_by_id(self, record_id):
        mydb = None
        mydbCursor = None
        try:
            mydb = pymysql.connect(
                host=self.host, user=self.user, password=self.password, database=self.database)
            mydbCursor = mydb.cursor()
            sql = "SELECT * FROM interest WHERE RollNo=%s"
            mydbCursor.execute(sql, (record_id,))
            row = mydbCursor.fetchone()
            return row
        except Exception as e:
            print(str(e))
        finally:
            if mydbCursor:
                mydbCursor.close()
            if mydb:
                mydb.close()
    def update_record(self, updated_rollNo, updated_name, updated_email, updated_gender, updated_dob,
                      updated_city, updated_interest, updated_department, updated_degree, updated_subject,
                      updated_startDate, updated_endDate):
        mydb = None
        mydbCursor = None
        try:
            mydb = pymysql.connect(
                host=self.host, user=self.user, password=self.password, database=self.database)
            mydbCursor = mydb.cursor()
            sql = """UPDATE interest 
                     SET  Name=%s, Email=%s, Gender=%s, Dob=%s, City=%s, Interest=%s, 
                         Department=%s, Degree=%s, Subject=%s, StartDate=%s, EndDate=%s
                     WHERE RollNo=%s"""
            args = (updated_name, updated_email, updated_gender, updated_dob, updated_city,
                    updated_interest, updated_department, updated_degree, updated_subject, updated_startDate,
                    updated_endDate, updated_rollNo)
            mydbCursor.execute(sql, args)
            mydb.commit()
        except Exception as e:
            print(str(e))
        finally:
            if mydbCursor is not None:
                mydbCursor.close()
            if mydb is not None:
                mydb.close()
    def delete_record(self, record_id):
        mydb = None
        mydbCursor = None
        try:
            mydb = pymysql.connect(
                host=self.host, user=self.user, password=self.password, database=self.database)
            mydbCursor = mydb.cursor()
            sql = "DELETE FROM interest WHERE RollNo=%s"
            mydbCursor.execute(sql, (record_id,))
            mydb.commit()
        except Exception as e:
            print(str(e))
        finally:
            if mydbCursor:
                mydbCursor.close()
            if mydb:
                mydb.close()
    def get_provincial_distribution(self):
        mydb = None
        mydbCursor = None
        try:
            mydb = pymysql.connect(
                host=self.host, user=self.user, password=self.password, database=self.database)
            mydbCursor = mydb.cursor()
            sql = "SELECT City, COUNT(*) as city_count FROM interest GROUP BY City"
            mydbCursor.execute(sql)
            rows = mydbCursor.fetchall()
            distribution_data = [{"label": row[0], "count": row[1]} for row in rows]
            return distribution_data
        except Exception as e:
            print(str(e))
        finally:
            if mydbCursor:
                mydbCursor.close()
            if mydb:
                mydb.close()

    def get_submission_chart_data(self, days):
        mydb = None
        mydbCursor = None
        try:
            mydb = pymysql.connect(
                host=self.host, user=self.user, password=self.password, database=self.database)
            mydbCursor = mydb.cursor()
            sql = "SELECT DATE(StartDate) as submission_date, COUNT(*) as submission_count FROM interest WHERE StartDate >= CURDATE() - INTERVAL %s DAY GROUP BY submission_date"
            mydbCursor.execute(sql, (days,))
            rows = mydbCursor.fetchall()
            chart_data = [{"date": str(row[0]), "count": row[1]} for row in rows]
            return chart_data
        except Exception as e:
            print(str(e))
        finally:
            if mydbCursor:
                mydbCursor.close()
            if mydb:
                mydb.close()

    def get_age_distribution(self):
        mydb = None
        mydbCursor = None
        try:
            mydb = pymysql.connect(
                host=self.host, user=self.user, password=self.password, database=self.database)
            mydbCursor = mydb.cursor()
            sql = "SELECT YEAR(CURDATE()) - YEAR(Dob) - (RIGHT(CURDATE(), 5) < RIGHT(Dob, 5)) as age, COUNT(*) as age_count FROM interest GROUP BY age"
            mydbCursor.execute(sql)
            rows = mydbCursor.fetchall()
            age_distribution = [{"age": row[0], "count": row[1]} for row in rows]
            return age_distribution
        except Exception as e:
            print(str(e))
        finally:
            if mydbCursor:
                mydbCursor.close()
            if mydb:
                mydb.close()

    # Example get_department_distribution() method in db.py
    def get_department_distribution(self):
        mydb = None
        mydbCursor = None
        try:
            mydb = pymysql.connect(
                host=self.host, user=self.user, password=self.password, database=self.database)
            mydbCursor = mydb.cursor()
            sql = "SELECT Department, COUNT(*) as department_count FROM interest GROUP BY Department"
            mydbCursor.execute(sql)
            rows = mydbCursor.fetchall()
            distribution_data = [{"label": row[0], "count": row[1]} for row in rows]
            return distribution_data
        except Exception as e:
            print(str(e))
        finally:
            if mydbCursor:
                mydbCursor.close()
            if mydb:
                mydb.close()


    def get_degree_distribution(self):
        mydb = None
        mydbCursor = None
        try:
            mydb = pymysql.connect(
                host=self.host, user=self.user, password=self.password, database=self.database)
            mydbCursor = mydb.cursor()
            sql = "SELECT Degree, COUNT(*) as degree_count FROM interest GROUP BY Degree"
            mydbCursor.execute(sql)
            rows = mydbCursor.fetchall()
            degree_distribution = [{"degree": row[0], "count": row[1]} for row in rows]
            return degree_distribution
        except Exception as e:
            print(str(e))
        finally:
            if mydbCursor:
                mydbCursor.close()
            if mydb:
                mydb.close()

    def get_gender_distribution(self):
        mydb = None
        mydbCursor = None
        try:
            mydb = pymysql.connect(
                host=self.host, user=self.user, password=self.password, database=self.database)
            mydbCursor = mydb.cursor()
            sql = "SELECT Gender, COUNT(*) as gender_count FROM interest GROUP BY Gender"
            mydbCursor.execute(sql)
            rows = mydbCursor.fetchall()
            gender_distribution = [{"gender": row[0], "count": row[1]} for row in rows]
            return gender_distribution
        except Exception as e:
            print(str(e))
        finally:
            if mydbCursor:
                mydbCursor.close()
            if mydb:
                mydb.close()
    
    def get_top_interests(self, limit):
        mydb = None
        mydbCursor = None
        interests = []

        try:
            mydb = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            mydbCursor = mydb.cursor()
            sql = f"SELECT Interest, COUNT(*) AS interest_count FROM interest GROUP BY Interest ORDER BY interest_count DESC LIMIT {limit}"
            mydbCursor.execute(sql)
            rows = mydbCursor.fetchall()
            interests = [row[0] for row in rows]
        except Exception as e:
            print(str(e))
        finally:
            if mydbCursor is not None:
                mydbCursor.close()
            if mydb is not None:
                mydb.close()
        return interests
    def get_bottom_interests(self, limit):
        mydb = None
        mydbCursor = None
        interests = []
        try:
            mydb = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            mydbCursor = mydb.cursor()
            sql = f"SELECT Interest, COUNT(*) AS interest_count FROM interest GROUP BY Interest ORDER BY interest_count ASC LIMIT {limit}"
            mydbCursor.execute(sql)
            rows = mydbCursor.fetchall()
            interests = [row[0] for row in rows]
        except Exception as e:
            print(str(e))
        finally:
            if mydbCursor is not None:
                mydbCursor.close()
            if mydb is not None:
                mydb.close()
        return interests
    def get_distinct_interests_count(self):
        mydb = None
        mydbCursor = None
        count = 0
        try:
            mydb = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            mydbCursor = mydb.cursor()
            sql = "SELECT COUNT(DISTINCT Interest) FROM interest"
            mydbCursor.execute(sql)
            count = mydbCursor.fetchone()[0]
        except Exception as e:
            print(str(e))
        finally:
            if mydbCursor is not None:
                mydbCursor.close()

            if mydb is not None:
                mydb.close()

        return count
