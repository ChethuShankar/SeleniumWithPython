import logging

logging.basicConfig(filename="..\logs\demologs.log", filemode="w", level=logging.DEBUG,
                    format="%(asctime)s - %(levelname)s - %(message)s",datefmt='%m/%d/%Y %I:%M:%S %p')


class DemoLogging:
    def add_numbers(self, a, b):
        return a + b

    def multiply_numbers(self, a, b):
        return a * b


dl = DemoLogging()
sum_result = dl.add_numbers(3, 5)
mul_result = dl.multiply_numbers(5, 6)
# logging.DEBUG(f"DEBUG:{mul_result}")
logging.warning(f"debug warning : addition result {sum_result}")
logging.error(f"debug error : addition result {sum_result}")
