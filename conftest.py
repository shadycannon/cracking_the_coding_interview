import pytest
from hashtable import HashTable

@pytest.fixture(scope='session', autouse=True)
def hashtable(request):
    ht = HashTable(100)
    ht['puppy'] = 'chorizo' 
    return ht
