"""
Trouve si une chaine de caractère est un palindrome
"""
#### Fonction secondaire


def ispalindrome(p):
    """
    Retourne True si la phrase est un palindrome
    """
    p = p.lower()
    phrase = p.maketrans("êéëèâàôûç","eeeeaaouc","-?' /!:[];,}{")
    p = p.translate(phrase)
    if p == p[::-1]:
        return True
    return False


#### Fonction principale


def main():
    """
    main
    """
    # vos appels à la fonction secondaire ici
    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))


if __name__ == "__main__":
    main()
