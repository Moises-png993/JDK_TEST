import json, time
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.firefox.webdriver import WebDriver
from pages.client_page import ClientsPage
from pages.login_page import LoginPage


def test_create_10_clients(driver: WebDriver | WebDriver):

    # Login
    login_page = LoginPage(driver)
    login_page.login(
        username="moises@yopmail.com",
        password="Mr@1!+234"
    )

    clients_page = ClientsPage(driver)

    # Validar que cargó la página
    assert clients_page.is_loaded()
    time.sleep(1)
    # Leer JSON
    with open("data/clients.json", encoding="utf-8") as file:
        clients_data = json.load(file)

    # Iterar clientes
    for client in clients_data:
        clients_page.create_client(client)
    time.sleep(10)