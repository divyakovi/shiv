from fixtures_test import studentDB
import pytest
def test_scott_dat():
    db=studentDB()
    db.connect('data.json')
    scott_data = db.get_data('scott')
    assert scott_data['id']==1
    assert scott_data['name']=='scott'
    assert scott_data['result']=='pass'

def test_mark_data():
    db=studentDB()
    db.connect('data.json')
    mark_data=db.get_data('mark')
    assert mark_data['id']==2
    assert mark_data['name']=='mark'
    assert mark_data['result']=='fail'