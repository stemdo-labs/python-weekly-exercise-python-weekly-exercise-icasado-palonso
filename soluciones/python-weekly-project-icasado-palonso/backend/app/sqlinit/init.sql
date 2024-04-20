CREATE TABLE IF NOT EXISTS tasks(
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    description VARCHAR(255),
    created TIMESTAMP DEFAULT NOW(),
    done BOOLEAN DEFAULT FALSE
);

INSERT INTO tasks (title, description) VALUES
    ('Aprender Python', 'Aprender Docker'),
    ('Llamar al cliente', 'Hablar con el cliente para discutir los detalles del proyecto'),
    ('Enviar informe semanal', 'Preparar y enviar el informe semanal a todos los miembros del equipo');