#pip3 install python-whois

import whois

def check_domain_availability(domain):
    try:
        w = whois.whois(domain)
        if w.status is None:
            return "Le domaine '{}' est disponible.".format(domain)
        else:
            return "Le domaine '{}' est déjà utilisé.".format(domain)
    except whois.parser.PywhoisError:
        return "Erreur : Impossible de vérifier le domaine '{}'.".format(domain)


