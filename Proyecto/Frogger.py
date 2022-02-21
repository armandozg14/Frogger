from argparse import Action
from OpenGL.GL import *
from glew_wish import *
import glfw
import math

#unidades por segundo
velocidad = 0.8
posicion_triangulo = [0.0,-0.95,0.0]
posiciones_cuadrados = [
     [0.3,-0.85, 0.0],
     [0.8, -0.75, 0.0],
     [-0.4, -0.65, 0.0],
     [0.2, -0.55, 0.0],
     [0.7, -0.45, 0.0],
     [-0.1, -0.55, 0.0],
     [-0.3, -0.25, 0.0],
     [-0.6, -0.15, 0.0],
     [-0.2, -0.05, 0.0],
     [0.5, 0.05, 0.0],
     [0.3, 0.15, 0.0],
     [0.7, 0.25, 0.0],
     [0.9, 0.75, 0.0],
     [0.2, 0.45, 0.0],
     [-0.4, 0.55, 0.0],
     [-0.2, 0.65, 0.0],
     [0.5, 0.75, 0.0],
     [0.2, 0.85, 0.0],
     #mas cuadros
     [0.5,-0.85, 0.0],
     [0.5, -0.75, 0.0],
     [-0.9, -0.65, 0.0],
     [0.8, -0.55, 0.0],
     [0.9, -0.45, 0.0],
     [-0.8, -0.85, 0.0],
     [-0.7, -0.25, 0.0],
     [-0.2, -0.15, 0.0],
     [-0.5, -0.05, 0.0],
     [0.9, 0.05, 0.0],
     [0.7, 0.15, 0.0],
     [0.2, 0.25, 0.0],
     [0.7, 0.65, 0.0],
     [0.5, 0.45, 0.0]
     
 ]

velocidades_cuadrados=[0.5, 0.6, 0.5, 0.7, 0.5, 0.8, 0.5, 0.9, 0.5, 0.6, 0.5, 0.7, 0.5, 0.8, 0.5, 0.9, 0.5, 0.6, 0.5, 0.8, 0.5, 0.9, 0.5, 0.6, 0.5, 0.7, 0.5, 0.8, 0.9, 0.5]
direcciones_cuadrados=[2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3]

window = None
velocidad_triangulo = 0.1

tiempo_anterior = 0.0

#0 arriba , 1 abajo, 2 izquierda, 3 derecha
direccion_triangulo = 0
angulo_triangulo = 0
direccion_derecha = 3
direccion_izquierda = 2

def actualizar():
    global tiempo_anterior
    global window
    global posicion_triangulo
    global direccion_triangulo
    global angulo_triangulo
    global velocidad_triangulo

    tiempo_actual = glfw.get_time()
    tiempo_delta = tiempo_actual - tiempo_anterior
    
    for i in range(30):
        cantidad_movimiento = velocidades_cuadrados[i] * tiempo_delta
        if direcciones_cuadrados[i] == 2:
            posiciones_cuadrados[i][0] = posiciones_cuadrados[i][0] - cantidad_movimiento
            if posiciones_cuadrados[i][0] <= -1:
                posiciones_cuadrados[i][0] = 1
        if direcciones_cuadrados[i] == 3:
            posiciones_cuadrados[i][0] = posiciones_cuadrados[i][0] + cantidad_movimiento
            if posiciones_cuadrados[i][0] >= 1:
                posiciones_cuadrados[i][0] = -1

    tiempo_anterior = tiempo_actual

