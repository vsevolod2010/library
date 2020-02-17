from rest_framework.test import APIClient


factory = APIClient()

print('*************************************************')
print('*             TEST CRUD FOR AUTHORS             *')
print('*-----------------------------------------------*')

c_request = factory.post('/api/v0/authors/', {
    'name': 'Корней Иванович Чуковский',
    'birthday': '1882-03-19',
    'city': 'Санкт-Петербург'
})

status, data = c_request.status_code, c_request.data
if not status == 201:
    print('* CREATE -- FAILURE                             *')
else:
    print('* CREATE -- SUCCESSFUL                          *')

r_request = factory.get('/api/v0/authors/{}/'.format(data['id']))
status, data = r_request.status_code, r_request.data
if not status == 200:
    print('* READ -- FAILURE                               *')
else:
    print('* READ -- SUCCESSFUL                            *')

u_request = factory.patch('/api/v0/authors/{}/'.format(data['id']), {
    'birthday': '1882-03-31',
})

status, data = u_request.status_code, u_request.data
if not status == 200:
    print('* UPDATE -- FAILURE                             *')
else:
    print('* UPDATE -- SUCCESSFUL                          *')

d_request = factory.delete('/api/v0/authors/{}/'.format(data['id']))

status, data = d_request.status_code, d_request.data
if not status == 204:
    print('* DELETE -- FAILURE                             *')
else:
    print('* DELETE -- SUCCESSFUL                          *')
print('*************************************************')


print('*************************************************')
print('*              TEST CRUD FOR BOOKS              *')
print('*-----------------------------------------------*')

c_request = factory.post('/api/v0/books/', {
    'title': 'The Lord of Rings',
    'annotation': '...',
    'publication_year': '1955',
    'authors': [1, 2]
})

status, data = c_request.status_code, c_request.data
if not status == 201:
    print('* CREATE -- FAILURE                             *')
else:
    print('* CREATE -- SUCCESSFUL                          *')

r_request = factory.get('/api/v0/books/{}/'.format(data['id']))
status, data = r_request.status_code, r_request.data
if not status == 200:
    print('* READ -- FAILURE                               *')
else:
    print('* READ -- SUCCESSFUL                            *')

u_request = factory.patch('/api/v0/books/{}/'.format(data['id']), {
    'publication_year': '1954',
})

status, data = u_request.status_code, u_request.data
if not status == 200:
    print('* UPDATE -- FAILURE                             *')
else:
    print('* UPDATE -- SUCCESSFUL                          *')

d_request = factory.delete('/api/v0/books/{}/'.format(data['id']))

status, data = d_request.status_code, d_request.data
if not status == 204:
    print('* DELETE -- FAILURE                             *')
else:
    print('* DELETE -- SUCCESSFUL                          *')
print('*************************************************')
