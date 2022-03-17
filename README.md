# Apps-Technical-Assignment
Software Developer Position Project

Total Effort for this project is approximately 810 minutes or 13,5 hours.
Efforts added to every commit individually.
Spent a lot of time to learn docker and JQuery.
If i already know them i think effort would be 8 hours.

# With Docker

navigate to the folder "apps_assignment"

in your terminal apply theese commands (you can change image-name to whatever you want to call your docker image)

docker build --tag image-name .

if building successfull now run this command

docker run --publish 8000:8000 image-name

When you see "watching file changes with statreloader" in your terminal now you can navigate to browser

Navigate to 127.0.0.1:8000/home/

Enjoy website :)

if you want to open admin panel you should navigate to  127.0.0.1:8000/admin

Two users are already registered

1- username = mehmet , password = deneme123  (Admin)
2- username = appz , password = `123456&*
