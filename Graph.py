from sqlalchemy import null


southwest_capitals = {'Pheonix': {'Santa Fe': [481, 'I-17, I-40, I-25'], 'Oklahoma City': [1006, "I-17, I-40"], 'Austin': [1051, "I-10, I-410, I-35"]},
                      'Santa Fe': {'Pheonix': [481, 'I-25, I-40, I-17'], 'Oklahoma City': [535, "I-40"], 'Austin': [957, "I-25, I-10, I-35"]},
                      'Oklahoma City': {'Santa Fe': [535, "I-40"], 'Pheonix': [1006, "I-40, I-17"], 'Austin': [388, "I-35"]},
                      'Austin': {'Santa Fe': [957, "I-35, I-10, I-25"], 'Oklahoma City': [388, "I-35"], 'Pheonix': [1051, "I-35, I-410, I-10"]},
                      }

# [[PHX, SFE, OKC, AUS]]
#

Graph = [[0, 481, 1006, 1051], [481, 0, 535, 957],
         [1006, 535, 0, 388], [1051, 957, 388, 0]]

midwest_capitals = {'Des Moines': {'Springfield': [337, '<I-80>, <I-74>, <I-155>'], 'Indianapolis': [477, '<I-80>, <I-74>, <I-465>'], 'Lansing': [], 'St. Paul': [], 'Jefferson City': [], 'Bismarck': [], 'Lincoln': [], 'Columbus': [], 'Pierre': [], 'Madison': []},
                    'Springfield': {'Des Moines': [337, ' <I-155>, <I-74>, <I-80>'], 'Indianapolis': [213, '<I-72>, <I-74>, <I-465>'], 'Lansing': [392, '<I-55>, <I-80>,  <I-94>, <I-69>, <I-94>'], 'St. Paul': [520, '<I-55>, <I-39>, <I-90>, <I-94>'], 'Jefferson City': [], 'Bismarck': [], 'Lincoln': [], 'Columbus': [], 'Pierre': [], 'Madison': []},
                    'Indianapolis': {'Springfield': [213, '<I-465>, <I-74>, <I-72>'], 'Des Moines': [477, '<I-465>, <I-74>, <I-80>'], 'Lansing': [], 'St. Paul': [], 'Jefferson City': [], 'Bismarck': [], 'Lincoln': [], 'Columbus': [], 'Pierre': [], 'Madison': []},
                    'Lansing': {'Springfield': [392, '<I-69>, <I-94>, <I-80>, <I-55>'], 'Indianapolis': [], 'Des Moines': [], 'St. Paul': [], 'Jefferson City': [], 'Bismarck': [], 'Lincoln': [], 'Columbus': [], 'Pierre': [], 'Madison': []},
                    'St. Paul': {'Springfield': [520, '<I-94>, <I-90>, <I-39>, <I-55>'], 'Indianapolis': [], 'Lansing': [], 'Des Moines': [], 'Jefferson City': [], 'Bismarck': [], 'Lincoln': [], 'Columbus': [], 'Pierre': [], 'Madison': []},
                    'Jefferson City': {'Springfield': [220, '<I-70>, <I-270>, <I-55>'], 'Indianapolis': [], 'Lansing': [], 'St. Paul': [], 'Des Moines': [], 'Bismarck': [], 'Lincoln': [], 'Columbus': [], 'Pierre': [], 'Madison': []},
                    'Bismarck': {'Springfield': [952, '<I-94>, <I-90>, <I-39>, <I-55>'], 'Indianapolis': [], 'Lansing': [], 'St. Paul': [], 'Jefferson City': [], 'Des Moines': [], 'Lincoln': [], 'Columbus': [], 'Pierre': [], 'Madison': []},
                    'Lincoln': {'Springfield': [530, '<I-80>, <I-74>, <I-155>, <I-55>'], 'Indianapolis': [], 'Lansing': [], 'St. Paul': [], 'Jefferson City': [], 'Bismarck': [], 'Des Moines': [], 'Columbus': [], 'Pierre': [], 'Madison': []},
                    'Columbus': {'Springfield': [], 'Indianapolis': [], 'Lansing': [], 'St. Paul': [], 'Jefferson City': [], 'Bismarck': [], 'Lincoln': [], 'Des Moines': [], 'Pierre': [], 'Madison': []},
                    'Pierre': {'Springfield': [], 'Indianapolis': [], 'Lansing': [], 'St. Paul': [], 'Jefferson City': [], 'Bismarck': [], 'Lincoln': [], 'Columbus': [], 'Des Moines': [], 'Madison': []},
                    'Madison': {'Springfield': [], 'Indianapolis': [], 'Lansing': [], 'St. Paul': [], 'Jefferson City': [], 'Bismarck': [], 'Lincoln': [], 'Columbus': [], 'Pierre': [], 'Des Moines': []},
                    }
