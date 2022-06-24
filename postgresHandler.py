def createDB(curs):
    # Preparing query to create a database
    sql = '''CREATE DATABASE "LvbleHomeAssignment"
    WITH 
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'Hebrew_Israel.1255'
    LC_CTYPE = 'Hebrew_Israel.1255'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1;''';

    # Creating a database
    try:
        curs.execute(sql)
        return "\nDatabase created successfully"
    except Exception as e:
        return e.args[0]


def createTables(curs):
    # Dropping tables if already exists.
    curs.execute("select exists(select * from information_schema.tables where table_name=%s)", ('mytable',))
    if curs.fetchone()[0]:
        print("Tables clickPay already exists")
    else:
        # Creating table as per requirement
        clickPayTable = '''CREATE TABLE public."clickPay"
        (
        username  character varying(30) COLLATE pg_catalog."default" NOT NULL,
        address  character varying(30) COLLATE pg_catalog."default",
        PropertyManagement character varying(30) COLLATE pg_catalog."default",
        email character varying(5000) COLLATE pg_catalog."default",
        phoneNumber character varying(150) COLLATE pg_catalog."default"
        )
    
        TABLESPACE pg_default;
    
        ALTER TABLE public."clickPay"
        OWNER to postgres;'''
        try:
            curs.execute(clickPayTable)
            print("clickPay tables created successfully\n")
        except Exception as e:
            print(e.args[0])


def insertIntoDBTable(curs, columns):
    clickPayTable = '''INSERT INTO public."clickPay"(
	    username, address, propertymanagement, email, phonenumber)
	    VALUES ({0}, {1}, {2}, {3}, {4});)'''.format(columns[0], columns[1], columns[2], columns[3], columns[4])

    try:
        curs.execute(clickPayTable)
        print("clickPay tables created successfully")
    except Exception as e:
        print(e.args[0])
