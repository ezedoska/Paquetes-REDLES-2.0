from sqlalchemy import types

paquetesOUT = {
    "F1252": {
        "titulo": "PAQUETE F.1252",
        "form": "F.1252",
        "exec": "proc_p0",
        "direccion": "P:\\SINTyS\\Paquete_00\\Lote_",
        "lotenombre": "P0-2019",
        "files": {
            "Paquete 0": {
                "tabla": "dbo.DTS_SalidaPaquete00_2019",
                "whereorder": "",
                "cabecera": "01307070463991252002000",
                "archivo": "F01252.cuit.30707046399.fecha.AAAAMMDD.nro.001de001.txt",
                "replace": "AAAAMMDD",
                "header": True,
                "sep": "|",
                "encoding": "ansi",
                "line_terminator": "",
                "escapechar": '"',
                "mode": "w",
            },
            "Informe Errores": {
                "tabla": "DTS_ErroresPaquete00_2019",
                "whereorder": "",
                "archivo": "No-enviados-paquete-0-NLOTE.txt",
                "replace": "NLOTE",
                "header": False,
                "sep": "|",
                "encoding": "ansi",
                "line_terminator": "",
                "escapechar": '"',
                "mode": "w",
            },
        },
    },
    "FSINTYS": {
        "titulo": "PAQUETE F.SINTyS",
        "form": "F.SINTyS",
        "exec": "proc_p2",
        "direccion": "P:\\SINTyS\\Paquete_02\\Lote_",
        "lotenombre": "P0-2019",
        "files": {
            "Paquete 2 Postulantes": {
                "tabla": "dbo.DTS_SalidaPaquete02_Titulares_2019",
                "whereorder": "",
                "archivo": "Paquete2LoteNLOTE.txt",
                "replace": "NLOTE",
                "header": False,
                "sep": "|",
                "encoding": "ansi",
                "line_terminator": "",
                "escapechar": '"',
                "mode": "w",
            },
            "Paquete 2 Familiares": {
                "tabla": "dbo.DTS_SalidaPaquete02_Familiares_2019",
                "whereorder": "",
                "archivo": "Paquete2AnexoLoteNLOTE.txt",
                "replace": "NLOTE",
                "header": False,
                "sep": "|",
                "encoding": "ansi",
                "line_terminator": "",
                "escapechar": '"',
                "mode": "w",
            },
        },
    },
    "F1253": {
        "titulo": "PAQUETE F.1253",
        "form": "F.1253",
        "exec": "proc_P4_01_2019",
        "direccion": "P:\\AFIP\\Paquete_04_2038\\Lote_",
        "lotenombre": "P4-2038",
        "files": {
            "Paquete 4": {
                "tabla": "dbo.DTS_SalidaPaquete04_2020",
                "whereorder": "order by text",
                "cabecera": "01307070463991253002005",
                "archivo": "F1253.cuit.30707046399.fecha.AAAAMMDD.txt",
                "replace": "AAAAMMDD",
                "header": True,
                "sep": "|",
                "encoding": "ansi",
                "line_terminator": "",
                "escapechar": '"',
                "mode": "w",
            },
        },
    },
    "F1257": {
        "titulo": "PAQUETE F.1257",
        "form": "F.1257",
        "exec": "proc_P7_01_2021",
        "direccion": "P:\\AFIP\\Paquete_07\\Lote_000",
        "lotenombre": "P7-2021",
        "files": {
            "Paquete 7": {
                "tabla": "dbo.DTS_SalidaPaquete07_2020",
                "whereorder": "order by text",
                "cabecera": "",
                "archivo": "F01257.cuit.30707046399.fecha.AAAAMMDD.txt",
                "replace": "AAAAMMDD",
                "header": False,
                "sep": "|",
                "encoding": "ansi",
                "line_terminator": "",
                "escapechar": '"',
                "mode": "w",
            },
        },
    },
    "F1258": {
        "titulo": "PAQUETE F.1258",
        "form": "F.1258",
        "exec": "proc_p8",
        "direccion": "P:\\AFIP\\Paquete_08\\Lote_",
        "lotenombre": "p8",
        "files": {
            "Paquete 8": {
                "tabla": "dbo.DTS_SalidaPaquete08_2019",
                "whereorder": "order by text",
                "cabcecera": "",
                "archivo": "F01258.cuit.30707046399.fecha.AAAAMMDD.txt",
                "replace": "AAAAMMDD",
                "header": False,
                "sep": "|",
                "encoding": "ansi",
                "line_terminator": "",
                "escapechar": '"',
                "mode": "w",
            },
        },
    },
    "F1253ADH": {
        "titulo": "PAQUETE F.1253ADH",
        "form": "F.1253ADH",
        "exec": "proc_p8",
        "direccion": "P:\\AFIP\\Paquete_14_Abm_(adh)\\Lote_",
        "lotenombre": "p14",
        "files": {
            "Paquete 14": {
                "tabla": "dbo.DTS_SalidaPaquete14_2019",
                "whereorder": "order by text",
                "cabcecera": "",
                "archivo": "F01253.cuit.30707046399.fecha.AAAAMMDD.txt",
                "replace": "AAAAMMDD",
                "header": False,
                "sep": "|",
                "encoding": "ansi",
                "line_terminator": "",
                "escapechar": '"',
                "mode": "w",
            },
        },
    },
}

