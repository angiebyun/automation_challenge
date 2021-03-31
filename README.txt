Author: Angela Byun

Before you proceed, please make sure that your Python version is at least 3.0 and that you have a chromedriver in the working directory.
Replace f_path with your index.html path on line 10.

1.) Navigate to AutomationChallenge folder
2.) In terminal, run: python -m unittest -v main.py

#########################################################################################################################################

RESULTS:

(AutomationChallenge) C:\Users\angel\Desktop\AutomationChallenge>python -m unittest -v main.py
test1 (main.automation_challenge) ... TEST 1:

[INFO] Email element found and sent keys.
[INFO] Password element found and sent keys.
[INFO] Login button found and clicked.
ok
test2 (main.automation_challenge) ... TEST 2:

[INFO] There are a total of  3  items in the list.
[INFO] Second list item's value is List Item 2
[INFO] Second list item's badge is 6
ok
test3 (main.automation_challenge) ... TEST 3:

ok
test4 (main.automation_challenge) ... TEST 4:

ok
test5 (main.automation_challenge) ... TEST 5:

[SUCCESS] Test 5 Button clicked.
ok
test6 (main.automation_challenge) ... TEST 6:

The value of coordiates 2,2 is:  It
ok

----------------------------------------------------------------------
Ran 6 tests in 49.121s

OK
