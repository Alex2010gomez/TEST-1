/*
====================================================
 SISTEMA DE GESTIÓN DE EQUIPOS INFORMÁTICOS
 Backend: Node.js + Express + PostgreSQL
====================================================
*/

require("dotenv").config();
const express = require("express");
const { Pool } = require("pg");
const path = require("path");

const app = express();

app.use(express.json());
app.use(express.static(path.join(__dirname, "public")));

const db = new Pool({
    host: process.env.DB_HOST,
    port: Number(process.env.DB_PORT),
    user: process.env.DB_USER,
    password: process.env.DB_PASSWORD,
    database: process.env.DB_NAME
});

// -------------------------------------------------
// GET - CONSULTAR EQUIPOS
// -------------------------------------------------
app.get("/equipos", async (req, res) => {
    try {
        const datos = await db.query(
            "SELECT * FROM equipos ORDER BY id_equipo ASC"
        );
        res.status(200).json(datos.rows);
    } catch (error) {
        console.error("Error en GET:", error.message);
        res.status(500).json({ error: "No se pudieron consultar equipos" });
    }
});

// -------------------------------------------------
// POST - REGISTRAR EQUIPO
// -------------------------------------------------
app.post("/equipos", async (req, res) => {
    const {
        tipo_equipo,
        nombre_dueno,
        marca_compu,
        procesador,
        generacion,
        ram_cantidada,
        tipo,
        almacenamiento_cantidad,
        almacenamiento_tipo,
        grafica_modelo,
        grafica_tipo,
        tamanio_monitor,
        estado
    } = req.body || {};

    if (!marca_compu || !nombre_dueno || !estado) {
        return res.status(400).json({ error: "Faltan datos obligatorios" });
    }

    try {
        const sql = `
            INSERT INTO equipos (
                tipo_equipo, nombre_dueno, marca_compu, procesador, generacion,
                ram_cantidada, tipo, almacenamiento_cantidad, almacenamiento_tipo,
                grafica_modelo, grafica_tipo, tamanio_monitor, estado
            )
            VALUES ($1, $2, $3, $4, $5, $6, $7, $8, $9, $10, $11, $12, $13)
            RETURNING *
        `;

        const valores = [
            tipo_equipo || "",
            nombre_dueno || "",
            marca_compu || "",
            procesador || "",
            generacion || "",
            Number(ram_cantidada) || 0,
            tipo || "",
            Number(almacenamiento_cantidad) || 0,
            almacenamiento_tipo || "",
            grafica_modelo || "",
            grafica_tipo || "",
            Number(tamanio_monitor) || 0,
            estado || "Operativo"
        ];

        const datos = await db.query(sql, valores);
        res.status(201).json(datos.rows[0]);
    } catch (error) {
        console.error("Error en POST:", error.message);
        res.status(500).json({ error: "No se pudo crear el equipo" });
    }
});

// -------------------------------------------------
// PUT - MODIFICAR EQUIPO
// -------------------------------------------------
app.put("/equipos/:id", async (req, res) => {
    const id = Number(req.params.id);
    const {
        tipo_equipo,
        nombre_dueno,
        marca_compu,
        procesador,
        generacion,
        ram_cantidada,
        tipo,
        almacenamiento_cantidad,
        almacenamiento_tipo,
        grafica_modelo,
        grafica_tipo,
        tamanio_monitor,
        estado
    } = req.body || {};

    if (!Number.isInteger(id) || id <= 0 || !marca_compu) {
        return res.status(400).json({ error: "ID o datos inválidos" });
    }

    try {
        const sql = `
            UPDATE equipos
            SET tipo_equipo = $1,
                nombre_dueno = $2,
                marca_compu = $3,
                procesador = $4,
                generacion = $5,
                ram_cantidada = $6,
                tipo = $7,
                almacenamiento_cantidad = $8,
                almacenamiento_tipo = $9,
                grafica_modelo = $10,
                grafica_tipo = $11,
                tamanio_monitor = $12,
                estado = $13
            WHERE id_equipo = $14
            RETURNING *
        `;

        const valores = [
            tipo_equipo || "",
            nombre_dueno || "",
            marca_compu || "",
            procesador || "",
            generacion || "",
            Number(ram_cantidada) || 0,
            tipo || "",
            Number(almacenamiento_cantidad) || 0,
            almacenamiento_tipo || "",
            grafica_modelo || "",
            grafica_tipo || "",
            Number(tamanio_monitor) || 0,
            estado || "Operativo",
            id
        ];

        const datos = await db.query(sql, valores);

        if (datos.rows.length === 0) {
            return res.status(404).json({ error: "Equipo no encontrado" });
        }

        res.status(200).json(datos.rows[0]);
    } catch (error) {
        console.error("Error en PUT:", error.message);
        res.status(500).json({ error: "No se pudo modificar el equipo" });
    }
});

// -------------------------------------------------
// DELETE - ELIMINAR EQUIPO
// -------------------------------------------------
app.delete("/equipos/:id", async (req, res) => {
    const id = Number(req.params.id);

    if (!Number.isInteger(id) || id <= 0) {
        return res.status(400).json({ error: "ID inválido" });
    }

    try {
        const datos = await db.query(
            "DELETE FROM equipos WHERE id_equipo = $1 RETURNING *",
            [id]
        );

        if (datos.rows.length === 0) {
            return res.status(404).json({ error: "Equipo no encontrado" });
        }

        res.status(200).json({ mensaje: "Equipo eliminado", equipo: datos.rows[0] });
    } catch (error) {
        console.error("Error en DELETE:", error.message);
        res.status(500).json({ error: "No se pudo eliminar el equipo" });
    }
});

const puerto = Number(process.env.PORT) || 3000;
app.listen(puerto, () => {
    console.log(`Servidor iniciado correctamente en http://localhost:${puerto}`);
});