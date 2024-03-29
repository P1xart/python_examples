# Словарь (Мапа или карта) имеет конструкцию {<Ключ:Значение>, <Ключ:Значение>, <Ключ:Значение>}
sites_map = {"vk":"vk.com", "yt":"youtube.com", "ok":"ok.ru", 13.14:"Число Pi"}
# В словаре нельзя обратиться по индексу, для этого существуют ключи, которые как и индекс возвращают значения присвоенные ключам.
print(sites_map["13.14"]) # Число Pi
# Для добавления элемента в словарь нужно применить конструкцию <имя_словаря>[<ключ>] = <значение>
sites_map["tw"] = "twitter.com"
print(sites_map) # {'vk': 'vk.com', 'yt': 'youtube.com', 'ok': 'ok.ru', 'tw': 'twitter.com'}
# Для удаления элемента словаря существует ключевое слово del
del sites_map["ok"]
print(sites_map) # {'vk': 'vk.com', 'yt': 'youtube.com', 'tw': 'twitter.com'}
