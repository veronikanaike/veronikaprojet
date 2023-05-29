# veronikaBilighaprojet
 AUTOMATISATION DES ACTIONS RED TEAM 
 
L'objectif principal de ce projet est de rechercher et collecter des informations spécifiques pour automatiser les actions de sécurité, cela se fera par le biais d'un script developpé en langage python. le but premier de cet outil est de permettre aux entreprises, aux clients de gagner du temps face aux cyberattaques qu'ils rencontrent au quotidien et d'anticiper leurs remediations . c'est un outil qui permet de scanner le reseau , detecter les vulneralbités et les exploiter .

En ce qui concerne le reseau , j'ai utilisé la fonction NMAP : qui est un scanner de ports libre , il permet de detecter les ports ouverts , identifier les infomations sur le systeme d'exploitation d'un ordinateur distant . j'ai choisi NMAP aussi parce que il utilise le langage de programmation Python ce qui est favorable avec mon outil puisqu'il est developpé en python . En outre , j'ai choisi d'ajouter  la fonction METASPLOIT : son but  est de fournir des informations sur les vulnérabilités de sytèmes informatiques , d'aider à la pénétration et au developpement  de signatures pour les systèmes de detection d'intrusion . 

J'ai installé une machine virtuelle windows server où j'ai crée un domaine nommé VERONIKA.LOCAL , et attribué l'adresse ip :  , ensuite j'ai crée un user : william.stephan ; Mot de passe : Bonjour33 

Pour editer et interpreter mon code j'ai eu besoin de visual studio code , de python  . 

EXPLICATION DU SCRIPT 

- tout d'abord je vais specifier l'interpreteur que je vais executer ( python3) afin que le script s'execute rapidement  
- on va definir une fonction principale où on va lister les options  et donner le choix à un utilisateur de choisir une lettre et lorqu'il va choisir une lettre  il sera redirigé vers une fonction 
- afin de pouvoir utiliser la fonction nmap , on va devoir installer la librairie , j'ai mis vc ( pour scan )
- on va demander à l'utilisateur de rentrer l'adresse ip , les ports 
