#515zzz
create project on github
add ssh-key
begin your project!

#11.4 init django 
	with admin.py form.py model.py
#11.5
python manage.py collectstatic
#11.8
branch my_rest
#11.9 
branch request & require
curl http://10.10.8.32:8000/tt/people/ -H 'Accept: text/html'
curl http://10.10.8.32:8000/tt/people/ -H 'Accept: application/json'
curl -X POST http://10.10.8.32:8000/tt/people/ -d '{"name":"test","city":"test","Email":"test@test.com"}'
