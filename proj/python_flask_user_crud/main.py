import pymysql
from app import app
from tables import Results, CropResults, CropDBResults
from db_config import mysql
from flask import flash, render_template, request, redirect
from werkzeug.security import generate_password_hash, check_password_hash

import numpy as np
import pandas as pd
from sklearn.model_selection import ShuffleSplit
import pickle



@app.route('/new_user')
def add_user_view():
	return render_template('add.html')
		
@app.route('/farm_user')
def farm_user_view():
	return render_template('farm.html')

@app.route('/predict')
def predict_view():
	return render_template('predict.html',output="No Prediction")


@app.route('/cropdb')
def cropdb_view():
	conn = None
	cursor = None
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT * FROM crop_tbl")
		rows = cursor.fetchall()
		table = CropDBResults(rows)
		table.border = True
		return render_template('cropdb.html', table=table)
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()



@app.route('/add', methods=['POST'])
def add_user():
	conn = None
	cursor = None
	try:		
		_name = request.form['inputName']
		_email = request.form['inputEmail']
		_password = request.form['inputPassword']
		# validate the received values
		if _name and _email and _password and request.method == 'POST':
			#do not save password as a plain text
			_hashed_password = generate_password_hash(_password)
			# save edits
			sql = "INSERT INTO tbl_user(user_name, user_email, user_password) VALUES(%s, %s, %s)"
			data = (_name, _email, _hashed_password,)
			conn = mysql.connect()
			cursor = conn.cursor()
			cursor.execute(sql, data)
			conn.commit()
			flash('User added successfully!')
			return redirect('/')
		else:
			return 'Error while adding user'
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()
		
@app.route('/')
def users():
	conn = None
	cursor = None
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT * FROM crop_tbl")
		rows = cursor.fetchall()
		table = CropResults(rows)
		table.border = True
		return render_template('allcrops.html', table=table)
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()

@app.route('/edit/<int:id>')
def edit_view(id):
	conn = None
	cursor = None
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT * FROM tbl_user WHERE user_id=%s", id)
		row = cursor.fetchone()
		if row:
			return render_template('edit.html', row=row)
		else:
			return 'Error loading #{id}'.format(id=id)
	except Exception as e:
		print(e)
	finally:
		cursor.close()
		conn.close()

@app.route('/update', methods=['POST'])
def update_user():
	conn = None
	cursor = None
	try:		
		_name = request.form['inputName']
		_email = request.form['inputEmail']
		_password = request.form['inputPassword']
		_id = request.form['id']
		# validate the received values
		if _name and _email and _password and _id and request.method == 'POST':
			#do not save password as a plain text
			_hashed_password = generate_password_hash(_password)
			print(_hashed_password)
			# save edits
			sql = "UPDATE tbl_user SET user_name=%s, user_email=%s, user_password=%s WHERE user_id=%s"
			data = (_name, _email, _hashed_password, _id,)
			conn = mysql.connect()
			cursor = conn.cursor()
			cursor.execute(sql, data)
			conn.commit()
			flash('User updated successfully!')
			return redirect('/')
		else:
			return 'Error while updating user'
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()
		
@app.route('/delete/<int:id>')
def delete_user(id):
	conn = None
	cursor = None
	try:
		conn = mysql.connect()
		cursor = conn.cursor()
		cursor.execute("DELETE FROM tbl_user WHERE user_id=%s", (id,))
		conn.commit()
		flash('User deleted successfully!')
		return redirect('/')
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()
		




### fUNCTIONS FROM Sandhya collab 
def highlown(nitro):
  if (nitro >= 0 and nitro <= 30) :
    valuen = str("low")
  elif (nitro > 30 and nitro <= 60) :
    valuen = str("medium")
  else:
    valuen = "high"
  return valuen


def highlowp(phos):
  valuep = 0
  if (phos >= 0 and phos <= 30) :
    valuep = "low"
  elif (phos> 30 and phos <= 60) :
    valuep = "medium"
  else:
    valuep = "high"
  return valuep


def highlowk(potash):
  valuek= 0
  if (potash >= 0 and potash <= 30) :
    valuek = "low"
  elif (potash > 30 and potash <= 60) :
    valuek = "medium"
  else:
    valuek = "high"
  return valuek

