import cv2
import time
import threading


TIME_LIMITED: int = 5  # // DEFINIR TEMPO PARA TIMEOUT DA CAMERA
Lista_de_camera = list(map(lambda x:{"ipCamera": f'''rtsp://admin:Visao5500@{".".join([str(int(i)) for i in x.strip().split('|')[0].split(".")])}'''},open("lista-de-cameras.txt","r")))

# for a in range(32, 36):
#     for x in range(1, 255):
#         if a == 32 and x >= 50:
#             Lista_de_camera.append(
#                 {"ipCamera": f"rtsp://admin:Visao5500@172.30.{a}.{x}"}
#             )
#         elif a in [33, 34, 35]:
#             Lista_de_camera.append(
#                 {"ipCamera": f"rtsp://admin:Visao5500@172.30.{a}.{x}"}
#             )


class MyThread(threading.Thread):
    def __init__(self, target, args=()):
        super(MyThread, self).__init__()
        self.func = target
        self.args = args

    def run(self):
        self.result = self.func(*self.args)

    def get_result(self):
        try:
            return self.result
        except Exception:
            return None


def limit_decor(limit_time):
    def functions(func):
        def run(*params):
            thre_func = MyThread(target=func, args=params)
            thre_func.setDaemon(True)
            thre_func.start()
            sleep_num = int(limit_time // 1)
            sleep_nums = round(limit_time % 1, 1)
            for i in range(sleep_num):
                time.sleep(1)
                infor = thre_func.get_result()
                if infor:
                    return infor
            time.sleep(sleep_nums)
            if thre_func.get_result():
                return thre_func.get_result()
            else:
                return (False, None)

        return run

    return functions


@limit_decor(TIME_LIMITED)
def video_capture_open(rtsp):
    capture = cv2.VideoCapture(rtsp)
    return (True, capture)


def frame_get(rtsp, camera, tempo):
    try:
        cap_status, cap = video_capture_open(rtsp)
        if not cap_status:
            return cap
        while True:
            _, frame = cap.read()
            fim = time.time()
          
            tempoAtual = int(fim - tempo)
            try:
                cv2.imwrite(f"./fotoscameras/{camera}.jpg", frame[0:416, 0:416])
            except:
                return {"status": 2, "cap": cap}           
            return {"status": 1, "cap": cap}
    except Exception as err:
        print(err)
        pass


def main() -> None:
    camera = 0
    for x in range(4):
        for i in Lista_de_camera:
            camera += 1
            ipCamera = i["ipCamera"]
            tempo = time.time()
            result = frame_get(ipCamera, camera, tempo)
            if not result:
                print(f"Failed to open RTSP stream, Camera: {ipCamera[23:]}")
            else:
                if result["status"] == 1:
                    result["cap"].release()
                    print(f" iP: {ipCamera[23:]}OK!")
                elif result["status"] == 2:
                    print(f"Camera com erro  iP: {ipCamera[23:]} ")


if __name__ == "__main__":
    main()
