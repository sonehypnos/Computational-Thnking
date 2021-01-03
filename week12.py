shopping_list = ['牛奶', '蛋', '咖啡豆', '西瓜', '鳳梨']
print(shopping_list)


season = "1995-1996"
team = "Chicago Bulls"
coach = "Phil Jackson"
records = [72, 10]
starting = ["Ron Harper", "Michael Jordan", "Scottie Pippen", "Dennis Rodman", "Luc Longley"]
champion = True

best_NBA = list((season, team, coach, records, starting,champion))
print(best_NBA)
['1995-1996', 'Chicago Bulls', 'Phil Jackson', [72, 10], ['Ron Harper', 'Michael Jordan', 'Scottie Pippen', 'Dennis Rodman','Luc Longley'], True]
print(type(best_NBA))


print(best_NBA[-2])
['Ron Harper', 'Michael Jordan', 'Scottie Pippen', 'Dennis Rodman', 'Luc Longley']
print(best_NBA[1:4])
['Chicago Bulls', 'Phil Jackson', [72, 10]]