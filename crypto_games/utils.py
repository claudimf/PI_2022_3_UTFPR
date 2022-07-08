from cv2 import cv2


def redimensionar(path):
    img = cv2.imread(path, 0)
    img = cv2.resize(img, (300, 300))
    cv2.imwrite(path, img)
   
def aplicar_tons_verde(path):
    img = cv2.imread(path)
    img2 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img2[:, :, 0] = 0
    img2[:, :, 2] = 0
    cv2.imwrite(path, img2)

def adicionar_marca_dagua(path):
    img = cv2.imread(path)
    cv2.putText(img, 'Crypto Games', (30, 30), cv2.FONT_HERSHEY_PLAIN, 1.5, 
            (255, 255, 0), 2, cv2.LINE_AA)
    cv2.imwrite(path, img)