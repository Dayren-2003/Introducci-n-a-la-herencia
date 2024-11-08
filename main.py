# main.py
from estudiantes import Estudiantes
from profesores import Profesores
from administrativos import Administrativos
from empleado_limpieza import EmpleadoLimpieza

def main():
    # Crear objetos
    estudiante = Estudiantes()
    estudiante.set_nombre("Alejandro")
    estudiante.set_apellido("Gonzalez")
    estudiante.set_edad(20)
    estudiante.set_matricula("123456")
    estudiante.set_carrera("Ing. Civil")
    estudiante.set_semestre("5°")

    profesor = Profesores()
    profesor.set_nombre("María")
    profesor.set_apellido("López")
    profesor.set_edad(52)
    profesor.set_departamento("Sistemas")
    profesor.set_categoria("Universidad")
    profesor.set_maxgrad0("Licenciatura")

    administrativo = Administrativos()
    administrativo.set_nombre("Mariana")
    administrativo.set_apellido("Morales")
    administrativo.set_edad(30)
    administrativo.set_cargo("Secretaria")
    administrativo.set_area("Contabilidad")

    empresa = EmpleadoLimpieza()
    empresa.set_nombre("Erick")
    empresa.set_apellido("Elizalde")
    empresa.set_edad(40)
    empresa.set_nombre_empresa("Limpieza S.A.")
    empresa.set_direccion("Calle Ficticia 123")
    empresa.set_numero_empleado("E6789")
    empresa.set_turno("Vespertino")

    # Mostrar información
    print("Estudiante:")
    print(estudiante.mostrar_informacion())

    print("\nProfesor:")
    print(profesor.mostrar_informacion())

    print("\nAdministrativo:")
    print(administrativo.mostrar_informacion())

    print("\nEmpleado de Limpieza:")
    print(empresa.mostrar_informacion())

if __name__ == "__main__":
    main()
