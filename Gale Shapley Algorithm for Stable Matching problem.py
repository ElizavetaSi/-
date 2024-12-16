# Реализация алгоритма Гэйла — Шепли для задачи стабильных бракосочетаний
def stable_marriage(men_preferences, women_preferences):
    
    free_men = list(men_preferences.keys())

    engagements = {}
    women_engaged_to = {}
    proposal_index = {man: 0 for man in men_preferences}

    while free_men:
        man = free_men[0]
        
        woman = men_preferences[man][proposal_index[man]]
        proposal_index[man] += 1

        if woman not in women_engaged_to:
            engagements[man] = woman
            women_engaged_to[woman] = man
            free_men.pop(0)
        else:
            current_partner = women_engaged_to[woman]
            if women_preferences[woman].index(man) < women_preferences[woman].index(current_partner):
                engagements[man] = woman
                women_engaged_to[woman] = man
                free_men.pop(0)
                free_men.append(current_partner)
                del engagements[current_partner]
            else:
                pass

    return engagements

men_preferences = {
    "m1": ["w1", "w2", "w3"],
    "m2": ["w2", "w1", "w3"],
    "m3": ["w1", "w3", "w2"],
}

women_preferences = {
    "w1": ["m2", "m1", "m3"],
    "w2": ["m1", "m2", "m3"],
    "w3": ["m1", "m3", "m2"],
}

stable_pairs = stable_marriage(men_preferences, women_preferences)
print("Стабильные пары:", stable_pairs)
