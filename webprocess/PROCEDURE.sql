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