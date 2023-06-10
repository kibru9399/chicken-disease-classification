from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.prepare_base_model import PrepareBaseModel
from cnnClassifier import logger

STAGE_NAME = 'Prepare base model.'
class BaseModelPreparationPipeline:
    def __init__(self):
        pass
    def main(self):
        config = ConfigurationManager()
        prepare_base_model_config = config.get_prepare_base_model_config()
        prepare_base_model = PrepareBaseModel(config=prepare_base_model_config)
        prepare_base_model.get_base_model()
        prepare_base_model.update_base_model()


if __name__ == '__main__':
    try:
        logger.info(f'****************************************')
        logger.info('>>>>>>>>>>stage {STAGE_NAME} started <<<<<<<<<<')
        obj = BaseModelPreparationPipeline()
        obj.main()
        logger.info('>>>>>>>>>>stage {STAGE_NAME} completed <<<<<<<<<<\n\n')
    except Exception as e:
        logger.exception(e)
        raise e
    
    