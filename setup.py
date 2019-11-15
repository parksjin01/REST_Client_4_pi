from setuptools import setup, find_packages

setup(
    name = "RestClient4py",
    version = "1.0.4",
    description = "REST-API client for Python",
    author = "Damotorie",
    author_mail = "parksjin01@gmail.com",
    url = "https://github.com/parksjin01/REST_Client_4_pi",
    download_url = "https://github.com/parksjin01/REST_Client_4_pi",
    install_requires = ["requests"],
    packages = find_packages(),
    keywords = ["REST", "REST-client"],
    python_requires = ">=3",
)