paquetesIN = {
    "F1252v": {
        "titulo": "VUELTA PAQUETE F.1252",
        "form": "F.1252v",
        "exec": [
            "proc_p1",
        ],
        "direccion": "P:\\AFIP\\Paquete_01\\Lote_5",
        "lotenombre": "P1-2019",
        "pqt": "AFIP_MDS_F01252.cuit.30707046399",
        "read_csv": {
            "compression": None,
            "sep": ";",
            "names": [
                "Lote",
                "clave",
                "CUIT",
                "cumple",
                "Empleador",
                "Empleador_periodo",
                "Dependiente",
                "Soc_CUIT",
                "Soc_Relacion",
                "Soc_Cargo",
                "Soc_Desde",
                "Soc_Estado",
                "Soc_cuitasoc",
                "Soc_cuitasoc_desde",
                "Error",
            ],
            "encoding": "ansi",
            "delimiter": None,
            "engine": "python",
            "dtype": None,
            # "dtype": {"text": types.VARCHAR(length=252)},
        },
        "SCP": {
            "tabla": "DTS_EntradaPaquete01_2020TEST",
            "repl": False,
            "dtype": None,
        },
    },
    "F1253v": {
        "titulo": "VUELTA PAQUETE F.1253",
        "form": "F.1253v",
        "exec": [
            "proc_p5",
        ],
        "direccion": "P:\\AFIP\\Paquete_05\\Lote_",
        "lotenombre": "P5-2038",
        "pqt": "Cuitificacion",
        "read_csv": {
            "compression": None,
            "sep": None,
            "names": ["text"],
            "delimiter": None,
            "engine": "python",
            "dtype": None,
        },
        "SCP": {
            "tabla": "DTS_EntradaPaquete05_2019",
            "repl": True,
            "dtype": {"text": types.VARCHAR(length=252)},
        },
    },
    "F1253ADHv": {
        "titulo": "VUELTA PAQUETE F.1253ADH",
        "form": "F.1253ADHv",
        "exec": [
            "proc_p15",
        ],
        "direccion": "P:\\AFIP\\Paquete_15\\Lote_",
        "lotenombre": "P15",
        "pqt": "ADH",
        "read_csv": {
            "compression": "zip",
            "sep": ",",
            "names": ["text"],
            "delimiter": None,
            "encoding": "ansi",
            "engine": "python",
            "dtype": None,
        },
        "SCP": {
            "tabla": "DTS_EntradaPaquete15_2019",
            "repl": False,
            "dtype": {"text": types.VARCHAR(length=252)},
        },
    },
    "F1257v": {
        "titulo": "VUELTA PAQUETE F.1257v",
        "form": "F.1257v",
        "exec": [
            "proc_p17v",
        ],
        "direccion": "P:\\AFIP\\Paquete_07\\Lote_",
        "lotenombre": "proc_P7_02_2021",
        "pqt": "1257",
        "read_csv": {
            "compression": None,
            "sep": ",",
            "names": ["text"],
            "delimiter": None,
            "encoding": "ansi",
            "engine": "python",
            "dtype": None,
        },
        "SCP": {
            "tabla": "dts_entradapaquete07_2021",
            "repl": False,
            "dtype": {"text": types.VARCHAR(length=252)},
        },
    },
    "F1258v": {
        "titulo": "VUELTA PAQUETE F.1258",
        "form": "F.1258v",
        "exec": [
            "proc_p8v",
        ],
        "direccion": "P:\\AFIP\\Paquete_08\\Lote_",
        "lotenombre": "P8v",
        "pqt": "ADH",
        "read_csv": {
            "compression": None,
            "sep": ",",
            "names": ["text"],
            "delimiter": None,
            "encoding": "ansi",
            "engine": "python",
            "dtype": None,
        },
        "SCP": {
            "tabla": "DTS_EntradaPaquete15_2019",
            "repl": False,
            "dtype": {"text": types.VARCHAR(length=252)},
        },
    },
}
