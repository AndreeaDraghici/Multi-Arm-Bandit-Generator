import os
import random
import logging

from src.load_logging_configuration import load_logging_config


class RandomInputGenerator :
    def __init__(self, num_files=10) :

        load_logging_config()

        # Get the logger for the 'staging' logger
        self.logger = logging.getLogger('staging')
        """
        Initializes the RandomInputGenerator.

        :param num_files: Number of random input files to generate.
        """
        self.num_files = num_files
        self.data_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)),
                                     '../input')  # Define the path to the 'input' directory

    def generate_inputs(self) :
        """
        Generates random input files.

        For each file, generates a random number of arms, total iterations, and epsilon.
        Saves the files in the 'input' directory.
        """
        try :
            # Check if the 'input' directory exists, and if not, create it
            if not os.path.exists(self.data_dir) :
                os.makedirs(self.data_dir)

            self.logger.info(f"Generating {self.num_files} random input files.")
            for i in range(1, self.num_files + 1) :
                num_arms = random.randint(5, 15)  # Generate a random number of arms
                num_iterations = random.randint(1500, 50000)  # Generate a random number of iterations
                epsilon = round(random.uniform(0.1, 0.5), 2)  # Generate a random epsilon

                file_path = os.path.join(self.data_dir, f'input{i}.txt')

                with open(file_path, 'w') as file :
                    file.write(f"{num_arms}\n{num_iterations}\n{epsilon}\n")  # Write the values to the input file

                self.logger.info(f"File {f'input{i}.txt'} generated with parameters: "
                                 f"num_arms={num_arms}, num_iterations={num_iterations}, epsilon={epsilon}")
        except Exception as e :
            error_message = f"An error occurred while generating input files due to: {str(e)}"
            self.logger.error(error_message)

