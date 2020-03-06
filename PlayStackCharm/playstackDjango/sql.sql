BEGIN;
--
-- Create model Usuario
--
CREATE TABLE "PlayStack_usuario" ("Nombre" varchar(25) NOT NULL PRIMARY KEY, "Contrasenya" varchar(50) NOT NULL, "Correo" varchar(100) NOT NULL, "FotoDePerfil" varchar(100) NOT NULL);
CREATE INDEX "PlayStack_usuario_Nombre_b41ba52d_like" ON "PlayStack_usuario" ("Nombre" varchar_pattern_ops);
COMMIT;
