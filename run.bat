pytest -s -v -m "sanity"--browser=chrome .\testCases\
rem pytest -s -v -m "sanity and regression"--browser=chrome .\testCases\
rem pytest -s -v -m "sanity or regression"--browser=chrome .\testCases\
rem pytest -s -v -m "regression"--browser=chrome .\testCases\

pause