Exercice de maintenance d'un programme
======================================

Le présent exercice reproduit le jeu du pendu.

Vous allez le corriger, le publier et l'améliorer.

Au cours de cet exercice, vous allez :

- manipuler un gestionnaire de ticket;
- manipuler un système de gestion de version, en l'occurence git ;
- résoudre des bugs, dans une démarche de reproduction par des tests unitaires ;
- intégrer ces tests au sein de l'intégration continue de gitlab ;

Voici plusieurs tâches à réaliser. A chaque fois, respectez une procédure de revue pour développer du code:

1. Ouvrir une _issue_ pour documenter le problème
2. la personne qui résout le problème s'assigne l'issue;

    Elle résout l'issue dans une branche dédiée, puis "pousse" la branche vers le serveur:

    ```bash
    # se remettre dans la branche master
    git checkout master
    # remettre à jour la branche master avec la branche master sur le dépôt distant (nommé `origin`): 
    git pull origin master
    # créer une nouvelle branche (x est le numéro de l'issue)
    git checkout -b x-description-de-ma-branche
    # résoudre le problème
    # puis commiter les fichiers modifiés
    git add <mon fichier>
    git commit
    # puis on pousse le travail vers le serveur "origin", en ajoutant le nom de la branche
    # le paramètre "set-upstream" permet de lier la branche locale à la branche distante,
    # ce "set-upstream" permettra d'utiliser le git pull / git push sans autres arguments
    # les prochaines fois:
    git push --set-upstream origin x-description-de-ma-branche
    ```

3. une fois résolue, le·la développeur·euse crée une pull request, sur l'interface web.

    Au moment de créer la pull request, vérifiez qu'il n'y a pas de conflit avec la branche master, ou que votre travail est à jour vis-à-vis de master. Si ça n'est pas le cas, voici les commandes:

    ```bash
    # vérifiez que vous êtes dans votre branche (git status et éventuellement git checkout x-nom-de-ma-branche)
    git pull origin master
    # résolvez les conflits. S'il y en a, il faut commiter les fichiers:
    git add <fichier_en_conflit> # uniquement si conflit, à répéter pour chaque fichier
    git commit # uniquement si conflit
    # renvoyer la branche mise à jour vers le server:
    git push
    ```
4. Un·e autre développeur·euse vérifie la MR. (A priori, on ne valide pas ses propres pull request)

    Si l'exécution du code est nécessaire, github montre quelles instructions utiliser dans son interface.

5. Si la PR est correcte, elle peut être fusionnée.

## Voici les premières issues à créer:

Coordonnez-vous oralement pour créer les issues.

Chaque issue doit être suffisamment documentée. Au moins deux titres doivent être créés:

* une description du problème;
* le comportement attendu.

Rédigez vos issues de manières à ce qu'elles soient compréhensibles par vos collègues.

### Corriger la fonction `is_guessed`

Le programme contient un bug: la fonction `is_guessed` n'est pas correcte: elle tient compare le nombre de caractères, mais pas les lettres. Dès lors, un mot qui a deux fois les mêmes lettres n'est pas trouvé.

### Des tests sont manquants

Listez les fonctions à tester dans l'issue que vous créerez.

### Configurez l'intégration continue dans github

Configurez l'intégration continue pour que:

- les tests soient effectués automatiquement après chaque commit;
- la PEP8 soit vérifiée après chaque commit;

Vous pouvez vous aider d'une IA pour générer le code nécessaire.

### De la documentation est manquante

Documentez les fonctions et classes.

### Ajouter une fonctionnalité: choisir le mot à deviner

Le mot à deviner est, pour le moment, inscrit "en dur" dans le fichier.

Il serait plus amusant que le mot soit choisi dans une liste de mots existants.

### Réfléchissez à de nouvelles fonctionnalités

À chaque fois, utilisez le gestionnaire de ticket pour discuter de vos fonctionnalités.

Exemples :

- nombre d'essais limités ;
- afficher un dessin de pendu dans le terminal ;
- ...

## Améliorez le programme

Une fois ces premières issues créées, répartissez-vous les issues et renseignez la personne en charge dans l'interface (voir `assignee`).

Lancez-vous dans les développements.

Au cours de ceux-ci, de nouvelles idées vous surviendront. N'hésitez pas à créer des issues pour cela!
