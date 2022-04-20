Emag BDD Automation Framework

Site tested: emag.to\
Design pattern used: page object model\
Methodology: behavior driven development

To import project\
git clone https://github.com/Andy-ITFactory/emag.git

Librarries to install:\
pip install -U selenium\
pip install behave\
pip install behave-html-formatter\
pip install webdriver-manager

Run tests:\
behave -f html -o behave-report.html --tags=emag

Happy Testing!\
Andy

Troubleshoot:\
Daca nu merge cu pip incercati comanda: py -m pip install selenium\
Daca nici asa nu merge:\
File -> Settings -> Click pe Project: [nume_proiect] -> Python Interpreter -> +\
Cautati 'selenium' -> Install Package