def key_callback(window, key, scancode, action, mods):
    global posicion_triangulo
    global velocidad_triangulo

    #Que la tecla escape cierre ventana al ser presionada
    if key == glfw.KEY_ESCAPE and action == glfw.PRESS:
        glfw.set_window_should_close(window,1)

    #MOVER LA RANA
     #IZQUIERDA
    if key == glfw.KEY_LEFT and (action == glfw.PRESS):
        posicion_triangulo[0] =  posicion_triangulo[0] - velocidad_triangulo
    #DERECHA
    if key == glfw.KEY_RIGHT and (action == glfw.PRESS):
         posicion_triangulo[0] =  posicion_triangulo[0] + velocidad_triangulo
    #ARRIBA
    if key == glfw.KEY_UP and (action == glfw.PRESS):
         posicion_triangulo[1] =  posicion_triangulo[1] + velocidad_triangulo
    #ABAJO
    if key == glfw.KEY_DOWN and (action == glfw.PRESS):
         posicion_triangulo[1] =  posicion_triangulo[1] - velocidad_triangulo



def colisionando():
    colisionando = False
    for i in range(30):
        if (posicion_triangulo[0] + 0.04 >= posiciones_cuadrados[i][0] - 0.05 
            and posicion_triangulo[0] - 0.04 <= posiciones_cuadrados[i][0] + 0.05 
            and posicion_triangulo[1] + 0.04 >= posiciones_cuadrados[i][1] - 0.05 
            and posicion_triangulo[1] - 0.04 <= posiciones_cuadrados[i][1] + 0.05):
            colisionando = True 
    return colisionando

def draw_ranita():
    global posicion_triangulo
    glPushMatrix()
    glTranslatef(posicion_triangulo[0], posicion_triangulo[1],0.0)
    glScalef(0.5,0.5,0.0) 

    #Revisar colision
    if colisionando():
        glfw.set_window_should_close(window)
        glColor3f(1,0,0)
    else:
        glColor3f(98/255,198/255,0/255)

    #RANA
    glTranslatef(0.75,0.2,0.0)
    glBegin(GL_QUADS)

    glVertex3f(-0.76, -0.11, 0.0)
    glVertex3f(-0.76, -0.15, 0.0)
    glVertex3f(-0.80, -0.15, 0.0)
    glVertex3f(-0.80, -0.11, 0.0)

    glVertex3f(-0.74, -0.25, 0.0)
    glVertex3f(-0.74, -0.15, 0.0)
    glVertex3f(-0.82, -0.15, 0.0)
    glVertex3f(-0.82, -0.25, 0.0)

    glVertex3f(-0.72, -0.18, 0.0)
    glVertex3f(-0.72, -0.15, 0.0)
    glVertex3f(-0.84, -0.15, 0.0)
    glVertex3f(-0.84, -0.18, 0.0)

    glVertex3f(-0.72, -0.22, 0.0)
    glVertex3f(-0.72, -0.25, 0.0)
    glVertex3f(-0.84, -0.25, 0.0)
    glVertex3f(-0.84, -0.22, 0.0)

    glVertex3f(-0.72, -0.27, 0.0)
    glVertex3f(-0.72, -0.22, 0.0)
    glVertex3f(-0.74, -0.22, 0.0)
    glVertex3f(-0.74, -0.27, 0.0)

    glVertex3f(-0.82, -0.27, 0.0)
    glVertex3f(-0.82, -0.22, 0.0)
    glVertex3f(-0.84, -0.22, 0.0)
    glVertex3f(-0.84, -0.27, 0.0)

    glVertex3f(-0.82, -0.13, 0.0)
    glVertex3f(-0.82, -0.15, 0.0)
    glVertex3f(-0.84, -0.15, 0.0)
    glVertex3f(-0.84, -0.13, 0.0)

    glVertex3f(-0.72, -0.13, 0.0)
    glVertex3f(-0.72, -0.15, 0.0)
    glVertex3f(-0.74, -0.15, 0.0)
    glVertex3f(-0.74, -0.13, 0.0)
    glEnd()

    glPopMatrix()

