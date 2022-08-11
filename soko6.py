class Sokoban:
    
    #variables globales
    mapa =[]

    nivel = 0
    num_metas = 0 
    mono = 0
    fila = 2 
    posicion = 1 #posicion del mono 
    m = 1
    jalar = False 
    
##########################################################################
################ IMPORTAR MAPA ###########################################
##########################################################################
    
    def __init__(self): #constructor
        print 'sokoban'
        
    def game_mapa(self):
        file = open(str(self.nivel) +'.demo.py','r')
        for line in file:
            fila = []
            for c in line[:-1]:
                fila.append(int(c))
            self.mapa.append(fila)
    def print_mapa(self):
        for f in range(len(self.mapa)):
            line = ' '
            for c in range(len(self.mapa[f])):
                line +=str(self.mapa[f][c]) + ' '
            print line 
##########################################################################
##########################################################################

#contador##

    def contar_metas(self):
        for fila in range (12):
             for columna in range (12):
                if self.mapa[fila][columna]==4:
                   self.num_metas+=1
####################### encontrar mono #############################
    def encontrar_mono(self):
        for fila in range(12):
            for columna in range(12):
                if self.mapa[fila][columna] == 0:
                   self.fila = fila
                   self.columna=columna
            
#TODO ESTE PROGRAMA ES PARA MOVERSE A LA DERECHA             
    def mover_derecha(self):
        if self.mapa[self.fila][self.posicion + 1] == 1: #validar espacio
            self.mapa[self.fila][self.posicion + 1] = 0 # mover monito 
            self.mapa[self.fila][self.posicion] = self.m # espacio
            self.posicion += 1 #actualizar posicion 
            self.m = 1
        elif self.mapa[self.fila][self.posicion + 1] == 4:
            self.mapa[self.fila][self.posicion +1] = 0
            self.mapa[self.fila][self.posicion] = self.m # espacio
            self.posicion += 1  #actualizar posicion 
            self.m = 4
    def mover_caja(self):
        if self.mapa[self.fila][self.posicion + 1] == 3 and self.mapa[self.fila][self.posicion + 2] == 1: #empujar caja hacia la derecha 
            self.mapa[self.fila][self.posicion+2] = 3
            self.mapa[self.fila][self.posicion + 1] = 0
            self.mapa[self.fila][self.posicion] = self.m
            self.posicion += 1
            self.m = 1
        elif self.mapa[self.fila][self.posicion + 1] == 3 and self.mapa[self.fila][self.posicion + 2] == 4: # para meterlo en la meta
            self.mapa[self.fila][self.posicion + 2]=5
            self.mapa[self.fila][self.posicion + 1]=0
            self.mapa[self.fila][self.posicion]= self.m
            self.posicion += 1 
            self.m = 1
            self.num_metas -=1
        elif self.mapa[self.fila][self.posicion + 1] == 5 and self.mapa[self.fila][self.posicion + 2] == 1:
            self.mapa[self.fila][self.posicion + 2]= 3
            self.mapa[self.fila][self.posicion + 1]= 0
            self.mapa[self.fila][self.posicion]= self.m
            self.posicion += 1
            self.m = 4
###############################################################################################################################       
##############################################################################################################################
            
