"""Running the Xetra ETL application"""
import logging
import logging.config

import yaml
import sys


def main():

    """
        entry point to run the xetra ETL job.
    """
    # Parsing YAML file
    print("Python version:", sys.version)
    config = 'C:\\Users\\Leo_B\\Documents\\Data Bellows\\python_projects\\xetra\\xetra_1234\\configs\\xetra_report1_config.yml'
    config = yaml.safe_load(open(config))
    # configure logging
    log_config = config['logging']
    logging.config.dictConfig(log_config)
    logger = logging.getLogger(__name__)
    logger.info("This is a test.")    


if __name__ == '__main__':
    main()