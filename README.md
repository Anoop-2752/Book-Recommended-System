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

