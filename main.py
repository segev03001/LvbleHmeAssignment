import requests
import postgresHandler
import clickPayrequests
import psycopg2
import sys


def clickpayConnect(username, password):
    try:
        with requests.Session() as s:
            clickPayrequests.login(username, password)
            UserProfileParams = clickPayrequests.getUserProfileData()
            PayNowParams = clickPayrequests.getPayNowData()
            UserProfileResponse = s.post(UserProfileParams[0], headers=UserProfileParams[2], data=UserProfileParams[1])
            PayNowParamsResponse = s.post(PayNowParams[0], headers=PayNowParams[2], data=PayNowParams[1])
    except Exception as e:
        print("We got some problems to connect")

    if 'Error' in PayNowParamsResponse.json():
        print("Error accrue: " + PayNowParamsResponse.json()['Error']['Text'])
    else:
        try:
            conn = psycopg2.connect(
                database="LvbleHomeAssignment", user='postgres', password='s2512160', host="localhost", port='5433'
            )
            conn.autocommit = True
            cursor = conn.cursor()
            columnsData = [PayNowParamsResponse["Result"]["user"]["Login"], UserProfileResponse["Result"]["city"],
                           tenant_portal, PayNowParamsResponse["Result"]["user"]["Email"],
                           PayNowParamsResponse["Result"]["user"]["Cellphone"]]
            postgresHandler.insertIntoDBTable(cursor, columnsData)
            conn.close()
        except Exception as e:
            print("We got problem update the DB " + e.args[0])


def clickpayConnectDB(tableName):
    # creating the DB that save the data
    # postgres
    correctConnection = True
    while correctConnection:
        print("we are creating PostgreSQL DB and tables.")
        user = input("Enter username of PostgreSQL DB (press ENTER for default:'postgres'): ") or 'postgres'
        password = input("Enter password of PostgreSQL DB (press ENTER for default:'1234'): ") or '1234'
        port = input("Port (press ENTER for default:'5432'): ") or '5432'
        try:
            conn = psycopg2.connect(
                database="postgres", user=user, password=password, host="localhost", port=port
            )
            correctConnection = False
        except Exception as e:
            print("We can't connect to DB, please try again\n")

    conn.autocommit = True
    cursor = conn.cursor()
    print(postgresHandler.createDB(cursor))
    conn.close()

    # creating the tables that save the data
    # postgres
    conn = psycopg2.connect(
        database="LvbleHomeAssignment", user='postgres', password='s2512160', host="localhost", port='5433'
    )
    conn.autocommit = True
    cursor = conn.cursor()
    postgresHandler.createTables(cursor, tableName)
    conn.close()


if __name__ == '__main__':
    try:
        tenant_portal = sys.argv[1]
        user = sys.argv[2]
        passw = sys.argv[3]
    except Exception as e:
        print("There is problem with the arguments")

    # tenant_portal = 'click_pay'
    # user = 'micael.lasry@gmail.com'
    # passw = 'Micael123'

    if tenant_portal == 'click_pay':
        clickpayConnectDB(tenant_portal)
        clickpayConnect(user, passw)
    elif tenant_portal == 'activebuilding':
        print("We can't connect this website yet")
    elif tenant_portal == 'activebuilding':
        print("We can't connect this website yet")
    else:
        print("We can't connect this website")
