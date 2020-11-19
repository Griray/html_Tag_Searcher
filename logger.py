import logging


journal_format = logging.basicConfig(filename='journal.log', filemode='w', datefmt='%d-%m-%Y; %H:%M:%S',
                                     level=logging.INFO, format='%(name)s - %(levelname)s - %(asctime)s - %(message)s ')
