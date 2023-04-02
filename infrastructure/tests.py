from django.test import TestCase
from infrastructure.servises.monitoring import ProcessMemoryScheme, FullMemoryScheme


class TestMemoryMonitoring(TestCase):

    def test_monitoring_process_memory(self):
        response = self.client.get(
            'http://127.0.0.1:8000/api/v1/infrastructure/full/',
        )
        self.assertTrue(isinstance(FullMemoryScheme(**response.data), FullMemoryScheme))

    def test_monitoring_full_memory(self):
        response = self.client.get(
            'http://127.0.0.1:8000/api/v1/infrastructure/process/',
        )
        self.assertTrue(isinstance(ProcessMemoryScheme(**response.data), ProcessMemoryScheme))

