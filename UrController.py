import socket
import time

# UR10e robot IP address and port
ROBOT_IP = "192.168.2.249"
ROBOT_PORT = 30002

def send_ur_script(command):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((ROBOT_IP, ROBOT_PORT))
        s.send(command.encode())
        response = s.recv(1024).decode()
        print("Response:", response)

def move_to_home():
    command = "movej([0, -1.57, 1.57, 0, -1.57, 0], a=1.4, v=1.05)\n"
    send_ur_script(command)

def move_to_T_Pose():
    command = "movej([0,-1.57,-1.57,0,1.57,1.57], a=0.3, v=1.05, t=0, r=0.01)\n"
    send_ur_script(command)

def move_to_custom_position():
    command = "movel(p[0.5, 0.3, 0.4, -3.14, -1.57, 0], a=1.2, v=0.25)\n"
    send_ur_script(command)

if __name__ == "__main__":
    try:
        move_to_home()
        time.sleep(2)
        move_to_T_Pose()
    except KeyboardInterrupt:
        print("Program interrupted.")
