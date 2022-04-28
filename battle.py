from poke_team import PokeTeam
from sort import selectionSort

class Battle:
    def __init__(self,team1_name: str, team2_name: str) -> None:
        self.team1 = PokeTeam(team1_name)
        self.team2 = PokeTeam(team2_name)

    def set_mode_battle(self) -> str:
        self.team1.choose_team(0,None)
        self.team2.choose_team(0,None)        

        #while length of both trainers is not zero rounds will go
        #checks speed of first pokemon in party to determine attackers and defender
        #after each attack checks if a pokemon has fainted if so remove it
        #if a pokemon has fainted end the round
        #when the loop ends return result 


        while self.team1.team.length != 0 or self.team2.team.length != 0:
            pk_1 = self.team1.team.pop()
            pk_2 = self.team2.team.pop()
            
            self.round(pk_1,pk_2,0)
            
            if self.team1.team.length == 0 or self.team2.team.length == 0:
                break

        return self.win_check()

    def rotating_mode_battle(self) -> str:
        self.team1.choose_team(1,None)
        self.team2.choose_team(1,None)      

        while self.team1.team.length != 0 or self.team2.team.length != 0:
            pk_1 = self.team1.team.serve()
            pk_2 = self.team2.team.serve()
            
            self.round(pk_1,pk_2)
            
            if self.team1.team.length == 0 or self.team2.team.length == 0:
                break

        return self.win_check()

    def  optimised_mode_battle(self, criterion_team1: str, criterion_team2: str) ->str:
        self.team1.choose_team(2,criterion_team1)
        self.team2.choose_team(2,criterion_team2)   

        while self.team1.team.length != 0 or self.team2.team.length != 0:
            pk_1 = self.team1.team.pop()
            pk_2 = self.team2.team.pop()

            self.round(pk_1,pk_2)
            self.team1.team = selectionSort(self.team1.team,criterion_team1)
            self.team2.team = selectionSort(self.team2.team,criterion_team2)
            
            if self.team1.team.length == 0 or self.team2.team.length == 0:
                break

        return self.win_check()



    def battle(self,pk1,pk2) -> bool:
        #pk2 is taking damage, if True pk2 is dead
        pk2.calc_damage(pk1)
        if pk2.hp < 1: 
            return True
        else:
            return False
    
    def update(self,pk1,pk2,condition,team) -> None:
        #Conditions: 0 If  a fainted pokemon 
        #Conditions: 1 If  no fainted pokemon
        #Team 1 or 2, surviving pokemon
        if condition == 0:
            if team == 1:
                pk1.set_level(pk1.level + 1)
                self.team1.team.push(pk1)
            else:
                pk2.set_level(pk2.level + 1)
                self.team2.team.push(pk2)
        elif condition == 1:
            pk1.set_hp(pk1.hp-1)
            pk2.set_hp(pk2.hp-1)
            if pk1.hp < 0 and pk2.hp < 0:
                #if both faint leave
                pass
            elif pk1.hp > 0 or pk2.hp > 0:
                #if neither faint push back into respective teams
                self.team1.team.push(pk1)
                self.team2.team.push(pk2)
            else:
                if pk1.hp > 0:
                    self.team1.team.push(pk1)
                else:
                    self.team2.team.push(pk2)
       


    def round(self,pk1,pk2) -> None:
        
        if pk1.speed > pk2.speed:
            if self.battle(pk1, pk2):
    
                    self.update(pk1,pk2,0,1)
            else:
                if self.battle(pk2,pk1):
          
                        
                        self.update(pk1,pk2,0,2)
                else:
                    self.update(pk1,pk2,1,0)

        elif pk1.speed < pk2.speed:
            if self.battle(pk2, pk1):
   
                self.update(pk1,pk2,0,2)
            else:
                if self.battle(pk1,pk2):

                    self.update(pk1,pk2,0,1)
                else:
                    self.update(pk1,pk2,1,0)

        elif pk1.speed == pk2.speed:
            self.battle(pk1,pk2)
            self.battle(pk2,pk1)

            if pk1.hp <= 0 and pk2.hp <= 0:
                #both pokemon faint

                pass
            elif pk2.hp <= 0:
                #if pk2 is ko'd pk1 is pushed back into team 1
 
                self.update(pk1,pk2,0,1)
            elif pk1.hp <= 0:
                #if pk1 is ko'd pk2 is pushed back into team 2
  
                self.update(pk1,pk2,0,2)
            else:

                self.update(pk1,pk2,1,0)

    def win_check(self):
        if self.team1.team.length == 0 and self.team2.team.length ==0:
            return 'Draw'
        elif self.team1.team.length == 0:
            return self.team2.trainer_name
        elif self.team2.team.length == 0:
            return self.team1.trainer_name
        else: pass


