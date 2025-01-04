from src.APIKeyL.APIKeyL import APIKeyL

files1 = ['java/testDirectory', 'resources/database.json']
files2 = ['java/testDirectory/database.xml', 'resources']
locator = APIKeyL(files1, 6)
locator.find_keys()