#CARROS    
def draw_cuadrado():
    global posiciones_cuadrados

    for i in range(30):
        glPushMatrix()
        glTranslatef(posiciones_cuadrados[i][0], posiciones_cuadrados[i][1], 0.0)
        glBegin(GL_QUADS)
        
        glColor3f(234/255,129/255,25/255)
        glVertex3f(-0.05,0.05,0.0)
        glVertex3f(0.05,0.05,0.0)
        glVertex3f(0.05,-0.05,0.0)
        glVertex3f(-0.05,-0.05,0.0)
        glEnd()
        
        glBegin(GL_LINE_LOOP)
        glColor3f(0.0, 0.0, 0.0)
        glVertex3f(-0.05,0.05,0.0)
        glVertex3f(0.05,0.05,0.0)
        glVertex3f(0.05,-0.05,0.0)
        glVertex3f(-0.05,-0.05,0.0)
        glEnd()
        glPopMatrix()


def draw():
    draw_ranita()
    draw_cuadrado()

def background():

    #ground
    glBegin(GL_QUADS)
    glColor3f(61/255, 0/255, 198/255)
    glVertex3f(-1.0,2.0,0.0)
    glVertex3f(1.0,2.0,0.0)
    glVertex3f(1.0,-2.0,0.0)
    glVertex3f(-1.0,-2.0,0.0)
    glEnd()

    #Calle
    glBegin(GL_QUADS)
    glColor3f(35/255,149/255,121/255)
    glVertex3f(-1.0,0.9,0.0)
    glVertex3f(1.0,0.9,0.0)
    glVertex3f(1.0,-0.9,0.0)
    glVertex3f(-1.0,-0.9,0.0)
    glEnd()

    #Banqueta
    glBegin(GL_QUADS)
    glColor3f(61/255, 0/255, 198/255)
    glVertex3f(-1.0,-0.30,0.0)
    glVertex3f(1.0,-0.30,0.0)
    glVertex3f(1.0,-0.40,0.0)
    glVertex3f(-1.0,-0.40,0.0)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(61/255, 0/255, 198/255)
    glVertex3f(-1.0,0.30,0.0)
    glVertex3f(1.0,0.30,0.0)
    glVertex3f(1.0,0.40,0.0)
    glVertex3f(-1.0,0.40,0.0)
    glEnd()

    #Lineas calle
    glBegin(GL_QUADS)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(-1.0,0.025,0.0)
    glVertex3f(-0.8,0.025,0.0)
    glVertex3f(-0.8,-0.025,0.0)
    glVertex3f(-1.0,-0.025,0.0)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(-0.5,0.025,0.0)
    glVertex3f(-0.3,0.025,0.0)
    glVertex3f(-0.3,-0.025,0.0)
    glVertex3f(-0.5,-0.025,0.0)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(0.0,0.025,0.0)
    glVertex3f(0.2,0.025,0.0)
    glVertex3f(0.2,-0.025,0.0)
    glVertex3f(0.0,-0.025,0.0)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(0.5,0.025,0.0)
    glVertex3f(0.7,0.025,0.0)
    glVertex3f(0.7,-0.025,0.0)
    glVertex3f(0.5,-0.025,0.0)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(0.5,0.025,0.0)
    glVertex3f(0.7,0.025,0.0)
    glVertex3f(0.7,-0.025,0.0)
    glVertex3f(0.5,-0.025,0.0)
    glEnd()



def main():
    global window

    width = 600
    height = 700

    if not glfw.init():
        return

    window = glfw.create_window(width, height, "Frogger", None, None)

    glfw.window_hint(glfw.SAMPLES, 4)
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
    glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, GL_TRUE)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

    if not window:
        glfw.terminate()
        return

    glfw.make_context_current(window)

    glewExperimental = True

    if glewInit() != GLEW_OK:
        print("No se pudo inicializar GLEW")
        return

    version = glGetString(GL_VERSION)
    print(version)

    glfw.set_key_callback(window, key_callback)

    while not glfw.window_should_close(window):
        glClearColor(0.7,0.7,0.7,1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        background()
        actualizar()
        draw()

        glfw.poll_events()

        glfw.swap_buffers(window)

    glfw.destroy_window(window)
    glfw.terminate()

if __name__ == "__main__":
    main()