crudo_otros_cursos = 5
crudo_este_curso = 3
promedio_de_duracion_de_otro_curso = 4
promedio_de_duracion_de_este_curso = 1.5


promedio_de_reduccion_de_otros_cursos = 100 - promedio_de_duracion_de_otro_curso * 100 / crudo_otros_cursos
promedio_de_reduccion_de_este_curso = 100 - promedio_de_duracion_de_este_curso * 100 / crudo_este_curso

print('El promedio de reduccion de otros  cursos es de:', promedio_de_reduccion_de_otros_cursos)
print('El promedio de reduccion de este  cursos es de:', promedio_de_reduccion_de_este_curso)