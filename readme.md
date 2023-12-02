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

View detail on container or PC terminal: Hello World! 2+3= 5 Type: Sedan Color: Blue

Steps to push local to hub:

1. PC local: docker images > startpytest_image  
   tag:latest

2. docker login > rename: docker tag startpytest_image anhsguy792/startpytest_image

3. To hub: docker push anhsguy792/startpytest_image:latest

4. run: docker run anhsguy792/startpytest_image

remove any image: docker rmi startpytest_image or anhsguy792/startpytest_image

Whenever step 4, the image in the hub will be loaded to Local and showing in PC terminal (docker images) even you delete it earlier

