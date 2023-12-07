# 2023ChargedUp
Our robotics code for the 2023 FRC season charged up

>:3
```bash
# Deploy
py -3 robot.py deploy --nc



# Download/push to computer
py -3 -m robotpy_installer download <module name>

# Install - disconnect from WiFi
py -3 -m robotpy_installer install <module name>
```



for git

Pushing to a branch
```bash
git push --set-upstream notorigin Branch-Name
```
qaq
Adding all changes
```bash
git add .
```

Check status
```bash
git status
```


Install ctre(used for can falcons(the drive of good))
```bash
py -3 -m pip install robotpy[ctre]
```
see push and download for getting on robot



# Source for CAN network.
https://docs.ctre-phoenix.com/en/stable/ch08_BringUpCAN.html