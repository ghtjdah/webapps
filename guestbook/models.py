import MySQLdb
from django.db import models

# Create your models here.
from webapps.settings import DATABASES


def connect():
    try:
        db = MySQLdb.connect(
            host=DATABASES['default']['HOST'],
            port=int(DATABASES['default']['PORT']),
            user=DATABASES['default']['USER'],
            password=DATABASES['default']['PASSWORD'],
            db=DATABASES['default']['NAME'],
            charset='utf8')
        return db
    except MySQLdb.Error as e:
        print("Error {}: {}".format(e.args[0], e.args[1]))
        return None


def fetchall(table):
    try:
        # 1. DB연결
        db = connect()

        # 2. 커서 생성
        cursor = db.cursor(MySQLdb.cursors.DictCursor)

        # 3. SQL문 실행
        sql = '''
            select no, name, message, 
                date_format(reg_date,'%Y-%m-%d %H:%i') as commit_date
                from {}
                order by reg_date desc
                '''.format(table)

        cursor.execute(sql)
        results = cursor.fetchall()

        length = len(results)-1
        count = 1
        for result in results:
            results[length]['sequence'] = count
            length -= 1
            count += 1

        # 4. 자원 정리
        cursor.close()
        db.close()

        # 5. 결과 처리
        return results

    except MySQLdb.Error as e:
        return None


def insert(message):
    try:
        db = connect()

        # 2. 커서 생성
        cursor = db.cursor()

        # 3. SQL문 실행
        sql = '''
            insert 
    	        into guestbook
            values (null,'{0}','{1}','{2}',now())'''\
            .format(message['name'], message['password'],message['message'])

        count = cursor.execute(sql)

        # 4. 자원 정리
        cursor.close()
        db.commit()
        db.close()

        # 5. 결과 처리
        return count==1

    except MySQLdb.Error as e:
        print("Error {}: {}".format(e.args[0], e.args[1]))
        return None


def delete(info):
    try:
        db = connect()

        # 2. 커서 생성
        cursor = db.cursor()

        # 3. SQL문 실행
        sql = '''
            delete
                from guestbook
                where no = {0}
                and password = {1}
                '''.format(info['no'], info['password'])

        count = cursor.execute(sql)
        print(count)

        # 4. 자원 정리
        cursor.close()
        db.commit()
        db.close()

        # 5. 결과 처리
        return count==1

    except MySQLdb.Error as e:
        print("Error {}: {}".format(e.args[0], e.args[1]))
        return False