#'TODO ESTE PROGRAMA SE MUEVE HACIA LA IZQUIERDA'
    def mover_izquierda(self):
        if self.mapa[self.fila][self.posicion - 1] == 1: #validar espacio
            self.mapa[self.fila][self.posicion - 1] = 0 # mover monito 
            self.mapa[self.fila][self.posicion] = self.m # espacio
            self.posicion -= 1 #actualizar posicion 
            self.m =1
        elif self.mapa[self.fila][self.posicion - 1] == 4:
            self.mapa[self.fila][self.posicion -1] = 0
            self.mapa[self.fila][self.posicion] = self.m # espacio
            self.posicion -= 1  #actualizar posicion 
            self.m = 4
    def mover_caja2(self):
        if self.mapa[self.fila][self.posicion - 1] == 3 and self.mapa[self.fila][self.posicion - 2] == 1: #empujar caja hacia la derecha 
            self.mapa[self.fila][self.posicion-2] = 3
            self.mapa[self.fila][self.posicion - 1] = 0
            self.mapa[self.fila][self.posicion] = self.m
            self.posicion -= 1
            self.m = 1
        elif self.mapa[self.fila][self.posicion - 1] == 3 and self.mapa[self.fila][self.posicion - 2] == 4: # para meterlo en la meta
            self.mapa[self.fila][self.posicion - 2]=5
            self.mapa[self.fila][self.posicion - 1]=0
            self.mapa[self.fila][self.posicion]=self.m
            self.posicion -= 1
            self.m = 1
            self.num_metas -=1 
        elif self.mapa[self.fila][self.posicion - 1] == 5 and self.mapa[self.fila][self.posicion - 2] == 1:
            self.mapa[self.fila][self.posicion - 2]= 3
            self.mapa[self.fila][self.posicion - 1]= 0
            self.mapa[self.fila][self.posicion]= self.m
            self.posicion -= 1
            self.m = 4 
            
#####################################################################################################################           
#####################################################################################################################
            
#mover hacia arriba 
    def mover_arriba(self):
        if self.mapa[self.fila-1][self.posicion] == 1: #validar espacio
            self.mapa[self.fila-1][self.posicion] = 0 # mover monito 
            self.mapa[self.fila][self.posicion] = self.m # espacio
            self.fila -= 1 #actualizar posicion
            self.m = 1
        elif self.mapa[self.fila-1][self.posicion] == 4:
            self.mapa[self.fila-1][self.posicion] = 0 
            self.mapa[self.fila][self.posicion] = self.m 
            self.fila -= 1
            self.m = 4
            
    def mover_cajas(self):
        if self.mapa[self.fila- 1][self.posicion] == 3 and self.mapa[self.fila-2][self.posicion] == 1: #empujar caja hacia la derecha 
            self.mapa[self.fila-2][self.posicion] = 3
            self.mapa[self.fila-1][self.posicion] = 0
            self.mapa[self.fila][self.posicion] = 1
            self.fila -= 1
        elif self.mapa[self.fila-1][self.posicion ] == 3 and self.mapa[self.fila-2][self.posicion] == 4: # para meterlo en la meta
            self.mapa[self.fila-2][self.posicion ]=5
            self.mapa[self.fila-1][self.posicion ]=0
            self.mapa[self.fila][self.posicion]=1
            self.fila -= 1
            self.num_metas -=1  
        elif self.mapa[self.fila-1][self.posicion ] == 5 and self.mapa[self.fila-2][self.posicion] == 1: 
            self.mapa[self.fila-2][self.posicion ]=3
            self.mapa[self.fila-1][self.posicion ]=0
            self.mapa[self.fila][self.posicion]=self.m
            self.fila -= 1 
            self.m = 4
         
    #####################################################################
    #####################################################################
        
        
        #mover hacia abajo 
    def mover_abajo(self):
        if self.mapa[self.fila+1][self.posicion] == 1: #validar espacio
            self.mapa[self.fila+1][self.posicion] = 0 # mover monito 
            self.mapa[self.fila][self.posicion] = self.m # espacio
            self.fila += 1 #actualizar posicion
            self.m = 1
        elif self.mapa[self.fila+1][self.posicion] == 4: 
            self.mapa[self.fila+1][self.posicion] = 0 
            self.mapa[self.fila][self.posicion] = self.m 
            self.fila += 1
            self.m = 4
    def mover_cajas1(self):
        if self.mapa[self.fila+1][self.posicion] == 3 and self.mapa[self.fila+2][self.posicion] == 1: #empujar caja hacia la derecha 
            self.mapa[self.fila+2][self.posicion] = 3
            self.mapa[self.fila+1][self.posicion] = 0
            self.mapa[self.fila][self.posicion] = 1
            self.fila += 1
        elif self.mapa[self.fila+1][self.posicion ] == 3 and self.mapa[self.fila+2][self.posicion] == 4: # para meterlo en la meta
            self.mapa[self.fila+2][self.posicion ]=5
            self.mapa[self.fila+1][self.posicion ]=0
            self.mapa[self.fila][self.posicion]=1
            self.fila += 1
            self.num_metas -=1 
        elif self.mapa[self.fila+1][self.posicion ] == 5 and self.mapa[self.fila+2][self.posicion] == 1: 
            self.mapa[self.fila+2][self.posicion ]=3
            self.mapa[self.fila+1][self.posicion ]=0
            self.mapa[self.fila][self.posicion]=self.m
            self.fila += 1 
            self.m = 4
    
    
