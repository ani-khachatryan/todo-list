# todo-list
techprog project (2nd sem)

![architecture overview](http://www.plantuml.com/plantuml/svg/ZLJVJzim47xFN-77L5F5EqE8GZishGD4YwOzHMvyoomSEznTnX3ZVrykRe9fksbzgVsTl-z-vunO8xUro-ZU-aQZhbNfD95wpivrULzXQBsv22wWkj4EBX70PpF4y1Z15UY8dGSqW5kmGUkhYByaoiI04FYfWOjTyM_WN7YCbAmCTHCyU5PppNgZ2N82_0auUUxqiXZWBJoqGFnHU-C0rSa9iMPR3YzFJxiKLFSxEcemb404fEZ1gOw55YWLggqt_vPWS5192fl0FJHL5N31mUWdAbZJFUKj0HRMJ7hxEqNWJU43s--sx5I3poUlFjSTuulskahSHdSzz_gccCtdkUZsYg_mVB5Sh1U7B9UBzNgs-hpAZMP8NCrQ_W6U9OZmDsVBwyjFLudMrUBhtMfnczQeiiI7Wfqg5ohhj-T64pq6DDlhKBP1UXE2Kz9T1mm5zgAuLvob2FwtfpSr7PzQeuwLzKEpf2OTG2o3EM109Tf6lE-QYEFxbVoF_UGYeUIHC7cVc7jQtfEYn30BbN35DW34vlWuAeWn5KxUY4urwewkhESUjaQmbmnyMyTGO_gnmfOXjY4q48i6lngBa5JiZW37YdbTm_OeapnUaov6zzgOVkB7G0r8EzzYO2nl4V6dDzBeajLhgvQMU9n1Owbn-cbtHUX3mBNis1Ybv5ssYE1ZHNl6pgTWEXrtEjktlLs8BBs9UHprFKkSomEAwJPdoJcQOgRPcFB9Ru7Jv0vnUamkVLztNqZZiZFmfgtT7m00)


# How to run

Download the server and client folders to host and user PCs recpectively.

On server:
cd abs_path_to/server
python3 create_db.py (only once)
python3 server.py


On client:
cd abs_path_to/client
python3 main.py

Enjoy!

# Supported functionality
todo-list has GUI implemented for client side with pythons kivy module

Supported operations are:
Authorizing, registering, adding/deleting tasks, displaying tasks scheduled on a certain date.
Also every day at 9 AM todo-list sends notification about that days tasks.

# Features and fixes that should be added in future
Make server-client relations work not only on local network
Server Deployment to a cloud
Packing the app and making it easily downloadable and installable
