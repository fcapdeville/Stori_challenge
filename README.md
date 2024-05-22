# Stori challenge: 

# QA Data:
QA Automation engineer: Federico Capdeville

Mail: federicocapdeville@gmail.com 


### Description:
Goal of this challenge is to successfully design, perform and execute all 
test steps on the given website. In addition to this, creation of RTM associated.

#### Deliverables:
- Excel RTM for QA Challenge
- Readme.md
- QA Challenge code
- Gherkin Files

-----

# Requirements for this project:
- Python (develop in 3.10.9).
- Libraries required are listed in requirements.txt.
- Use below command to install libraries required: 
  ``` Python
  pip -r requirements.txt
  ```
- web drivers (Chrome, Firefox and Opera) (used by Selenium).
  - Chrome path: 'E:/Chromedriver/chromedriver.exe'
  - Firefox path: 'E:/Geckodriver/geckodriver.exe'
  - Opera path: 'E:/Operadriver/operadriver.exe'

Note: paths variables are located in features/testdata.py.

# How to execute:
- cd Stori folder
- Execute using command below according to browser necessities:
``` Python
python .\test_stori_challenge.py --browser chrome
python .\test_stori_challenge.py --browser firefox
python .\test_stori_challenge.py --browser opera
```
Note: by default browser argument is chrome.

After execution, output reports will be generated in Reports folder:

Report is located in 'reports/index.html'.

## How to open reports:
After an execution, a report is generated in this project.

To open a report, open reports/allure_report/index.html File.

## How to generate reports:
Reports generated for this project are made in allure:

https://github.com/allure-framework/allure2/releases

Download files from latest release and unzip them.

Then, add allure path to environment variables:

..\allure-2.29.0\bin
