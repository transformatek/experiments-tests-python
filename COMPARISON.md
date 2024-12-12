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


## useful links 
- https://github.com/apache/airflow/tree/main/tests



# Python/Flask Testing Frameworks and Open Source Code Quality Tools

## Unit and Integration Testing Frameworks

### `unittest`
[docs.python.org](https://docs.python.org)  
A built-in Python module for writing and organizing unit tests. It supports test discovery, assertions, and test case management.

### `pytest`
 [pytest.org](https://pytest.org)  
A powerful and flexible testing framework for Python. It simplifies test writing with features like fixtures, parameterized testing, and a rich plugin ecosystem. `pytest` is more feature-rich and extensible than `unittest`, making it the go-to choice for most Python projects.

### `nose2`
 [nose2.io](https://nose2.io)  
Successor to Nose, providing a streamlined approach to running and managing Python tests. While `nose2` is simpler than `pytest`, it lacks the extensibility and community support of `pytest`.

### Conclusion:
For unit and integration testing in Flask applications, `pytest` is the most recommended due to its ease of use, flexibility, and strong community support.

## Component Testing

### `pytest-flask`
 [pytest-flask.readthedocs.io](https://pytest-flask.readthedocs.io)  
A Pytest plugin specifically designed for testing Flask applications. It helps in testing views, routes, and Flask-specific features.

### `Flask-Testing`
 [pythonhosted.org/Flask-Testing](https://pythonhosted.org/Flask-Testing)  
Enhances unittest with Flask-specific functionality for testing applications. `pytest-flask` is preferred for its modern features and seamless integration with the broader `pytest` ecosystem.

### Conclusion:
`pytest-flask` stands out as the best choice for component testing due to its simplicity and powerful integration with pytest.

## End-to-End (E2E) Testing

### `Selenium`
 [selenium.dev](https://selenium.dev)  
Automates browser interactions for E2E testing. It’s widely used but has a steeper learning curve and slower execution compared to modern tools.

### `Playwright`
 [playwright.dev](https://playwright.dev)  
A modern E2E testing tool with support for multiple browsers, parallel execution, and advanced debugging features. `Playwright` is faster and easier to use than Selenium, making it ideal for Flask applications with complex frontends.

### Conclusion:
For E2E testing, Playwright is highly recommended for its speed, ease of use, and advanced features compared to Selenium.

## Mocking API Calls

### `Responses`
 [github.com/getsentry/responses](https://github.com/getsentry/responses)  
A Python library for mocking HTTP requests made with the `requests` library.

### `HTTPretty`
 [httpretty.readthedocs.io](http://httpretty.readthedocs.io)  
A tool for intercepting and mocking HTTP requests. It works with various Python HTTP clients. `Responses` is simpler and more Pythonic, while `HTTPretty` offers broader client support but can be more complex to configure.

### Conclusion:
`Responses` is the best option for mocking API calls due to its simplicity and seamless integration with Python's requests library.

## Open Source Tools for Code Quality

### `SonarQube`
 [sonarqube.org](https://sonarqube.org)  
Continuous inspection of code quality that identifies bugs, vulnerabilities, and code smells. It supports Python and integrates with CI/CD pipelines. While it has a complex setup and configuration, it offers comprehensive analysis and detailed reporting, as well as the ability to detect security vulnerabilities.

### `Bandit`
 [bandit.readthedocs.io](https://bandit.readthedocs.io)  
A static analysis tool focused on finding security vulnerabilities in Python code. It detects common issues like hardcoded secrets and SQL injection risks. Bandit is lightweight and Python-specific, but limited to security checks.

### `Black`
 [black.readthedocs.io](https://black.readthedocs.io)  
An opinionated code formatter that enforces consistent styling. It automatically formats code and integrates well with most editors. However, it has no customization options for styling rules.

### `Flake8`
 [flake8.pycqa.org](https://flake8.pycqa.org)  
Combines `pyflakes`, `pep8`, and `mccabe` for linting and style checking. It is highly customizable via plugins and is flexible and extendable, but it doesn’t automatically fix issues.

### `Pylint`
[pylint.pycqa.org](https://pylint.pycqa.org)  
A widely used Python linter that checks for errors in Python code, enforces a coding standard, and looks for code smells. It offers detailed reports and is highly customizable through configuration options. However, it can be slow on large codebases.


### Conclusion:
For improving code quality:
  - Use `SonarQube` for comprehensive code analysis.
  - Use `Bandit `for Python security checks.
  - Combine `Black` for auto-formatting with `Flake8` for linting and style validation.




          	