def thanjavur(sow,valuen,valuep,valuek):
  # January
  if sow == "January" :
    if valuen == "medium" and valuep == "low" and valuek == "low":
      print("The crop sugarcane can be grown in your field")
    elif valuen == "low" and valuep == "medium" and valuek == "medium":
    	print("The crop groundnut can be grown in your field")
    else:
    	print("No crop can be successfully grown in January for your present soil conditions")
  # February
  elif sow == "February" :
    if valuen == "medium" and valuep == "low" and valuek == "low":
      print("The crops sugarcane and banana can be grown as major crops in your field")
    elif valuen == "high" and valuep == "high" and valuek == "medium":
      print("The crop sesame can be grown in your field")
    else:
      print("No crop can be successfully grown in February for your present soil conditions")
 # March
  elif sow == "March" :
    if valuen == "medium" and valuep == "low" and valuek == "low":
      print("The crops sugarcane and banana can be grown as major crops in your field")
    elif valuen == "high" and valuep == "high" and valuek == "medium":
      print("The crop sesame can be grown in your field")
    else:
      print("No crop can be successfully grown in March for your present soil conditions")
  # April
  elif sow == "April" :
    if valuen == "medium" and valuep == "low" and valuek == "low":
      print("The crop banana can be grown as a major crop in your field")
    else:
      print("No crop can be successfully grown in April for your present soil conditions")
  # May, August, September, October
  elif sow == "May" or sow == "August" or sow == "September" or sow ==" October":
      print("No crop can be successfully grown in", sow," for your present soil conditions")
  # June
  elif sow == "June" :
    if valuen == "medium" and valuep == "low" and valuek == "low":
      print("The crop rice can be grown as major crop in your field")
    else:
      print("No crop can be successfully grown in June for your present soil conditions")
  # July
  elif sow == "July" :
    if valuen == "medium" and valuep == "low" and valuek == "low":
      print("The crop rice can be grown as major crop in your field")
    else:
      print("No crop can be successfully grown in July for your present soil conditions")
  # November
  elif sow == "November" :
    if valuen == "medium" and valuep == "low" and valuek == "low":
      print("The crop banana can be grown as a major crop in your field")
    else:
      print("No crop can be successfully grown in November for your present soil conditions")
  # December
  elif sow == "December" :
    if valuen == "medium" and valuep == "low" and valuek == "low":
      print("The crop banana can be grown as a major crop in your field")
    elif valuen == "low" and valuep == "medium" and valuek == "medium":
      print("The crop groundnut can be grown in your field")
    else:
      print("No crop can be successfully grown in December for your present soil conditions")


def coimbatore(sow,valuen,valuep,valuek):
  #JAnuary
  if sow == "January" :
    if valuen == "low" and valuep == "low" and valuek == "medium":
      print("The crop coconut can be grown in your field")
    else:
      print("No crop can be successfully grown in January for your present soil conditions")
  #MArch, April
  elif sow == "March" or sow =="April":
    if valuen == "low" and valuep == "medium" and valuek == "low":
      print("The crop cowpea can be grown in your field")
    else:
      print("No crop can be successfully grown in March for your present soil conditions")
  
  #May, #June
  elif sow =="May" or sow == "June":
    if valuen == "low" and valuep == "medium" and valuek == "low":
      print("The crop cowpea can be grown in your field")
    elif valuen == "medium" and valuep == "low" and valuek == "low":
      print("The crop sorghum can be grown in your field")
    elif valuen == "low" and valuep == "medium" and valuek == "low":
      print("The crop maize can be grown in your field")
    elif valuen == "medium" and valuep == "medium" and valuek == "medium":
      print("The crop tomato can be grown in your field")
    else:
      print("No crop can be successfully grown in January for your present soil conditions")
 #July
  elif sow == "July":
    if valuen == "low" and valuep == "medium" and valuek == "low":
      print("The crop cowpea can be grown in your field")
    elif valuen == "medium" and valuep == "low" and valuek == "low":
      print("The crop sorghum can be grown in your field")
    else:
      print("No crop can be successfully grown in March for your present soil conditions")
  #Nov, Dec
  elif sow == "November" or "December":
    if valuen == "medium" and valuep == "medium" and valuek == "medium":
      print("The crop tomato can be grown in your field")
    else:
      print("No crop can be successfully grown in March for your present soil conditions")

