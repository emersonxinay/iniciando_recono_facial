import cv2

def main():
    # Abre la cámara
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # Usando CAP_DSHOW para la API de Windows
    
    # Verifica si la cámara se abrió correctamente
    if not cap.isOpened():
        print("Error al abrir la cámara. Saliendo...")
        return
    
    while True:
        ret, frame = cap.read()  # Captura un frame de la cámara
        
        # if not ret:
        #     print("No se puede recibir el frame. Saliendo...")
        #     break
        
        # Muestra el frame en una ventana
        # cv2.imshow('Video', frame)
        
        # Espera a que se presione la tecla 'q' para salir del bucle
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # Libera la cámara y cierra las ventanas
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
