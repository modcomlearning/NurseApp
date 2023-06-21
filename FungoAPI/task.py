from flask import *
from flask_restful import Resource, Api
import pymysql 
import pymysql.cursors

app = Flask(__name__)
api = Api(app)

class Member(Resource):
    def post(self):
        data = request.json
        account_number = data['account_number']
        names = data['names']
        amount = data['amount']
        location = data['location']
        connection = pymysql.connect(host='localhost', user='root', password='', database='FungoAPI')
        cursor = connection.cursor()
        sql = '''insert into members(account_number,names,amount,location) values(%s,%s,%s,%s)'''
        try:
            cursor.execute(sql, (account_number,names,amount,location))
            connection.commit()
            return jsonify({'message':'Member Saved'})
        except:
            return jsonify({'message':'Failed'})
        
    def get(self):
        connection = pymysql.connect(host='localhost', user='root', password='', database='FungoAPI')
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        sql = "select * from members order by account_number ASC"
        cursor.execute(sql)
        if cursor.rowcount == 0:
            return jsonify({'message': 'No Member'})
        else:
            members = cursor.fetchall()
            return jsonify(members) 
            
    def put(self):                                                                                                                            
          connection = pymysql.connect(host='localhost', user='root', password='', database='FungoAPI')  
          data = request.json
          account_number = data['account_number']
          amount = data['amount']
          cursor = connection.cursor()
          sql = "update members set amount=%s where account_number=%s"
          cursor.execute(sql,(amount, account_number))
          connection.commit()
          return jsonify({'message': 'Updated Successful'})
        
    def delete(self):
        connection = pymysql.connect(host='localhost', user='root', password='', database='FungoAPI')
        data = request.json
        account_number = data['account_number']
        cursor = connection.cursor()
        sql = "delete from members where account_number=%s"
        cursor.execute(sql, account_number)
        connection.commit()
        return jsonify({'message': 'DELETE SUCCESSFUL'})

api.add_resource(Member, '/members')
if __name__ == '__main__':
    app.run(debug=True)