# JALAR CAJAS ################################################
    def Jalar_caja(self):
        if self.mapa[self.fila][self.posicion - 1]== 1 and self.mapa[self.fila][self.posicion + 1]== 3:
            self.jalar = True
            if self.jalar == True:
                self.mapa[self.fila][self.posicion-1] =0 
                self.mapa[self.fila][self.posicion+1] = 1  
                self.mapa[self.fila][self.posicion]=3 
                self.posicion -= 1
                 
        elif self.mapa[self.fila][self.posicion + 1]== 1 and self.mapa[self.fila][self.posicion - 1]== 3:
            self.jalar = True
            if self.jalar == True:
                self.mapa[self.fila][self.posicion+1] =0 
                self.mapa[self.fila][self.posicion-1] = 1  
                self.mapa[self.fila][self.posicion]=3 
                self.posicion += 1
                
        elif self.mapa[self.fila-1][self.posicion]== 1 and self.mapa[self.fila+1][self.posicion]== 3:
            self.jalar = True
            if self.jalar == True:
                self.mapa[self.fila-1][self.posicion] =0 
                self.mapa[self.fila+1][self.posicion] = 1  
                self.mapa[self.fila][self.posicion]=3
                self.fila -= 1
                
        elif self.mapa[self.fila+1][self.posicion]== 1 and self.mapa[self.fila-1][self.posicion]== 3:
            self.jalar = True
            if self.jalar == True:
                self.mapa[self.fila+1][self.posicion] =0 
                self.mapa[self.fila-1][self.posicion] = 1  
                self.mapa[self.fila][self.posicion]=3 
                self.fila += 1
                
                
                
#  def superado(self):
        #self
            
############################################################################
############################################################################
############################################################################
################ METODOS DEL JUEGO PARA DISFRUTARLO ########################
############################################################################
############################################################################

#str(nivel)
   # def iniciar_juego():
    #    cargar_mapa(2)
     #   encontrar_mono()
      #  contar_metas()
       # imprimir_mapa()



            
objeto = Sokoban()
objeto.game_mapa()
objeto.contar_metas()
objeto.encontrar_mono()
#objeto = iniciar_juego()

while True:
    objeto.print_mapa()
    print 'monito:' + str(objeto.posicion) # imprimir posicion
    print 'metas:' + str(objeto.num_metas)
    movimiento = raw_input('d - derecha\na - izquierda\nw-arriba\ns-abajo\nj-jalar:')
    if movimiento == 'd':
        objeto.mover_derecha()
        objeto.mover_caja()
    elif movimiento == 'a':
        objeto.mover_izquierda()
        objeto.mover_caja2()
    elif movimiento == 'w':
        objeto.mover_arriba()
        objeto.mover_cajas()
    elif movimiento == 's':
        objeto.mover_abajo()
        objeto.mover_cajas1()
    elif movimiento == 'j':
        objeto.Jalar_caja()
    if objeto.num_metas == 0:
        objeto.nivel = 0
        print 'superado nivel '
        break 
        
        
                   
