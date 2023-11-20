import cv2
import face_recognition

# Cargando la imagen y convirtiéndola a RGB
image = cv2.imread('path/a/tu/imagen.jpg')
rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Encontrando las ubicaciones de los rostros en la imagen
face_locations = face_recognition.face_locations(rgb_image)

print(f"Se encontraron {len(face_locations)} rostros en la imagen.")

# Iterando sobre cada ubicación de rostro en la imagen
for face_location in face_locations:
    # Extraer las coordenadas de la ubicación del rostro
    top, right, bottom, left = face_location
    
    # Dibujando un rectángulo alrededor del rostro encontrado
    cv2.rectangle(image, (left, top), (right, bottom), (0, 255, 0), 2)

# Mostrando la imagen con los rostros detectados
cv2.imshow('Rostros encontrados', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
