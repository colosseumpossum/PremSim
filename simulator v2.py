import random
import itertools

teams = {
    "Arsenal": {"attack": 8, "defense": 10, "midfield": 10},
    "Manchester City": {"attack": 10, "defense": 9, "midfield": 10},
    "Manchester United": {"attack": 8, "defense": 9, "midfield": 7},
    "Liverpool": {"attack": 8, "defense": 8, "midfield": 7},
    "Aston Villa": {"attack": 7, "defense": 7, "midfield": 8},
    "Brighton": {"attack": 7, "defense": 8, "midfield": 7},
    "Bornemouth": {"attack": 8, "defense": 6, "midfield": 7},
    "Chelsea": {"attack": 8, "defense": 7, "midfield": 7},
    "Brentford": {"attack": 7, "defense": 7, "midfield": 6},
    "Fulham": {"attack": 7, "defense": 7, "midfield": 7},
    "Everton": {"attack": 6, "defense": 7, "midfield": 7},
    "Sunderland": {"attack": 6, "defense": 7, "midfield": 7},
    "Crystal Palace": {"attack": 6, "defense": 8, "midfield": 7},
    "Leeds United": {"attack": 7, "defense": 6, "midfield": 7},
    "Newcastle United": {"attack": 7, "defense": 6, "midfield": 8},
    "Nottingham Forest": {"attack": 6, "defense": 7, "midfield": 7},
    "West Ham United": {"attack": 6, "defense": 5, "midfield": 6},
    "Tottenham Hotspur": {"attack": 5, "defense": 5, "midfield": 6},
    "Burnley": {"attack": 5, "defense": 4, "midfield": 5},
    "Wolves": {"attack": 4, "defense": 4, "midfield": 4},
}

league_standings = {
   team: {"wins": 0, "draws": 0, "losses": 0, "points": 0, "played": 0}
   for team in teams
}

class Player:
   def __init__ (self, name, attack, defense, midfield):
      self.name = name
      self.attack = attack
      self.defense = defense
      self.midfield = midfield
    
      self.is_injured = False
      self.injury_proneness = 0
      self.injury_time = 0
       
   def check_injury(self):
      injury_chance = random.randint(0, 200)
      
      if injury_chance - self.injury_proneness <= 1:
         self.injury_time = 30
         self.is_injured = True
         self.injury_proneness += 5
            
      elif injury_chance - self.injury_proneness <= 5:
         self.injury_time = 10
         self.is_injured = True
         self.injury_proneness += 3
             
      elif injury_chance - self.injury_proneness <= 10:
         self.injury_time = 3
         self.is_injured = True
         self.injury_proneness += 1

      def injury_count(self):
         if self.is_injury:
            self.filler += 1
          
             
      def current_stats(self):
         if self.is_injured:
            if self.injury_time <= 3:
               return {"attack": name["attack"/2], "defense": name["defense"/2], "midfield": name["midfield"/2]}
            else:
               return {"attack": 0, "defense": 0, "midfield": 0}
         
         return {
         "attack": self.attack,
         "defense": self.defense,
         "midfield": self.midfield
         }
          
             
class Match:
   def __init__(self,team_1_name, team_1_stats, team_2_name, team_2_stats):
      self.team_1_name = team_1_name
      self.team_1_stats = team_1_stats
      self.team_2_name = team_2_name
      self.team_2_stats = team_2_stats
    
   def play(self):
      t1_score = 0
      t2_score = 0
      if self.team_1_stats["attack"] > self.team_2_stats["defense"]:
         t1_score += 1
      elif self.team_1_stats["attack"] < self.team_2_stats["defense"]:
         t2_score += 1
          
      if self.team_1_stats["defense"] > self.team_2_stats["attack"]:
         t1_score += 1
      elif self.team_1_stats["defense"] < self.team_2_stats["attack"]:
         t2_score += 1
           
      if self.team_1_stats["midfield"] > self.team_2_stats["midfield"]:
         t1_score += 1
      elif self.team_1_stats["midfield"] < self.team_2_stats["midfield"]:
         t2_score += 1
          
      league_standings[self.team_1_name]["played"] += 1
      league_standings[self.team_2_name]["played"] += 1

      if t1_score > t2_score:
         league_standings[self.team_1_name]["points"] += 3
         league_standings[self.team_1_name]["wins"] += 1
         league_standings[self.team_2_name]["losses"] += 1
         return 

      if t1_score == t2_score:
         league_standings[self.team_2_name]["points"] += 1
         league_standings[self.team_1_name]["points"] += 1
         league_standings[self.team_2_name]["draws"] += 1
         league_standings[self.team_1_name]["draws"] += 1
         return
      
      league_standings[self.team_2_name]["points"] += 3
      league_standings[self.team_2_name]["wins"] += 1
      league_standings[self.team_1_name]["losses"] += 1
   
weeks_to_simulate = int(input("How many game weeks to simulate? "))

games = list(itertools.combinations(teams, 2))
games = games * 2
random.shuffle(games)
games_to_play = games[:10 * weeks_to_simulate]

if weeks_to_simulate > len(games) // 10:
   print(f"There are only {len(games)} game weeks in a season.")
else:
   for i in range(0, len(games_to_play)):
      team_1_name, team_2_name = games[i]
      team_1_stats = teams[team_1_name]
      team_2_stats = teams[team_2_name]
      game = Match(team_1_name, team_1_stats, team_2_name, team_2_stats)
      game.play()

final_table = sorted(league_standings.items(), key=lambda team_data: team_data[1]["points"], reverse = True)

table_width = 80
divider = "-" * table_width
print(divider)
print(f"| {"Position":<8} | {"Teams":<20} | {"Wins":<6} | {"Draws":<6} | {"Losses":<6} | {"Points":<6} | {"Played":<7} |")
print(divider)
for position, team in enumerate(final_table, start=1):
   name = team[0]
   s = team[1]
   print(f"| {position:<8} | {name:<20} | {s['wins']:<6} | {s['draws']:<6} | {s['losses']:<6} | {s['points']:<6} | {s['played']:<7} |")
print(divider)
    