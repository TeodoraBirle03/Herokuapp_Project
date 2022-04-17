pip install -U selenium
pip install behave
pip install behave-html-formatter
pip install webdriver-manager

run test
behave -f html -o behave-report.html --tags=smoke
flow-ul unui test de la 0:
atingem pages -> context -> steps -> features