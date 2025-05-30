BOOKS = {
    "libro_iva_digital_ventas_cbte": {
        1: {
            "Campo": "Fecha de comprobante",
            "Posiciones": (0, 7),
            "Tipo de Dato": "Numérico",
            "Longitud": 8,
            "Observaciones": "AAAAMMDD",
        },
        2: {
            "Campo": "Tipo de comprobante",
            "Posiciones": (8, 10),
            "Tipo de Dato": "Numérico",
            "Longitud": 3,
            "Observaciones": "Según tabla Comprobantes Ventas",
        },
        3: {
            "Campo": "Punto de venta",
            "Posiciones": (11, 15),
            "Tipo de Dato": "Numérico",
            "Longitud": 5,
            "Observaciones": None,
        },
        4: {
            "Campo": "Número de comprobante",
            "Posiciones": (16, 35),
            "Tipo de Dato": "Numérico",
            "Longitud": 20,
            "Observaciones": None,
        },
        5: {
            "Campo": "Número de comprobante hasta",
            "Posiciones": (36, 55),
            "Tipo de Dato": "Numérico",
            "Longitud": 20,
            "Observaciones": None,
        },
        6: {
            "Campo": "Código de documento del comprador",
            "Posiciones": (56, 57),
            "Tipo de Dato": "Numérico",
            "Longitud": 2,
            "Observaciones": "Según tabla Documentos",
        },
        7: {
            "Campo": "Número de identificación del comprador",
            "Posiciones": (58, 77),
            "Tipo de Dato": "Alfaumérico",
            "Longitud": 20,
            "Observaciones": "Completar con ceros a la izquierda",
        },
        8: {
            "Campo": "Apellido y nombre o denominación del comprador",
            "Posiciones": (78, 107),
            "Tipo de Dato": "Alfanumérico",
            "Longitud": 30,
            "Observaciones": None,
        },
        9: {
            "Campo": "Importe total de la operación",
            "Posiciones": (108, 122),
            "Tipo de Dato": "Numérico",
            "Longitud": 15,
            "Observaciones": "13 enteros 2 decimales sin punto decimal",
        },
        10: {
            "Campo": "Importe total de conceptos que no integran el precio neto gravado",
            "Posiciones": (123, 137),
            "Tipo de Dato": "Numérico",
            "Longitud": 15,
            "Observaciones": "13 enteros 2 decimales sin punto decimal",
        },
        11: {
            "Campo": "Percepción a no categorizados",
            "Posiciones": (138, 152),
            "Tipo de Dato": "Numérico",
            "Longitud": 15,
            "Observaciones": "13 enteros 2 decimales sin punto decimal",
        },
        12: {
            "Campo": "Importe de operaciones exentas",
            "Posiciones": (153, 167),
            "Tipo de Dato": "Numérico",
            "Longitud": 15,
            "Observaciones": "13 enteros 2 decimales sin punto decimal",
        },
        13: {
            "Campo": "Importe de percepciones o pagos a cuenta de impuestos nacionales",
            "Posiciones": (168, 182),
            "Tipo de Dato": "Numérico",
            "Longitud": 15,
            "Observaciones": "13 enteros 2 decimales sin punto decimal",
        },
        14: {
            "Campo": "Importe de percepciones de ingresos brutos",
            "Posiciones": (183, 197),
            "Tipo de Dato": "Numérico",
            "Longitud": 15,
            "Observaciones": "13 enteros 2 decimales sin punto decimal",
        },
        15: {
            "Campo": "Importe de percepciones de impuestos municipales",
            "Posiciones": (198, 212),
            "Tipo de Dato": "Numérico",
            "Longitud": 15,
            "Observaciones": "13 enteros 2 decimales sin punto decimal",
        },
        16: {
            "Campo": "Importe de impuestos internos",
            "Posiciones": (213, 227),
            "Tipo de Dato": "Numérico",
            "Longitud": 15,
            "Observaciones": "13 enteros 2 decimales sin punto decimal",
        },
        17: {
            "Campo": "Código de moneda",
            "Posiciones": (228, 230),
            "Tipo de Dato": "Alfaumérico",
            "Longitud": 3,
            "Observaciones": "Según tabla Tipo de Monedas",
        },
        18: {
            "Campo": "Tipo de cambio",
            "Posiciones": (231, 240),
            "Tipo de Dato": "Numérico",
            "Longitud": 10,
            "Observaciones": "4 enteros 6 decimales sin punto decimal",
        },
        19: {
            "Campo": "Cantidad de alícuotas de IVA",
            "Posiciones": (241,),
            "Tipo de Dato": "Numérico",
            "Longitud": 1,
            "Observaciones": None,
        },
        20: {
            "Campo": "Código de operación",
            "Posiciones": (242,),
            "Tipo de Dato": "Alfabético",
            "Longitud": 1,
            "Observaciones": "Según tabla Código de Operación",
        },
        21: {
            "Campo": "Otros tributos",
            "Posiciones": (243, 257),
            "Tipo de Dato": "Numérico",
            "Longitud": 15,
            "Observaciones": "13 enteros 2 decimales sin punto decimal",
        },
        22: {
            "Campo": "Fecha de Vencimiento o Pago",
            "Posiciones": (258, 265),
            "Tipo de Dato": "Numérico",
            "Longitud": 8,
            "Observaciones": "AAAAMMDD",
        },
    },
    "libro_iva_digital_ventas_alicuota": {
        1: {
            "Campo": "Tipo de comprobante",
            "Posiciones": (0, 2),
            "Tipo de Dato": "Numérico",
            "Longitud": 3,
            "Observaciones": "Según tabla de Comprobantes",
        },
        2: {
            "Campo": "Punto de venta",
            "Posiciones": (3, 7),
            "Tipo de Dato": "Numérico",
            "Longitud": 5,
            "Observaciones": None,
        },
        3: {
            "Campo": "Número de comprobante",
            "Posiciones": (8, 27),
            "Tipo de Dato": "Numérico",
            "Longitud": 20,
            "Observaciones": None,
        },
        4: {
            "Campo": "Importe neto gravado",
            "Posiciones": (28, 42),
            "Tipo de Dato": "Numérico",
            "Longitud": 15,
            "Observaciones": "13 enteros 2 decimales sin punto decimal",
        },
        5: {
            "Campo": "Alícuota de IVA",
            "Posiciones": (43, 46),
            "Tipo de Dato": "Numérico",
            "Longitud": 4,
            "Observaciones": "Según tabla Alícuotas",
        },
        6: {
            "Campo": "Impuesto Liquidado",
            "Posiciones": (47, 61),
            "Tipo de Dato": "Numérico",
            "Longitud": 15,
            "Observaciones": "13 enteros 2 decimales sin punto decimal",
        },
    },
    "libro_iva_digital_compras_cbte": {
        1: {
            "Campo": "Fecha de comprobante",
            "Posiciones": (0, 7),
            "Tipo de Dato": "Numérico",
            "Longitud": 8,
            "Observaciones": "AAAAMMDD",
        },
        2: {
            "Campo": "Tipo de comprobante",
            "Posiciones": (8, 10),
            "Tipo de Dato": "Numérico",
            "Longitud": 3,
            "Observaciones": "Según tabla Comprobantes Compra",
        },
        3: {
            "Campo": "Punto de venta",
            "Posiciones": (11, 15),
            "Tipo de Dato": "Numérico",
            "Longitud": 5,
            "Observaciones": None,
        },
        4: {
            "Campo": "Número de comprobante",
            "Posiciones": (16, 35),
            "Tipo de Dato": "Numérico",
            "Longitud": 20,
            "Observaciones": None,
        },
        5: {
            "Campo": "Despacho de importación",
            "Posiciones": (36, 51),
            "Tipo de Dato": "Alfaumérico",
            "Longitud": 16,
            "Observaciones": None,
        },
        6: {
            "Campo": "Código de documento del vendedor",
            "Posiciones": (52, 53),
            "Tipo de Dato": "Numérico",
            "Longitud": 2,
            "Observaciones": "Según tabla Documentos",
        },
        7: {
            "Campo": "Número de identificación del vendedor",
            "Posiciones": (54, 73),
            "Tipo de Dato": "Alfaumérico",
            "Longitud": 20,
            "Observaciones": "Completar con ceros a la izquierda",
        },
        8: {
            "Campo": "Apellido y nombre o denominación del vendedor",
            "Posiciones": (74, 103),
            "Tipo de Dato": "Alfanumérico",
            "Longitud": 30,
            "Observaciones": None,
        },
        9: {
            "Campo": "Importe total de la operación",
            "Posiciones": (104, 118),
            "Tipo de Dato": "Numérico",
            "Longitud": 15,
            "Observaciones": "13 enteros 2 decimales sin punto decimal",
        },
        10: {
            "Campo": "Importe total de conceptos que no integran el precio neto gravado",
            "Posiciones": (119, 133),
            "Tipo de Dato": "Numérico",
            "Longitud": 15,
            "Observaciones": "13 enteros 2 decimales sin punto decimal",
        },
        11: {
            "Campo": "Importe de operaciones exentas",
            "Posiciones": (134, 148),
            "Tipo de Dato": "Numérico",
            "Longitud": 15,
            "Observaciones": "13 enteros 2 decimales sin punto decimal",
        },
        12: {
            "Campo": "Importe de percepciones o pagos a cuenta del Impuesto al Valor Agregado",
            "Posiciones": (149, 163),
            "Tipo de Dato": "Numérico",
            "Longitud": 15,
            "Observaciones": "13 enteros 2 decimales sin punto decimal",
        },
        13: {
            "Campo": "Importe de percepciones o pagos a cuenta de impuestos nacionales",
            "Posiciones": (164, 178),
            "Tipo de Dato": "Numérico",
            "Longitud": 15,
            "Observaciones": "13 enteros 2 decimales sin punto decimal",
        },
        14: {
            "Campo": "Importe de percepciones de ingresos brutos",
            "Posiciones": (179, 193),
            "Tipo de Dato": "Numérico",
            "Longitud": 15,
            "Observaciones": "13 enteros 2 decimales sin punto decimal",
        },
        15: {
            "Campo": "Importe de percepciones de impuestos municipales",
            "Posiciones": (194, 208),
            "Tipo de Dato": "Numérico",
            "Longitud": 15,
            "Observaciones": "13 enteros 2 decimales sin punto decimal",
        },
        16: {
            "Campo": "Importe de impuestos internos",
            "Posiciones": (209, 223),
            "Tipo de Dato": "Numérico",
            "Longitud": 15,
            "Observaciones": "13 enteros 2 decimales sin punto decimal",
        },
        17: {
            "Campo": "Código de moneda",
            "Posiciones": (224, 226),
            "Tipo de Dato": "Alfaumérico",
            "Longitud": 3,
            "Observaciones": "Según tabla Tipo de Monedas",
        },
        18: {
            "Campo": "Tipo de cambio",
            "Posiciones": (227, 236),
            "Tipo de Dato": "Numérico",
            "Longitud": 10,
            "Observaciones": "4 enteros 6 decimales sin punto decimal",
        },
        19: {
            "Campo": "Cantidad de alícuotas de IVA",
            "Posiciones": (237,),
            "Tipo de Dato": "Numérico",
            "Longitud": 1,
            "Observaciones": None,
        },
        20: {
            "Campo": "Código de operación",
            "Posiciones": (238,),
            "Tipo de Dato": "Alfabético",
            "Longitud": 1,
            "Observaciones": "Según tabla Código de Operación",
        },
        21: {
            "Campo": "Crédito Fiscal Computable",
            "Posiciones": (239, 253),
            "Tipo de Dato": "Numérico",
            "Longitud": 15,
            "Observaciones": "13 enteros 2 decimales sin punto decimal",
        },
        22: {
            "Campo": "Otros Tributos",
            "Posiciones": (254, 268),
            "Tipo de Dato": "Numérico",
            "Longitud": 15,
            "Observaciones": "13 enteros 2 decimales sin punto decimal",
        },
        23: {
            "Campo": "CUIT emisor/corredor",
            "Posiciones": (269, 279),
            "Tipo de Dato": "Numérico",
            "Longitud": 11,
            "Observaciones": None,
        },
        24: {
            "Campo": "Denominación del emisor/corredor",
            "Posiciones": (280, 309),
            "Tipo de Dato": "Alfanumérico",
            "Longitud": 30,
            "Observaciones": None,
        },
        25: {
            "Campo": "IVA comisión",
            "Posiciones": (310, 324),
            "Tipo de Dato": "Numérico",
            "Longitud": 15,
            "Observaciones": "13 enteros 2 decimales sin punto decimal",
        },
    },
    "libro_iva_digital_compras_alicuota": {
        1: {
            "Campo": "Tipo de comprobante",
            "Posiciones": (0, 2),
            "Tipo de Dato": "Numérico",
            "Longitud": 3,
            "Observaciones": "Según tabla de Comprobantes",
        },
        2: {
            "Campo": "Punto de venta",
            "Posiciones": (3, 7),
            "Tipo de Dato": "Numérico",
            "Longitud": 5,
            "Observaciones": None,
        },
        3: {
            "Campo": "Número de comprobante",
            "Posiciones": (8, 27),
            "Tipo de Dato": "Numérico",
            "Longitud": 20,
            "Observaciones": None,
        },
        4: {
            "Campo": "Código de documento del vendedor",
            "Posiciones": (28, 29),
            "Tipo de Dato": "Numérico",
            "Longitud": 2,
            "Observaciones": "Según tabla Documentos",
        },
        5: {
            "Campo": "Número de identificación del Vendedor",
            "Posiciones": (30, 49),
            "Tipo de Dato": "Alfanumérico",
            "Longitud": 20,
            "Observaciones": "Completar con ceros a izquierda",
        },
        6: {
            "Campo": "Importe neto gravado",
            "Posiciones": (50, 64),
            "Tipo de Dato": "Numérico",
            "Longitud": 15,
            "Observaciones": "13 enteros 2 decimales sin punto decimal",
        },
        7: {
            "Campo": "Alícuota de IVA",
            "Posiciones": (65, 68),
            "Tipo de Dato": "Numérico",
            "Longitud": 4,
            "Observaciones": "Según tabla de Alícuotas",
        },
        8: {
            "Campo": "Impuesto liquidado",
            "Posiciones": (69, 83),
            "Tipo de Dato": "Numérico",
            "Longitud": 15,
            "Observaciones": "13 enteros 2 decimales sin punto decimal",
        },
    },
}
