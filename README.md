# Commencez par installer Django en utilisant pip, le gestionnaire de paquets Python.
# pip install django 
# Création d'un nouveau projet Django 
# django-admin startproject nom_du_projet
# Création d'une application Django 
# cd nom_du_projet
# python manage.py startapp nom_de_l_application
# Exécutez les migrations non appliquées en exécutant la commande migrate
# python manage.py migrate 
# Création d'un superutilisateur pour la partie admin
# python manage.py createsuperuser
# python manage.py runserver


# manage.py

` un script en ligne de commande qui vous permet d'interagir avec votre projet Django. Vous l'utiliserez pour effectuer diverses tâches telles que la gestion des migrations, le démarrage du serveur de développement, la création de superutilisateurs`

# Nom du projet 1


# __init__.py
`un fichier vide qui indique à Python que ce répertoire doit être traité comme un package Python.`

# settings.py
` le fichier de configuration principal de votre projet Django. Vous y définissez les paramètres de configuration pour votre application, tels que les bases de données, les clés secrètes, les applications installées`

# urls.py 
`le fichier de configuration des URL de votre projet. Vous définissez les correspondances URL vers les vues de votre application dans ce fichier`

# wsgi.py 
`un point d'entrée pour votre application WSGI (Web Server Gateway Interface). Il est utilisé pour servir votre application via des serveurs web compatibles WSGI`

# asgi.py 
`un point d'entrée pour votre application ASGI (Asynchronous Server Gateway Interface). Il est utilisé pour servir votre application via des serveurs web compatibles ASGI, qui prennent en charge les fonctionnalités asynchrones.`

# Nom de l'application 2

# __init__.py
`un fichier vide qui indique à Python que ce répertoire doit être traité comme un package Python.`

# admin.py
`un fichier dans lequel vous pouvez enregistrer vos modèles pour les rendre accessibles dans l'interface d'administration Django.`

# apps.py 
`un fichier qui définit la configuration de votre application Django.`

# models.py  
`un fichier dans lequel vous définissez vos modèles de données en utilisant des classes Python. Chaque modèle représente une table dans votre base de données.`

# tests.py 
` un fichier dans lequel vous pouvez écrire des tests pour votre application.`

# views.py
`un fichier dans lequel vous définissez les vues de votre application. Les vues sont des fonctions ou des classes Python qui traitent les requêtes HTTP et renvoient les réponses.`
