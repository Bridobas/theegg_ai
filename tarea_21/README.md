Tarea 21
La primera tarea de la escuela en la que he tenido que desarrallar y mi primera experiencia con Phyton. 
He utilizado Phyton 3 y programado en Visual Studio Code.

Notación Big-O: O(1)

Entrada: número real entre 0,0001 y 0,9999 (y de no más de 4 cifras decimales)
Salida: fracción irreducible del número de entrada

Pasos realizados:
Al ser la primera vez sin querer he leído un poco el apartado Explicación del enunciado en la web de Nacho Cabanes. 
1.- Lo primero que he hecho es una comprobación de que el dato de entrada tiene el formato correcto (4 decimales máximo y entre o y 1).
2.- Sabiendo que el denominador siempre debe ser mayor que el enumerador para que el resultado sea entre 0 y 1 he iterado una variable desde el valor 1 hasta el 10000. Se acaba en el 10000 ya que el mayor valor posible (0.9999) se obtendría como máximo haciendo 9999/10000.
3.- Desde esta iteración llamo a una función que calcula pasándole el denominador si existe un numerador de menor valor que al dividirlos dé el valor de entrada.
4.- Si desde esta función se devolviera un valor éste sería directamente la fracción irreducible.

Al principio he probado más cosas, pensando, por ejemplo, que los números primos o la función de Python modulus (%) podrían ayudarme a resolver el problema, pero las he descartado finalmente.


Ficheros: tarea_21.py 