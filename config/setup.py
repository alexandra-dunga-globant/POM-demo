from decouple import config

class SetupData:
    # to have a separate setup.py file only for exec path ( for ex browsers in incognito, specific states)
    #test PR_lenalena

    USER = config('USER')

    CHROME_EXEC_PATH = f"/Users/{USER}/Downloads/chromedriver"
    FIREFOX_EXEC_PATH = f"/Users/{USER}/Downloads/geckodriver"
    EDGE_EXEC_PATH = f"/Users/{USER}/Downloads/msedgedriver"
    SAFARI_EXEC_PATH = f"/Users/{USER}/Downloads/safaridriver"
