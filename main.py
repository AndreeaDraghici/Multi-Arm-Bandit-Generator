from src.random_input_generator import RandomInputGenerator


def main_driver():
    generator = RandomInputGenerator(num_files=10)
    generator.generate_inputs()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main_driver()
