import platform
import multiprocessing
import psutil


class AboutSystem:
    """
    About Systems

    This Class is for getting information about the system and its properties.
    """

    @staticmethod
    def get_total_info():
        """ get_total_info
        Function to return a dictionary with information about the system

        <b>Returns:</b> Dict containing information
        """
        return {"CPU Count": AboutSystem._get_cpu_count(),
                "CPU frequency": AboutSystem._get_cpu_freq(),
                "Amount of ram": AboutSystem._get_amount_ram(),
                "Processor information": AboutSystem._get_processor_info()}

    @staticmethod
    def _get_cpu_freq():
        """
        Gets information about the frequency of the CPU
        :return:
        """
        return psutil.cpu_freq()[2]

    @staticmethod
    def _get_processor_info():
        """
        Get information about the processor
        :return:
        """
        return platform.processor()

    @staticmethod
    def _get_cpu_count():
        """
        Get amount of cpu count of the system
        :return:
        """
        return multiprocessing.cpu_count()

    @staticmethod
    def _get_amount_ram():
        """
        Get amount of RAM of the system
        :return:
        """
        total_mem = psutil.virtual_memory()[0]
        return total_mem / 1024 ** 3

    @staticmethod
    def get_mem_usage():
        """
        This function is used to get the usage of the amount of RAM.

        This uses the psutil library.

        <b>Return: </b> Usage of the amount of memory in use
        """
        return psutil.virtual_memory()[2]

    @staticmethod
    def get_cpu_usage():
        return psutil.cpu_percent(interval=0.5)
