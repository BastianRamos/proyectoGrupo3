-- Lista de los nombres y apellidos de los empleados
CREATE OR REPLACE PROCEDURE proc_nombre_empleados(nombres OUT SYS_REFCURSOR)
IS
BEGIN
    OPEN nombres FOR
    SELECT id,
        nombre ||' '|| apellido
    FROM core_empleado;
END;

/*
SELECT a.nombre,
    a.password,
    b.rol
FROM core_usuario a INNER JOIN core_empleado b
    ON a.empleado_id = b.id;*/

-- Agrega una nueva tarea a la tabla con la informacion del formulario web
CREATE OR REPLACE PROCEDURE proc_agregar_tarea(
    v_nombre VARCHAR2,
    v_plazo DATE,
    v_descripcion VARCHAR2,
    v_estado NUMBER,
    v_responsable NUMBER,
    v_salida OUT NUMBER -- Usamos el valor de salida para determinar si se ejecuto o no
)
IS
BEGIN
    INSERT INTO core_tarea(nombre, plazo, descripcion, estado, responsable_id)
    VALUES(v_nombre, v_plazo, v_descripcion, v_estado, v_responsable);
    COMMIT;
    v_salida:=1;

    EXCEPTION

    WHEN OTHERS THEN
        v_salida:=0;
END;
