# Automated Testing Framework for The Internet (https://the-internet.herokuapp.com/)

## Project Overview

This repository contains an automated testing framework for the website [The Internet](https://the-internet.herokuapp.com/). The framework is designed to provide efficient, maintainable, and scalable automated tests using the Page Object Model (POM) strategy.

## Page Object Model (POM) Strategy

### Manual Test Cases
Before automation, each test case is initially documented as a manual test case. This documentation serves as a blueprint for automation, ensuring that the steps align with automation principles.

### Page Objects
PageObjects classes are created for each example link, utilizing XPath for identification (e.g., `//a[@href='/abtest']`). Additionally, PageObject classes are nested for examples with steps that navigate to multiple pages, promoting a modular and reusable approach.

### BaseClass
A BaseClass is utilized for repeatable actions across tests, enhancing code maintainability and reducing redundancy.

### Conftest and Fixtures
The Conftest file is employed for fixtures, allowing the definition of reusable fixtures across different test modules.

## Object-Oriented Programming (OOP) Concepts

Efficient automation relies on OOP principles such as encapsulation, inheritance, and polymorphism. The framework leverages these concepts to create modular, scalable, and maintainable code.

## Framework Features

### Multiple Browser Automation
The framework supports automation on multiple browsers, providing flexibility for cross-browser testing.

### Jenkins Integration
Integration with Jenkins enables continuous integration and automated testing with every code commit.

### Test Failure Screenshots
In case of test failures, the framework captures screenshots for diagnostic purposes, aiding in identifying and resolving issues quickly.

### Multi-Thread Run
The framework is designed to support multi-threaded test execution, optimizing test suite execution time.

