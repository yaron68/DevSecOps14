import os


def get_app_number():
    print("Please enter the number of the program you want to start")
    print(f"1 videos")
    print(f"2 calculator")
    print(f"3 mines")
    while True:
        app_number = int(input())
        if 0 < app_number < 4:
            return app_number


def check_if_app_open(app_num):
    apps = {1: "shotwell", 2: "calculator", 3: "mines"}
    command = f"ps -ef | grep {apps[app_num]} "
    files = os.popen(command).read()
    for line in files.split("\n"):
        if "grep" not in line and apps[app_num] in line:
            return True
    return False


end_action = True
count = 0
while end_action and count < 3:
    app_no = get_app_number()
    res = check_if_app_open(app_no)
    if not res:
        if app_no == 1:
            os.system("shotwell &")
            end_action = False
        elif app_no == 2:
            os.system("gnome-calculator &")
            end_action = False
        elif app_no == 3:
            os.system("gnome-mines &")
            end_action = False
    else:
        print('Application already running')
        count += 1
