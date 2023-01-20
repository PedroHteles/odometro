import imp
import os
import cv2


def files_path04(path):
    for _, _, arquivo in os.walk(path):
        for a in arquivo:
            print(a)
            try:
                img = cv2.imread(f"J:/IA/fotosProcessarMonitoraCamera/{a}")
                frame = img[0:416, 0:416]
                cv2.imwrite(f"J:/IA/fotosRecortadasIA2/{a}", frame)
            except:
                continue


files_path04("J:/IA/fotosProcessarMonitoraCamera")
