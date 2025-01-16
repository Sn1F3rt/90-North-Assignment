1. Start the docker container: `docker-compose up -d`
2. Run migrations: `python manage.py migrate`
3. Create admin user: `python manage.py createsuperuser`
4. Run server: `python manage.py runserver`
5. Open browser and go to `http://localhost:8000`

You can create different users via register, login and then use the application in order to chat with other users after adding them as friends. 
