def ballenrij(lijst):
    n = len(lijst)
    nieuw = []
    aantal_b = 0
    for i in range(n):
        el = "🔴"
        if lijst[n - 1 - i] == 0 and aantal_b % 2 != 0:
            el = "🔵"
            aantal_b += 1
        elif lijst[n - 1 - i] == 1 and aantal_b % 2 != 1:
            el = "🔵"
            aantal_b += 1
        nieuw.append(el)
    
    # nu omdraaien
    reverse = []
    for i in range(n):
        reverse.append(nieuw[n - 1 - i])
            
    return reverse
