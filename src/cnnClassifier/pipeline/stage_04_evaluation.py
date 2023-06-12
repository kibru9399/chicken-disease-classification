from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.prepare_callbacks import PrepareCallbacks
from cnnClassifier.components.evaluation import Evaluation
from cnnClassifier import logger

STAGE_NAME = 'MODEL EVALUATION.'
class EvaluationPipelline:
    def __init__(self):
        pass
    def main(self):
        config = ConfigurationManager()
        val_config = config.get_validation_config()
        evaluation = Evaluation(val_config)
        evaluation.evaluation()
        evaluation.save_score()

if __name__ == '__main__':
    try:
        logger.info(f'****************************************')
        logger.info(f'>>>>>>>>>>stage {STAGE_NAME} started <<<<<<<<<<')
        obj = EvaluationPipelline()
        obj.main()
        logger.info(f'>>>>>>>>>>stage {STAGE_NAME} completed <<<<<<<<<<\n\n')
    except Exception as e:
        logger.exception(e)
        raise e
    