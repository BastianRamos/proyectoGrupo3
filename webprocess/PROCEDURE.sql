-- Lista de los nombres y apellidos de los empleados
CREATE OR REPLACE PROCEDURE proc_nombre_empleados(nombres OUT SYS_REFCURSOR)
IS
BEGIN
    OPEN nombres FOR
    SELECT id,
        nombre ||' '|| apellido
    FROM core_empleado;
    COMMIT;
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
    INSERT INTO core_tarea(id, nombre, plazo, descripcion, estado, responsable_id)
    VALUES(ISEQ$$_75771.nextval, v_nombre, v_plazo, v_descripcion, v_estado, v_responsable);
    COMMIT;
    v_salida:=1; -- Indica que se ejecuto el Insert

    EXCEPTION

    WHEN OTHERS THEN
        v_salida:=0; -- Indica que no se ejecuto el Insert
    COMMIT;
END;


-- ELIMINAR MODELO USUARIO Y AGREGAR PASSWORD A MODELO EMPLEADO
-- PARA USAR CORREO COMO NOMBRE USUARIO.
SELECT a.nombre,
    b.rol
FROM core_usuario a INNER JOIN core_empleado b
    ON (a.empleado_id = b.id)
WHERE b.rol = 2;


-- Lista de tareas agrupadas por unidad interna
CREATE OR REPLACE PROCEDURE proc_unidad_tarea(tareas_unidades OUT SYS_REFCURSOR)
IS
BEGIN
    OPEN tareas_unidades FOR
    SELECT tarea.nombre AS Tarea,
        unidad.nombre AS Unidad_Interna
    FROM core_empleado empleado
        INNER JOIN core_unidadinterna unidad  ON(empleado.unidadinterna_id = unidad.id)
        INNER JOIN core_tarea tarea ON(empleado.id = tarea.responsable_id)
    ORDER BY empleado.unidadinterna_id;
    COMMIT;
END;


-- Lista de tareas por id de usuario
CREATE OR REPLACE PROCEDURE proc_tareas_usuario(tareas_usuario OUT SYS_REFCURSOR)
IS
BEGIN
    OPEN tareas_usuario FOR
    SELECT nombre,
        plazo,
        descripcion,
        estado
    FROM core_tarea
    WHERE responsable_id = 7
    ORDER BY estado;
    COMMIT;
END;