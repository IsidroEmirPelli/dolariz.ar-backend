# Si por ejemplo, el método GET de X View, requiere procesar algún HTML para
# scrapearlo, mas bien SOLO se encargará de realizar las tareas que hereda (las tareas
# dispuestas por su padre, sease APIView, ModelViewSet, o etc.), de adaptar los
# parámetros de entrada como por ejemplo extraer una query:
# mi_query = (request.query.get('X_Query') or request.query.get('XQuery'))
# , Y, instanciar al N servicio para que realice entonces el procesamiento del HTML,
# pasándole el parámetro que contenga exe HTML. De esta forma 