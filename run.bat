@echo off
rd /s /q allure-results 2>nul
pytest --alluredir=./allure-results
allure serve ./allure-results