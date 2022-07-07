CREATE TABLE Usuarios ( 
		id_usu INTEGER,
		name TEXT,
		PRIMARY KEY(id_usu)
		);

CREATE TABLE Perfiles ( 
		id_profile INTEGER,
		id_usu INTEGER,
		name TEXT,
		PRIMARY KEY(id_profile),
		FOREIGN KEY (id_usu) REFERENCES Usuarios(id_usu)
		);

CREATE TABLE Botones ( 
		id_btn INTEGER,
		id_profile INTEGER,
		name TEXT,
		shortcut TEXT,
		postion INT,
		mantener INT,
		PRIMARY KEY(id_profile),
		FOREIGN KEY (id_profile) REFERENCES Perfiles(id_profile)
		);