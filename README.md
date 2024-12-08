# Experiments-tests-python
Experiments different testing framework for Python

##  User stories
- [ ] As a software tests developper, I should be to implement tests in a Python/Flask project, in order to ensure high quality of the delivrables,
- [ ] As a software tests developper, I should be have automated hooks that improve the quality of my code (on commit or push) , in order to ensure high quality of the delivrables,
- [ ] As a software tests developper, I should get quick feedback of the quality of my code, in order to ensure high quality of the delivrables,
- [ ] As a project maintainer, I should be able to check the code code quality on CI pipelines, in order to ensure high quality of the delivrables,


## Steps
- [ ] List all relevant testing frameworks for Python/Flask in a nd MD file,
- [ ] List all open source software tool that can help to imporve code quality (SonarQube, ...),
- [ ] Create a starter FlaskAppBuilder application,
- [ ] Create fake model/view/Api for testing the backend,
- [ ] Create a test for the API endopoint,
- [ ] Update the README fie,
- [ ] Add comparison (Pros, Cons) of the frameworks and tools to the above MD file.

## Requirements
- [ ] Test each Framework in a separate branch,
- [ ] Use devContainer extension to hanlde developement environement.



## Run  flask

```bash
cd src
flask run
```
## Migration steps
First time
```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
flask db revision --rev-id a3bf43e917a8
```
After updates
```bash
flask db migrate
flask db upgrade
```
## Create admin user

```bash
flask fab create-admin
```

## steps for test API  with pytest-flask

```bash
pip install -r requirements.txt
```

```bash
cd src
```
```bash
cd app ```


```bash
cd tests```

```bash
pytest test_api.py```
