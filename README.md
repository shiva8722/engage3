# engage3
1.create virtual environment with python3.
--> python3.6 -m virtualenv vir_env_engage

2.Activate virtual environment
--> source vir_env_engage/bin/activate

3.Git configuration
-->git clone git@github.com:shiva8722/engage3.git


4.install required library in virtual environment.
--> pip install -r requirements.txt

5.running python script
  -->cd engage3
  -->python engage_script.py

#To run test cases

--> pytest

--> coverage run -m pytest

--> coverage report
![alt text](https://raw.githubusercontent.com/shiva8722/engage3/main/Screen_shots/report.png)

--> coverage html

![script_test](https://raw.githubusercontent.com/shiva8722/engage3/main/Screen_shots/code_coverage_script_test.png)

![script](https://raw.githubusercontent.com/shiva8722/engage3/main/Screen_shots/code_coverage_enage_script.png)
