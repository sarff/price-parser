import mysql.connector
import toml

config = toml.load("conf/config.toml")
#config = toml.load("/root/priceupdate/price-parser/conf/config.toml")
updtable = config.get('dbtable').get('updtable')
updrow = config.get('dbtable').get('updrow')
updwhere = config.get('dbtable').get('updwhere')
updwhere2 = config.get('dbtable').get('updwhere2')



mydb = mysql.connector.connect(
    host=config.get('database').get('host'),
    user=config.get('database').get('login'),
    password=config.get('database').get('passwd'),
    database=config.get('database').get('name')
)

class MySql():
    @staticmethod
    def update_price(setvalue):
        try:
            mycursor = mydb.cursor()
            sql = "UPDATE {0} SET {1} = '{2}' WHERE id = {3} LIMIT 1".format(updtable,updrow,setvalue,updwhere)
            mycursor.execute(sql)
            mydb.commit()
            mycursor.close()

            return True
        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))
            return False

    @staticmethod
    def update_upd(setvalue):
        try:
            mycursor = mydb.cursor()
            sql = "UPDATE {0} SET {1} = '{2}' WHERE id = {3} LIMIT 1".format(updtable, updrow, setvalue, updwhere2)
            mycursor.execute(sql)
            mydb.commit()
            mycursor.close()

            return True
        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))
            return False