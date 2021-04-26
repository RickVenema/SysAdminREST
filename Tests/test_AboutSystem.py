from unittest import TestCase
from API.AboutSystem import AboutSystem


class TestAboutSystem(TestCase):
    """
    This test class is used for the test cases for the AboutSystem class.
    """

    def test_get_processor_info(self):
        assert AboutSystem._get_processor_info() == "Intel64 Family 6 Model 165 Stepping 2, GenuineIntel"

    def test_get_cpu_count(self):
        assert AboutSystem._get_cpu_count() == 8

    def test_get_total_info(self):
        assert AboutSystem.get_total_info() == {
            "CPU Count": 8,
            "CPU frequency": 2496.0,
            "Amount of ram": 31.79058074951172,
            "Processor information": "Intel64 Family 6 Model 165 Stepping 2, GenuineIntel"
        }

    def test_get_amount_ram(self):
        assert AboutSystem._get_amount_ram() == 31.79058074951172

    def test_get_mem_usage(self):
        print(f"Amount of RAM used: {AboutSystem.get_mem_usage()}")

    def test_get_cpu_usage(self):
        print(f"Amount of CPU used: {AboutSystem.get_cpu_usage()}")
