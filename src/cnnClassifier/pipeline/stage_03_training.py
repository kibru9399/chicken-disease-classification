from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.prepare_callbacks import PrepareCallbacks
from cnnClassifier.components.training import Training
from cnnClassifier import logger

STAGE_NAME = 'TRAINING.'
class TrainingPipelline:
    def __init__(self):
        pass
    def main(self):
        config = ConfigurationManager()
        prepare_callbacks_config = config.get_prepare_callbacks_config()
        callbacks = PrepareCallbacks(prepare_callbacks_config)
        callback_list = callbacks.get_tb_ckpt_callbacks()

        training_config = config.get_training_config()
        training = Training(training_config)
        training.get_base_model()
        training.train_valid_generator()
        training.train(callback_list)

if __name__ == '__main__':
    try:
        logger.info(f'****************************************')
        logger.info(f'>>>>>>>>>>stage {STAGE_NAME} started <<<<<<<<<<')
        obj = TrainingPipelline()
        obj.main()
        logger.info(f'>>>>>>>>>>stage {STAGE_NAME} completed <<<<<<<<<<\n\n')
    except Exception as e:
        logger.exception(e)
        raise e
    