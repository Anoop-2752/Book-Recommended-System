from books_recommender.components.stage_00_data_ingestion import DataIngestion
from books_recommender.components.stage_01_data_validation import DataValidation
from books_recommender.components.stage_02_data_transformation import DataTransformation
from books_recommender.components.stage_03_model_trainer import ModelTrainer


class TrainingPipeline:
    def __init__(self):
        self.data_ingestion = DataIngestion()
        
    def start_training_pipeline(self):
        """
        Starts the training pipeline
        :return: none
        """
        self.data_ingestion.initiate_data_ingestion()
        