def dindigul(sow,valuen,valuep,valuek):
  # January
  if sow == "January" :
    if valuen == "low" and valuep == "medium" and valuek == "medium":
      print("The crop groundnut can be grown in your field")
    else:
      print("No crop can be successfully grown in January for your present soil conditions")
  # May
  elif sow == "May" :
    if valuen == "medium" and valuep == "low" and valuek == "low":
      print("The crop sorghum can be grown in your field")
    else:
      print("No crop can be successfully grown in May for your present soil conditions")
  # February, March, April, November, August
  elif sow == "February" or sow == "March" or sow == "April" or sow =="November" or sow == "August":
      print("No crop can be successfully grown in", sow," for your present soil conditions")
  # June, July
  elif sow == "June" or sow== "July" :
    if valuen == "low" and valuep == "medium" and valuek == "medium":
      print("The crop pepper can be grown as major crop in your field")
    elif valuen == "medium" and valuep == "low" and valuek == "low":
      print("The crop sorghum can be grown in your field")
    elif valuen == "medium" and valuep == "medium" and valuek == "low":
      print("The crop potato can be grown in your field")
    else:
      print("No crop can be successfully grown in June for your present soil conditions")
  # September, October
  elif sow == "September" or sow == "October" :
    if valuen == "low" and valuep == "medium" and valuek == "low":
      print("The crop maize or butter beans can be grown as major crop in your field")
    else:
      print("No crop can be successfully grown in July for your present soil conditions")
  # November
  elif sow == "November" :
    if valuen == "medium" and valuep == "low" and valuek == "low":
      print("The crop banana can be grown as a major crop in your field")
    else:
      print("No crop can be successfully grown in November for your present soil conditions")
  # December
  elif sow == "December" :
    if valuen == "low" and valuep == "medium" and valuek == "medium":
      print("The crop groundnut can be grown in your field")
    else:
      print("No crop can be successfully grown in December for your present soil conditions")


def thoothukudi(sow,valuen,valuep,valuek):
  # August
  if sow == "August" :
    if valuen == "low" and valuep == "medium" and valuek == "low":
      print("The crop black gram can be grown in your field")
    else:
      print("No crop can be successfully grown in August for your present soil conditions")
  # May
  elif sow == "May" :
    if valuen == "medium" and valuep == "low" and valuek == "low":
      print("The crop sorghum can be grown in your field")
    else:
      print("No crop can be successfully grown in May for your present soil conditions")
  # February, March, April, January
  elif sow == "February" or sow == "March" or sow == "April" or sow =="January":
      print("No crop can be successfully grown in", sow," for your present soil conditions")
  # June, July
  elif sow == "June" or sow== "July" :
    if valuen == "medium" and valuep == "low" and valuek == "low":
      print("The crop sorghum can be grown in your field")
    elif valuen == "medium" and valuep == "medium" and valuek == "low":
      print("The crop sunflower can be grown in your field")
    else:
      print("No crop can be successfully grown in June for your present soil conditions")
  # September, October
  elif sow == "September" or sow == "October" :
    if valuen == "low" and valuep == "medium" and valuek == "low":
      print("The crop maize can be grown as major crop in your field")
    elif valuen == "medium" and valuep == "high" and valuek == "low":
      print("The crop green gram can be grown in your field")
    elif valuen == "high" and valuep == "medium" and valuek == "low":
      print("The crop sesame can be grown in your field")
    elif valuen == "low" and valuep == "medium" and valuek == "low":
      print("The crop black gram can be grown in your field")
    else:
      print("No crop can be successfully grown in July for your present soil conditions")
  # November, December
  elif sow == "November" or sow == "December" :
    if valuen == "low" and valuep == "medium" and valuek == "low":
      print("The crop black gram can be grown as a major crop in your field")
    else:
      print("No crop can be successfully grown in November for your present soil conditions")




def calculate_globals(_nitrogen, _phosphorous, _potassium, _month, _location ):
	nitro = int(_nitrogen)
	valuen = highlown(nitro)
	phos = int(_phosphorous)
	valuep = highlowp(phos)
	potash = int(_potassium)
	valuek = highlowk(potash)
	loc = _location
	sow = _month
	if loc == "Thanjavur":
  		thanjavur(sow,valuen,valuep,valuek)
	elif loc == "Dindigul":
  		dindigul(sow,valuen,valuep,valuek)
	elif loc == "Thoothukudi":
  		thoothukudi(sow,valuen,valuep,valuek)
	elif loc == "Coimbatore":
	  coimbatore(sow,valuen,valuep,valuek)
	return 






