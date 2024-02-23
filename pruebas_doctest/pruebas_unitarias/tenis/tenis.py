#Funcionalidad para un partido de tenis
# Adalberto Cerrillo Vázquez
class tenis:
    #metodo para inicializar los datos
    def iniciar(self, p1,p2):
        # inicializamos el jugador 1
        self.player1 = p1
        # iniializamos el jugador 2
        self.player2 = p2
        # inicializamos el score
        self.scores = [0,0]
        # inicializamos una variable para manejar el jugador actual
        self.player_Actual = None
        # inicializamos una variable para manejar al rival
        self.rival_Actual = None
        # inicializamos una variable para determinar la ventaja
        self.ventaja = None
        # inicializamos una variable resultado
        self.resultado = "0-0"

    #metodo para devolver el marcador actual
    def score(self):
        return self.resultado
    
    #metodo para manejar las anotaciones del partido
    def points(self,player):
        # si se trata del primer jugador
        if player == self.player1:
            self.player_Actual = 0
            self.rival_Actual = 1
        else:
            self.player_Actual = 1
            self.rival_Actual = 0
        # checamos si el jugador tiene menos de 30 puntos
        if self.scores[self.player_Actual] < 30:
            # agregamos 15 puntos
            self.scores[self.player_Actual] +=15
            self.resultado = str(self.scores[0]) + "-" + str(self.scores[1])
        # si ya tiene 30 puntos
        elif self.scores[self.player_Actual] == 30:
            self.scores[self.player_Actual] +=10
            self.resultado = str(self.scores[0]) + "-" + str(self.scores[1])
        # si tiene 40 puntos
        else:
            # verificamos si hay un empate
            if self.scores[self.rival_Actual] == 40:
                # verificamos si el rival posee la ventaja 
                if self.ventaja == self.rival_Actual:
                    # si es así, se otorga el empate
                    self.ventaja = None
                    self.resultado = "Empate momentaneo"
                else:
                    # vemos si el player actual tiene la ventaja
                    if self.ventaja == self.player_Actual:
                        # si es así, ganamos la partida
                        if self.player_Actual == 0:
                            self.resultado =  self.player1 + " Win"
                        else:
                            self.resultado = self.player2 + " Win"
                    else:
                        # si no tenemos la ventaja, se otorga la ventaja
                        self.ventaja = self.player_Actual
                        if self.player_Actual == 0:
                            self.resultado =  "Ventaja " + self.player1
                        else:
                            self.resultado =  "Ventaja " + self.player2
            else:
                # si no tiene 40 puntos entonces ganamos
                if self.player_Actual == 0:
                    self.resultado = self.player1 + " Win"
                else:
                    self.resultado = self.player2 +  " Win"

        