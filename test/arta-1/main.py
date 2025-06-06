from arta import RulesEngine

eng = RulesEngine(config_path="")

applicants = [
    {
        "id": 1,
        "name": "Superman",
        "civilian_name": "Clark Kent",
        "age": None,
        "city": "Metropolis",
        "language": "english",
        "power": "fly",
        "favorite_meal": "Spinach",
        "secret_weakness": "Kryptonite",
        "weapons": [],
    },
    {
        "id": 2,
        "name": "Batman",
        "civilian_name": "Bruce Wayne",
        "age": 33,
        "city": "Gotham City",
        "language": "english",
        "power": "strength",
        "favorite_meal": None,
        "secret_weakness": "Feel alone",
        "weapons": ["Hands", "Batarang"],
    },
    {
        "id": 3,
        "name": "Wonder Woman",
        "civilian_name": "Diana Prince",
        "age": 5000,
        "city": "Island of Themyscira",
        "language": "french",
        "power": "strength",
        "favorite_meal": None,
        "secret_weakness": "Lost faith in humanity",
        "weapons": ["Magic lasso", "Bulletproof bracelets", "Sword", "Shield"],
    },
]

result = eng.apply_rules(input_data=applicants[2])

print(result)
