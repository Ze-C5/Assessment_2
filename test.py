from pokemon import Charmander, Bulbasaur,Squirtle
from queue_adt import CircularQueue



def selectionSort2(team, criteria):
    size = team.length

    def valueassign(poke):
        if isinstance(poke,Charmander):
            return 1
        elif isinstance(poke,Bulbasaur):
            return 2
        elif isinstance(poke,Squirtle):
            return 3
        else:
            pass

    for s in range(size):
        idx = s
         
        for i in range(s + 1, size):
             
            # For sorting in descending order
            # for minimum element in each loop
            if getattr(team.array[i],criteria) > getattr(team.array[idx],criteria):
                idx = i

            elif getattr(team.array[i],criteria) == getattr(team.array[idx],criteria):
                #Charmander = 1, Squirtle = 2, Bulbasaur = 3
                hold_1 = valueassign(team.array[i])
                hold_2 = valueassign(team.array[idx])

                if hold_1 < hold_2:
                    idx = i
                # Arranging min at the correct position
                    (team.array[s], team.array[idx]) = (team.array[idx], team.array[s])
                else:
                    pass
 
        # Arranging min at the correct position
        (team.array[s], team.array[idx]) = (team.array[idx], team.array[s])


        


team = CircularQueue(6)

team.append(Bulbasaur())
team.append(Bulbasaur())
team.append(Squirtle())



selectionSort2(team,'level')
for i in range(team.length):
    print(team.array[i])