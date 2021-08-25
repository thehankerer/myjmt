from flask_table import Table, Col, LinkCol
 
class Results(Table):
    user_id = Col('Id', show=False)
    user_name = Col('Name')
    user_email = Col('Email')
    user_password = Col('Password', show=False)
    edit = LinkCol('Edit', 'edit_view', url_kwargs=dict(id='user_id'))
    delete = LinkCol('Delete', 'delete_user', url_kwargs=dict(id='user_id'))


class CropResults(Table):
    crop_id = Col('Id', show=False)
    nitro = Col('pH')
    phos = Col('Rainfall')
    pota = Col('Temperature')
    majorcrop = Col('Crop Name')
    month  = Col('Month')
    cropyield = Col("Yield Kg/Ha")
    minorcrop = Col('Password', show=False)



class CropDBResults(Table):
    crop_id = Col('Id', show=False)
    nitro = Col('pH')
    phos = Col('Rainfall')
    pota = Col('Temperature')
    lati = Col('latitude')
    longi = Col('longitute')
    month  = Col('Month')
    majorcrop = Col('Crop Name')
    cropyield = Col("Yield Kg/Ha")
    minorcrop = Col('Password', show=False)
