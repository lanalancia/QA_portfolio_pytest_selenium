from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pytest


@pytest.fixture
def create_webdriver():
    return webdriver.Chrome()
