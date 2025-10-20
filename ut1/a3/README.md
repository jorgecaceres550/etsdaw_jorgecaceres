
<center>

# A3 PRACTICANDO GIT


</center>

***Nombre:Jorge Luis Cáceres Gómez***
***Curso:1ºDAW*** 

### ÍNDICE

+ [Introducción](#id1)
+ [Objetivos](#id2)
+ [Material empleado](#id3)
+ [Desarrollo](#id4)
+ [Conclusiones](#id5)


#### ***Introducción***. <a name="id1"></a>

En esta práctica vamos a usar los distintos comandos de git

#### ***Objetivos***. <a name="id2"></a>

El objetivo de esta práctica es practicar los distintos comandos de git para ser más agiles a la hora de hacer un repositorio.

#### ***Material empleado***. <a name="id3"></a>

hardware:
1. Monitor.
2. Teclado
3. Raton.
software:
1. Terminal
2. Cuenta de github para crear el repositorio

#### ***Desarrollo***. <a name="id4"></a>

Commit inicial

Añadir al README.md los comanddos utilizados hasta ahora y hacer un coomit inicial con el mensaje commit inicial.

git add .
git commit -m "commit inicial"
Push inicial

Subir los cambios al repositorio remoto.

git push origin master

    Pregunta: Si has clonado el repositorio es necesario que parte del comando anterior puedo omitir.Justifica tu respuesta en el fichero README.md.
Ignorar archivos
Respuesta: Podríasmos haber saltado la creación del README.md ya que al hacer un repositorio también crea uno

Crear en el repositorio local un fichero llamado privado.txt.

touch privado.txt

Crear en el repositorio local una carpeta llamada privada.

mkdir privada

Realizar los cambios oportunos para que tanto el archivo como la carpeta sean ignorados por git.

echo "privado.txt" >> .gitignore
echo "/privada" >> .gitignore
git add .
git commit -m "añadido fichero .gitignore"

    Preunta: el fichero y el directorio privado debe de subir al repositorio si se encuentra añadido al fichero .gitingnore. [Si/No]. Justifica tu respuesta en el fichero README.md.
Añadir fichero
Respuesta:No, porque al tener el .gitignore no se súbira al repostirio debido a que git los va a ignorar

    Añadir fichero 1.txt al repositorio local.

touch 1.txt
git add .
git commit -m "añadido 1.txt"

    Pregunta: Si ejecutado las acciones add y commit, que realiza cada una sobre el/los ficheros. Justifica tu respuesta en el fichero README.md.
Crear un tag
Respuesta:git add . agrega todos los cambios de los archivos modificados y git commit guarda los cambios de forma permanente, 
    Crear un tag v0.1.

git tag v0.1
Subir el tag

    Subir los cambios al repositorio remoto.

git push --tag origin master

    Preunta: ¿Qué es un tag sobre un repositorio git, en nuestro caso Github?. Justifica tu respuesta en el fichero README.md.
Crear una rama
Respuesta: un tag es una referencia permanente a un punto específico al historial de commits.

    Crear una rama v0.2.

git branch v0.2

    Posiciona tu carpeta de trabajo en esta rama.

git checkout v0.2
Añadir fichero

    Añadir un fichero 2.txt en la rama v0.2.

touch 2.txt
git add .
git commit -m "añadido 2.txt"

    Preunta: Cuando estamos trabajando con ramas, cual es su fin, y sentido en organizaciones pequeñas/medianas/grandes. Justifica tu respuesta en el fichero README.md.
Crear rama remota v0.2
Respuesta:Los tags son marcadores fijos que apuntan a un commit específico e inmutable. se pueden utilizar cuando tienen una versión estable de software.
    Subir los cambios al repositorio remoto.

git push origin v0.2
Merge directo

    Posicionarse en la rama master/main según sea tu rama principal.

git checkout master

    Hacer un merge de la rama v0.2 en la rama main.

git merge v0.2 -m "merge v0.2 sin conflictos"

    Pregunta: Se tendrían que producir conflictos en esta acción. [Si/No] Justifica tu respuesta en el fichero README.md.
Respuesta:Si, porque al modificar el mismo archivo desde dos ramas distintas va haber un conflicto ya que git no sabe como combinarlas.
Merge con conflicto

    En la rama main poner Hola en el fichero 1.txt y hacer commit.

git checkout master
echo "Hola" >> 1.txt
git add .
git commit -m "hola en 1.txt"

    Posicionarse en la rama v0.2 y poner Adios en el fichero 1.txt y hacer commit.

git checkout v0.2
echo "Adios" >> 1.txt
git add .
git commit -m "adios en 1.txt"

    Posicionarse de nuevo en la rama main y hacer un merge con la rama v0.2

git checkout master
git merge v0.2
vim 1.txt
git add .
git commit -m "arreglado merge en 1.txt"
Listado de ramas

    Listar las ramas con merge y las ramas sin merge.

git branch --merged
git branch --no-merged
Arreglar conflicto

    Arreglar el conflicto anterior y hacer un commit.

nano 1.txt
git add .
git commit -m "arreglado merge en 1.txt"
Borrar rama

    Crear un tag v0.2

git tag v0.2

    Borrar la rama v0.2

git branch -d v0.2
Listado de cambios

    Listar los distintos commits con sus ramas y sus tags.

git config --global alias.list 'log --oneline --decorate --graph --all'
git list

*Complicaciones: la primera dificultad que tuve fue al modificar el archivo 1.txt desde distintas ramas, lo que provocó un error, tuve que requeir a internet para resolverlo,pero fue fácil de responder

#### ***Conclusiones***. <a name="id5"></a>

Realizar esta actividad, me resultó un tanto complicada debido a que no tengo muchos conocimientos sobre git.
