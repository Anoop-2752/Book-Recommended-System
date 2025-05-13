### Book Recommendation System

1. First, we create a notebook/ folder, and inside it, a research notebook (research.ipynb) to conduct all the exploratory work. In this notebook, we build our collaborative filtering model and save the trained model using pickle into an artifacts/ folder.

2. Next, we set up the project folder structure to enable modular and maintainable coding. This can be done either manually or automatically. Here, we create the structure automatically.

- We create a template.py file, which contains the logic to generate the project’s folder structure.

- This template.py file can be reused for any end-to-end machine learning project. You can also customize it based on specific project requirements.

- It includes everything needed to set up a standard ML pipeline structure, ensuring consistency across projects.

3. Modular Coding Approach:
Instead of writing all code in a single file, we split the logic into separate modules (e.g., data ingestion, model training, evaluation, etc.), and bring them together at the main execution point.

4. Next we are writing The setup.py: file is a standard Python script used for packaging Python projects. It's especially important when you're turning your machine learning or data science project into a distributable Python package.

5. -e . add on the requirements.txt this will look for set.py and install your folder as your local package.

6. Then we create YAML file in config folder and also add in requirement.txt and we execute it then a egg-info file will be created. And once it is created our local package installation is done. Now we can write the modular coding.

7. Now we are writing the exception handler : Custom exeption you can use this file for all the projects. the main benefit of this is it will show the line no that has the error.

8. Next we write the logger : A logger file records program events like info, errors, and warnings, helping track execution, debug issues, and save logs for analysis during development or production..

9. Then we will write the utils file : utils.py is a utility module in a Python project. It's typically used to store helper functions or reusable logic that are shared across multiple files in your project.

10. Now we can write the constant file : The constant file (usually inside a constant/ folder in a modular machine learning project) the file is used to stores fixed values like file paths or names, improving project consistency, reducing repetition, and making configuration changes easier and centralized.

11. Artifacts : are files generated during an ML pipeline—like datasets, models, and logs—stored in a dedicated folder to track outputs, ensure reproducibility, and simplify debugging.

12. Next we will write the entity : The entity module holds custom classes (often using Python’s @dataclass) that define the structure and type of data used across the ML pipeline — such as configuration settings, artifacts, and schema objects. making code cleaner, more readable, and easier to maintain and debug.

13. next we are writing configuration.py file : configuration.py is a Python module that reads settings (like file paths, parameters, or API keys) from a config file (usually config.yaml) and returns them as structured objects, often using data classes from the entity module. so that YAMl file is important.