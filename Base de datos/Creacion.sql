CREATE TABLE Ususario
(
   Nombre         CHAR(-1) PRIMARY KEY,
   Contrasenya    CHAR(-1)        NOT NULL,
   Correo         CHAR(-1)        NOT NULL,
   FotoDePerfil   BOOLEAN
);

CREATE TABLE Premium
(
   Nombre   CHAR(-1) PRIMARY KEY,
   FOREIGN KEY (Nombre) REFERENCES Ususario(Nombre)
);

CREATE TABLE NoPremium
(
   Nombre    CHAR(-1) PRIMARY KEY,
   NumSalt   NUMBER        NOT NULL,
   FOREIGN KEY (Nombre) REFERENCES Ususario(Nombre)
);

CREATE TABLE CreadorContenido
(
   Nombre   CHAR(-1) PRIMARY KEY,
   FOREIGN KEY (Nombre) REFERENCES Ususario(Nombre)
);

CREATE TABLE Genero
(
   ID       NUMBER PRIMARY KEY,
   Nombre   CHAR(-1)        NOT NULL
);

CREATE TABLE Audio
(
   FicheroAudio              CHAR(-1)        NOT NULL,
   Titulo                    CHAR(-1)        NOT NULL,
   Idioma                    CHAR(-1)        NOT NULL,
   ID                        NUMBER,
   Duracion                  FLOAT        NOT NULL,
   CreadorContenido_Nombre   CHAR(-1),
   PRIMARY KEY (ID,CreadorContenido_Nombre),
   FOREIGN KEY (CreadorContenido_Nombre) REFERENCES CreadorContenido(Nombre)
);

CREATE TABLE Podcast
(
   ID        NUMBER PRIMARY KEY,
   Resumen   CHAR(-1)        NOT NULL,
   FOREIGN KEY (ID) REFERENCES Audio(ID)
);

CREATE TABLE Cancion
(
   ID   NUMBER PRIMARY KEY,
   FOREIGN KEY (ID) REFERENCES Audio(ID)
);

CREATE TABLE PlayList
(
   ID                NUMBER,
   Nombre            CHAR(-1)        NOT NULL,
   Ususario_Nombre   CHAR(-1),
   PRIMARY KEY (ID,Ususario_Nombre),
   FOREIGN KEY (Ususario_Nombre) REFERENCES Ususario(Nombre)
);

CREATE TABLE Carpeta
(
   ID       NUMBER PRIMARY KEY,
   Nombre   CHAR(-1)        NOT NULL
);

CREATE TABLE Artista
(
   Nombre             CHAR(-1) PRIMARY KEY,
   PaisDeNacimiento   CHAR(-1)        NOT NULL
);

CREATE TABLE Amacenar
(
   Carpeta_ID                 NUMBER,
   PlayList_ID                NUMBER,
   PlayList_Ususario_Nombre   CHAR(-1),
   PRIMARY KEY (Carpeta_ID,PlayList_ID,PlayList_Ususario_Nombre),
   FOREIGN KEY (Carpeta_ID) REFERENCES Carpeta(ID),
   FOREIGN KEY (PlayList_ID,PlayList_Ususario_Nombre) REFERENCES PlayList(ID,Ususario_Nombre)
);

CREATE TABLE Contiene
(
   Audio_ID                        NUMBER,
   Audio_CreadorContenido_Nombre   CHAR(-1),
   PlayList_ID                     NUMBER,
   PlayList_Ususario_Nombre        CHAR(-1),
   PRIMARY KEY (Audio_ID,Audio_CreadorContenido_Nombre,PlayList_ID,PlayList_Ususario_Nombre),
   FOREIGN KEY (Audio_ID,Audio_CreadorContenido_Nombre) REFERENCES Audio(ID,CreadorContenido_Nombre),
   FOREIGN KEY (PlayList_ID,PlayList_Ususario_Nombre) REFERENCES PlayList(ID,Ususario_Nombre)
);

CREATE TABLE Pertenecer
(
   Audio_ID                        NUMBER,
   Audio_CreadorContenido_Nombre   CHAR(-1),
   Genero_ID                       NUMBER,
   PRIMARY KEY (Audio_ID,Audio_CreadorContenido_Nombre,Genero_ID),
   FOREIGN KEY (Audio_ID,Audio_CreadorContenido_Nombre) REFERENCES Audio(ID,CreadorContenido_Nombre),
   FOREIGN KEY (Genero_ID) REFERENCES Genero(ID)
);

CREATE TABLE Seguir
(
   Ususario_Nombre   CHAR(-1),
   Ususario_Nombre   CHAR(-1),
   PRIMARY KEY (Ususario_Nombre,Ususario_Nombre),
   FOREIGN KEY (Ususario_Nombre) REFERENCES Ususario(Nombre),
   FOREIGN KEY (Ususario_Nombre) REFERENCES Ususario(Nombre)
);

CREATE TABLE SerFavorita
(
   Audio_ID                        NUMBER,
   Audio_CreadorContenido_Nombre   CHAR(-1),
   Ususario_Nombre                 CHAR(-1),
   PRIMARY KEY (Audio_ID,Audio_CreadorContenido_Nombre,Ususario_Nombre),
   FOREIGN KEY (Audio_ID,Audio_CreadorContenido_Nombre) REFERENCES Audio(ID,CreadorContenido_Nombre),
   FOREIGN KEY (Ususario_Nombre) REFERENCES Ususario(Nombre)
);

CREATE TABLE Componer
(
   Artista_Nombre                  CHAR(-1),
   Audio_ID                        NUMBER,
   Audio_CreadorContenido_Nombre   CHAR(-1),
   PRIMARY KEY (Artista_Nombre,Audio_ID,Audio_CreadorContenido_Nombre),
   FOREIGN KEY (Artista_Nombre) REFERENCES Artista(Nombre),
   FOREIGN KEY (Audio_ID,Audio_CreadorContenido_Nombre) REFERENCES Audio(ID,CreadorContenido_Nombre)
);