def region_frompos(lati,longi):
  if lati == 11:
    if longi == 77:
      return "Coimbatore"
    else : 
      return "Thanjavur"
  elif lati == 10 and longi == 78:
    return "Dindigul"
  elif lati == 9 and longi == 78:
    return "Thoothudi"
  else :
    return "Coimbatore"

def pos_fromregion(loc):
  if loc == "Thanjavur":
  	return (11,79)
  if loc == "Dindigul":
    return (10,78)
  if loc == "Thoothukudi" :
    return (9,78)
  else :
    return (11,77)






def getfrom_cropdb():
	conn = None
	cursor = None
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT * FROM tbl_user where ")
		rows = cursor.fetchall()
		table = Results(rows)
		table.border = True
		return render_template('users.html', table=table)
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()


def calculate_fromdb(_nitrogen, _phosphorous, _potassium, _month, _location ):
  nitro = int(_nitrogen)
  phos = int(_phosphorous)
  potash = int(_potassium)
  (_lati,_longi) = pos_fromregion(_location)
  sow = _month
  print (nitro , phos, potash, _lati, _longi, sow)
  # Getting the value from the DB !!! 
  conn = None
  cursor = None
  try:
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    soilchk = "nitro = "+ _nitrogen + " and pota = "+_potassium+" and phos = "+_phosphorous+" and" ; 
    exstring = "SELECT * FROM crop_tbl where ("+ soilchk + " longi = "+ str(_longi) + " and month = '"+_month+"')"
    print (exstring)
    cursor.execute(exstring)
    rows = cursor.fetchall()
    print (rows)
    room = pH = nitro
    ptratio = temp = potash
    lstat = rain = phos

    fromfile = pickle.load(open('model.pk1','rb'))
    client_data = [[pH, rain, ptratio ]]
    for i, price in enumerate(fromfile.predict(client_data)):
      print("Predicted Yield for Crop {}'s home: ${:,.2f}".format(i+1, price))


    return rows
    #return render_template('crop.html', table=table)
  except Exception as e:
    print(e)
  finally:
    cursor.close()
    conn.close()



## farm user method

@app.route('/farm', methods=['POST'])
def farm_user():
  try:		
    _nitrogen = request.form['Nitrogen']
    _phosphorous = request.form['Phosphorous']
    _potassium = request.form['Potassium']
    _month = request.form['Month']
    _location = request.form['Location']
    my_string = _nitrogen + _phosphorous + _potassium + _month + _location
    calculate_globals(_nitrogen, _phosphorous, _potassium, _month, _location)
    print(my_string)
    rows = calculate_fromdb(_nitrogen, _phosphorous, _potassium, _month, _location)
    print( " Did I reach here ")
    if (_nitrogen):
      table = CropResults(rows)
      table.border = True
      print(" Ready to render")
      print (table)
      return render_template('crop.html', table=table)
      #app.logger.info("First Log ")
		# validate the received values
    if _nitrogen and _phosphorous and _potassium and request.method == 'POST':
      flash(my_string)
      return redirect('/')
    else:
      return redirect('/')
    return redirect('/')
  except Exception as e:
    print(e)
	


@app.route('/predict' , methods=['POST'])
def predict():
  try:		
    _ph = request.form['pH']
    _rainfall = request.form['Rainfall']
    _temperature = request.form['Temperature']
    my_string = _ph + _rainfall + _temperature
    print(my_string)
    phval = float(_ph)
    rainval = float(_rainfall)
    tempval = float(_temperature)
    fromfile = pickle.load(open('model.pk1','rb'))
    client_data = [[phval, rainval, tempval ]]
    for i, price in enumerate(fromfile.predict(client_data)):
      print("Predicted Yield for Crop {}'s home: {:,.2f} kg/ha".format(i+1, price))
    output_str = "Predicted Yield is "+str(price)+"kg/ha"
    flash("output_str")
    return render_template('predict.html',output=output_str)
  except Exception as e:
    print(e)






 



#### MAIN FUNCTION 

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000, debug=False)
