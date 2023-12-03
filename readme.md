Version control (gitHub) steps:
1. Git from Tools > Initialize Git Repository
2. Setting > Create Repository on GitHub > back
3. click main > "First commit" to Message >Stage and commit all changes -
4. click 'Publish branch as 'origin/main'
5. any change > step3-4 again

goto github > repository startpytest > code >

behave using docker container steps:
john_mac@MikeMac welcome-to-docker %
1. PC local: git clone https://github.com/anhsguy/startpytest.git
2. cd startpytest
3. docker build -t startpytest_image .
4. docker run startpytest_image --1.1GB

View detail on container or PC terminal: 

============================= test session starts ==============================
platform linux -- Python 3.8.18, pytest-7.4.3, pluggy-1.3.0
rootdir: /app
collected 14 items

test_compare.py ...                                                      [ 21%]
test_div_by_3_6.py ..                                                    [ 35%]
test_multiplication.py ....                                              [ 64%]
test_runner.py .                                                         [ 71%]
test_square.py ...                                                       [ 92%]
test_string.py .                                                         [100%]

=============================== warnings summary ===============================
test_compare.py:3
  /app/test_compare.py:3: PytestUnknownMarkWarning: Unknown pytest.mark.great - is this a typo?  You can register custom marks to avoid this warning - for details, see https://docs.pytest.org/en/stable/how-to/mark.html
    @pytest.mark.great

test_compare.py:8
  /app/test_compare.py:8: PytestUnknownMarkWarning: Unknown pytest.mark.great - is this a typo?  You can register custom marks to avoid this warning - for details, see https://docs.pytest.org/en/stable/how-to/mark.html
    @pytest.mark.great

test_compare.py:13
  /app/test_compare.py:13: PytestUnknownMarkWarning: Unknown pytest.mark.others - is this a typo?  You can register custom marks to avoid this warning - for details, see https://docs.pytest.org/en/stable/how-to/mark.html
    @pytest.mark.others

test_square.py:4
  /app/test_square.py:4: PytestUnknownMarkWarning: Unknown pytest.mark.square - is this a typo?  You can register custom marks to avoid this warning - for details, see https://docs.pytest.org/en/stable/how-to/mark.html
    @pytest.mark.square

test_square.py:9
  /app/test_square.py:9: PytestUnknownMarkWarning: Unknown pytest.mark.square - is this a typo?  You can register custom marks to avoid this warning - for details, see https://docs.pytest.org/en/stable/how-to/mark.html
    @pytest.mark.square

test_square.py:18
  /app/test_square.py:18: PytestUnknownMarkWarning: Unknown pytest.mark.others - is this a typo?  You can register custom marks to avoid this warning - for details, see https://docs.pytest.org/en/stable/how-to/mark.html
    @pytest.mark.others

test_string.py:8
  /app/test_string.py:8: PytestUnknownMarkWarning: Unknown pytest.mark.match - is this a typo?  You can register custom marks to avoid this warning - for details, see https://docs.pytest.org/en/stable/how-to/mark.html
    @pytest.mark.match

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
======================== 14 passed, 7 warnings in 0.04s ========================

Steps to push local to hub:

1. PC local: docker images > startpytest_image  
   tag:latest

2. docker login > rename: docker tag startpytest_image anhsguy792/startpytest_image

3. To hub: docker push anhsguy792/startpytest_image:latest

4. run: docker run anhsguy792/startpytest_image

remove any image: docker rmi startpytest_image or anhsguy792/startpytest_image

Whenever step 4, the image in the hub will be loaded to Local and showing in PC terminal (docker images) even you delete it earlier

