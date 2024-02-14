#create a Pokemon
class Pokemon:
    def __init__(Self , name , primary_type , max_hp):
        Self.name = name
        Self.primary_type = primary_type
        Self.max_hp = max_hp
        Self.hp = max_hp 

    def __str__(Self):
        return f"{Self.name} ({Self.primary_type}): {Self.hp}/{Self.max_hp}"



    def feed(self):
        if self.hp < self.max_hp:
            self.hp += 1
            print(f"{self.name} has now {self.hp} HP.")
        else:
            print(f"{self.name} is full.")



    def battle(self , other):
        self.typewheel(self.primary_type , other.primary_type)
        result = self.typewheel(self.primary_type , other.primary_type)
        #depending on the result  , have effects
        if result == "lose":
            self.hp -= 10
            print(f"{self.name} lost and now has {self.hp} HP.")
        print(f"{self.name} fought {other.name} and the result is a {result}")
        # call typewheel

    @staticmethod
    def typewheel(type1,type2):
        result = {0 : "lose" , 1 : "win" , -1:"tie"}
        # mapping between types and result conditions
        game_map = {"water" : 0 , "fire":1 , "grass" : 2}
        # implement win-lose matrix
        wl_matrix = [
            [-1 , 1 , 0], # water
            [0 , -1 , 1], # fire
            [1 , 0 , -1], # grass
        ]

        #declare a winner
        wl_result = wl_matrix[game_map[type1]][game_map[type2]]
    
        return result[wl_result]






if __name__ == '__main__':
    bulbi = Pokemon(name="bulbasaur",primary_type="grass" , max_hp = 100)
    charm = Pokemon(name="charmender",primary_type="fire" , max_hp=150)
    bulbi.battle(charm)