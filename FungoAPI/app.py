from flask import *
from flask_restful import Resource, Api
import pymysql
import pymysql.cursors

app = Flask(__name__)


api = Api(app)

# We create a resource with post, get, put, delete
class Employee(Resource):

    def post(self):
        data = request.json
        id_number = data['id_number']
        username = data['username']
        others = data['others']
        salary = data['salary']
        department = data['department']
        # connect to database
        connection = pymysql.connect(host='localhost', user='root', password='', database='FungoAPI')
        cursor = connection.cursor()
        sql = ''' insert into employees(id_number, username, others, salary, department) values(%s, %s, %s, %s,%s) '''
        # execute sql
        try:
            cursor.execute(sql, (id_number, username, others, salary, department))
            connection.commit()
            return jsonify({'message': 'Employee Saved'})
        except:
            return jsonify({'message': 'Failed to Save'})
        

    def get(self):
        connection = pymysql.connect(host='localhost', user='root', password='', database='FungoAPI')

        cursor = connection.cursor(pymysql.cursors.DictCursor)
        sql = "select * from employees order by salary ASC"
        cursor.execute(sql)
        if cursor.rowcount == 0:
            return jsonify({'message': 'No Employees'})
        else:
            employees = cursor.fetchall()
            return jsonify(employees) 
    
    def put(self):
          connection = pymysql.connect(host='localhost', user='root', password='', database='FungoAPI')
          data = request.json
          id_number = data['id_number']
          salary = data['salary']
          cursor = connection.cursor()
          sql = "update employees set salary=%s where id_number=%s"
          cursor.execute(sql,(salary, id_number))
          connection.commit()
          return jsonify({'message': 'Updated Successful'})
    
    def delete(self):
        connection = pymysql.connect(host='localhost', user='root', password='', database='FungoAPI')
        data = request.json
        id_number = data['id_number']
        cursor = connection.cursor()
        sql = "delete from employees where id_number =%s"
        cursor.execute(sql, id_number)
        connection.commit()
        return jsonify({'message': 'DELETE SUCCESSFUL'})

  


class Account(Resource):

    def post(self):
        data = request.json
        firstname = data['firstname']
        secondname = data['secondname']
        email = data['email']
        password = data['password']
        id = data['id']
        # connect to database
        connection = pymysql.connect(host='localhost', user='root', password='', database='FungoAPI')
        cursor = connection.cursor()
        sql = ''' insert into accounts(firstname, secondname, email, password, id) values(%s, %s, %s, %s, %s) '''
        # execute sql
        try:
            cursor.execute(sql, (firstname, secondname, email, password, id))
            connection.commit()
            return jsonify({'message': 'Saved'})
        except:
            return jsonify({'message': 'Failed'})

class Book(Resource):

    def post(self):
        data = request.json
        firstname = data['firstname']
        email = data['email']
        hotel = data['hotel']
        site = data['site']
        id = data['id']
        # connect to database
        connection = pymysql.connect(host='localhost', user='root', password='', database='FungoAPI')
        cursor = connection.cursor()
        sql = ''' insert into book(firstname,email, hotel, site, id) values(%s, %s, %s, %s, %s) '''
        # execute sql
        try:
            cursor.execute(sql, (firstname, email, hotel,site, id,))
            connection.commit()
            return jsonify({'message': 'Booked'})
        except:
            return jsonify({'message': 'Failed'})       

    def get(self):
        connection = pymysql.connect(host='localhost', user='root', password='', database='FungoAPI')

        cursor = connection.cursor(pymysql.cursors.DictCursor)
        sql = "select * from book order by ASC"
        cursor.execute(sql)
        if cursor.rowcount == 0:
            return jsonify({'message': 'No Booking'})
        else:
            employees = cursor.fetchall()
            return jsonify(Book) 

    def put(self):
          connection = pymysql.connect(host='localhost', user='root', password='', database='FungoAPI')
          data = request.json
          id = data['id']
          hotel = data['salary']
          site = data['site']
          cursor = connection.cursor()
          sql = "update booking set site=%s, hotel=%s where id=%s"
          cursor.execute(sql,(site, id, hotel))
          connection.commit()
          return jsonify({'message': 'Updated Successful'})
    
    def delete(self):
        connection = pymysql.connect(host='localhost', user='root', password='', database='FungoAPI')
        data = request.json
        id = data['id']
        hotel = data['salary']
        site = data['site']
        cursor = connection.cursor()
        sql = "delete from booking where id=%s, site=%s, hotel=%s"
        cursor.execute(sql, id, hotel, site)
        connection.commit()
        return jsonify({'message': 'DELETE SUCCESSFUL'})

# create an accessible link  to your API
api.add_resource(Employee, '/employees')
api.add_resource(Account, '/accounts')
api.add_resource(Book,'/booking')
# Run the app
if __name__ == '__main__':
    app.run(debug=True)



