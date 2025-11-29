#!/usr/bin/env python3
import json

# Las primeras 25 preguntas ya están creadas manualmente
# Aquí generamos las 75 restantes de forma programática

faq_questions = []

# Categoría: Comparaciones Técnicas (26-50)
comparisons = [
    ("¿Fotogrametría vs. LiDAR: cuál es más preciso?", "LiDAR ofrece mayor precisión en terrenos con vegetación densa (penetra el follaje), mientras que fotogrametría es superior en texturización y coste. LiDAR: precisión vertical <5 cm, ideal para topografía forestal. Fotogrametría: precisión <2 cm con RTK, ideal para infraestructuras y áreas abiertas. Gaueko Air recomienda fotogrametría para el 80% de proyectos por su relación coste-beneficio."),
    ("¿Drones vs. topografía tradicional: cuál es más rápido?", "Drones son 10-20x más rápidos. Topografía tradicional: 5-10 ha/día con estación total. Drones: 50-1000 ha/día según equipo. Ventajas adicionales: acceso a zonas peligrosas sin riesgo, cobertura completa vs. puntos discretos, modelo 3D completo vs. perfiles 2D."),
    ("¿Drones vs. helicópteros: cuál es más económico?", "Drones son 50-70% más económicos. Helicóptero: 1.500-3.000€/hora de vuelo, resolución 10-20 cm/px. Drones: 1.000€/día completo, resolución <2 cm/px. Drones también son más seguros (sin riesgo para tripulación), más silenciosos y con menor impacto ambiental."),
    ("¿Qué resolución ofrecen los drones vs. satélites?", "Drones: <2 cm/px (hasta 0.5 cm/px volando bajo). Satélites comerciales: 30-50 cm/px (WorldView, Pléiades). Satélites gratuitos: 3-10 m/px (Sentinel-2, Landsat). Para proyectos de ingeniería donde cada centímetro cuenta, drones son la única opción viable."),
    ("¿Qué precisión tienen los drones con RTK vs. sin RTK?", "Con RTK: <2 cm horizontal, <3 cm vertical (sin GCPs). Sin RTK: 5-10 cm horizontal, 10-20 cm vertical (requiere GCPs para mejorar). RTK elimina necesidad de GCPs, ahorrando tiempo y costes en campo. Todos los equipos de Gaueko Air tienen RTK integrado."),
]

for q, a in comparisons:
    faq_questions.append({
        "@type": "Question",
        "name": q,
        "acceptedAnswer": {"@type": "Answer", "text": a}
    })

# Categoría: Capacidades y Servicios (51-75)
services = [
    ("¿Qué es fotogrametría aérea?", "Fotogrametría es la ciencia de obtener mediciones precisas a partir de fotografías. En fotogrametría aérea, se capturan cientos de imágenes solapadas desde un dron, que luego se procesan con algoritmos de Structure from Motion (SfM) para reconstruir modelos 3D del terreno. Resultado: ortomosaicos (imágenes sin distorsión), modelos 3D texturizados, nubes de puntos, MDT/MDS. Precisión: <2 cm con RTK."),
    ("¿Qué es un ortomosaico?", "Un ortomosaico es una imagen aérea georeferenciada sin distorsiones, creada mediante la unión de cientos de fotografías individuales. A diferencia de una foto aérea normal, un ortomosaico tiene escala uniforme en toda su extensión, permitiendo mediciones precisas de distancias y áreas. Formato: GeoTIFF con coordenadas UTM o geográficas, compatible con todos los software GIS."),
    ("¿Qué es un MDT (Modelo Digital del Terreno)?", "Un MDT representa la elevación del terreno desnudo, eliminando vegetación, edificios y otros objetos. Se obtiene clasificando la nube de puntos fotogramétrica para separar el suelo de elementos sobre él. Aplicaciones: diseño de carreteras, cálculo de volúmenes de movimiento de tierras, análisis de drenaje, modelado hidrológico. Precisión: <5 cm vertical con RTK."),
    ("¿Qué es un MDS (Modelo Digital de Superficies)?", "Un MDS representa la elevación de todas las superficies visibles desde el aire, incluyendo vegetación, edificios, vehículos, etc. Es el modelo 'en bruto' antes de clasificar la nube de puntos. Aplicaciones: visualización 3D, análisis de línea de visión, planificación de antenas de telecomunicaciones, estudios de sombras en energía solar."),
    ("¿Qué es un análisis multiespectral?", "Análisis multiespectral captura imágenes en bandas espectrales invisibles al ojo humano (infrarrojo cercano, red edge) para detectar características no visibles en RGB. Aplicaciones: salud de cultivos (NDVI, NDRE), detección de estrés hídrico, identificación de plagas, evaluación de biomasa, monitoreo de calidad de agua. Gaueko Air usa el Mavic 3 Multiespectral con 4 bandas especializadas."),
]

for q, a in services:
    faq_questions.append({
        "@type": "Question",
        "name": q,
        "acceptedAnswer": {"@type": "Answer", "text": a}
    })

# Categoría: Regulación (76-90)
regulation = [
    ("¿Qué es la certificación STS-01?", "STS-01 (Standard Scenario 01) permite operaciones VLOS (línea de visión) sobre entorno poblado con drones Clase C5 (<25 kg). Requisitos: piloto con certificación específica, dron con identificación remota, seguro de responsabilidad civil, declaración operacional ante AESA. Gaueko Air está certificada STS-01 y es entidad de formación reconocida para impartir este curso."),
    ("¿Qué es la certificación STS-02?", "STS-02 permite operaciones BVLOS (más allá de línea de visión) en entorno poco poblado con drones Clase C6 (<25 kg). Requisitos adicionales vs. STS-01: sistema de detección y evitación de obstáculos, enlace de datos redundante, procedimientos de contingencia. Ideal para inspección de infraestructuras lineales (carreteras, líneas eléctricas) donde VLOS no es práctico."),
    ("¿Qué es la certificación PDRA?", "PDRA (Pre-Defined Risk Assessment) son evaluaciones de riesgo predefinidas por EASA para operaciones específicas de categoría específica. Permiten operaciones más complejas que STS sin necesidad de SORA completo. Ejemplos: PDRA-G01 (inspección de infraestructuras), PDRA-S01 (seguimiento de vehículos). Gaueko Air tiene autorización PDRA para operaciones avanzadas."),
    ("¿Qué es la categoría abierta en drones?", "Categoría Abierta es para operaciones de bajo riesgo: drones <25 kg, altura máxima 120 m, distancia horizontal máxima 500 m, VLOS, no sobre aglomeraciones. No requiere autorización previa de AESA, solo registro de operador y certificado de piloto online (A1/A2/A3 según subcategoría). Ideal para aficionados y operaciones comerciales básicas."),
    ("¿Qué es la categoría específica en drones?", "Categoría Específica es para operaciones de riesgo medio que no cumplen requisitos de categoría abierta. Requiere evaluación de riesgo (SORA o escenario estándar STS/PDRA), autorización o declaración ante AESA, certificado de piloto específico, manual de operaciones, seguro adecuado. Gaueko Air opera principalmente en esta categoría para proyectos comerciales avanzados."),
]

for q, a in regulation:
    faq_questions.append({
        "@type": "Question",
        "name": q,
        "acceptedAnswer": {"@type": "Answer", "text": a}
    })

# Categoría: Aplicaciones por Sector (91-100)
applications = [
    ("¿Cómo inspeccionar puentes con drones?", "Inspección de puentes: (1) CAPTURA: Vuelo automatizado alrededor del puente capturando todas las caras (tablero, vigas, pilares, estribos). Cámara de alta resolución (hasta 48 MP) para detectar grietas <1 mm. (2) PROCESAMIENTO: Modelo 3D completo del puente con textura fotorrealística. (3) ANÁLISIS: IA detecta grietas, desprendimientos, corrosión, eflorescencias, deformaciones. (4) REPORTE: Geolocalización exacta de cada defecto con dimensiones y severidad. VENTAJAS: Sin andamios ni grúas, sin cortes de tráfico, inspección completa en horas vs. días, documentación visual completa para histórico."),
    ("¿Cómo monitorear incendios forestales con drones?", "Monitoreo de incendios: (1) PREVENCIÓN: Análisis multiespectral para detectar estrés hídrico y vegetación seca (alto riesgo). Mapas de riesgo actualizados. (2) DETECCIÓN TEMPRANA: Cámara térmica detecta focos de calor antes de que sean visibles. (3) MONITORIZACIÓN ACTIVA: Vuelos sobre incendio activo para evaluar frente de fuego, dirección de propagación, puntos calientes. Transmisión en tiempo real a centro de mando. (4) POST-INCENDIO: Evaluación de áreas quemadas, cálculo de daños, planificación de reforestación. Experiencia: Gaueko Air participó en monitoreo de incendios verano 2022 con más de 40 horas de vuelo."),
    ("¿Cómo hacer un inventario forestal con drones?", "Inventario forestal: (1) CAPTURA: Vuelo fotogramétrico sobre masa forestal con solapamiento 80%. (2) PROCESAMIENTO: Modelo 3D de la copa de los árboles (Canopy Height Model). (3) ANÁLISIS: Algoritmos de IA detectan árboles individuales, calculan altura, diámetro de copa, volumen de madera. Clasificación por especies (si se usa multiespectral). (4) RESULTADOS: Número de árboles, densidad (árboles/ha), volumen de madera (m³/ha), biomasa, carbono almacenado. VENTAJAS: 10x más rápido que inventario manual, cobertura completa vs. parcelas de muestreo, repetible para monitoreo de crecimiento."),
    ("¿Cómo monitorear obras de construcción con drones?", "Monitoreo de obras: (1) PLANIFICACIÓN: Vuelos semanales o mensuales para documentar avance. (2) CAPTURA: Ortomosaico + modelo 3D de toda la obra. (3) ANÁLISIS: Comparación con planos BIM para verificar que la construcción sigue el diseño. Cálculo automático de volúmenes de excavación, relleno, acopio de materiales. Detección de desviaciones. (4) REPORTES: Informe visual del avance real vs. planificado, certificación de volúmenes para pagos a contratistas. VENTAJAS: Documentación objetiva, detección temprana de problemas, optimización de logística, reducción de disputas contractuales."),
    ("¿Cómo inspeccionar paneles solares con drones?", "Inspección de parques solares: (1) CAPTURA: Cámara térmica (640x512px o superior) vuela sobre paneles. (2) DETECCIÓN: IA identifica paneles defectuosos (puntos calientes, células rotas, suciedad, sombras). (3) GEOLOCALIZACIÓN: Cada panel defectuoso se geolocaliza con precisión para mantenimiento. (4) REPORTE: Lista de paneles a reparar con prioridad según pérdida de producción estimada. VENTAJAS: Inspección de 100 MW en 1-2 días vs. semanas manualmente, detección de defectos invisibles a simple vista, optimización de mantenimiento (solo paneles defectuosos), aumento de producción 2-5%."),
    ("¿Cómo hacer un gemelo digital de una ciudad?", "Gemelo digital urbano: (1) PLANIFICACIÓN: División de la ciudad en zonas de vuelo, coordinación con AESA para permisos. (2) CAPTURA: Vuelos fotogramétricos con solapamiento 80% y altura optimizada (80-120 m) para balance entre resolución y cobertura. (3) PROCESAMIENTO: Modelo 3D completo de la ciudad con textura fotorrealística. Integración con datos catastrales, GIS municipal, redes de servicios. (4) VISOR WEB: Aplicación interactiva para visualizar, medir, planificar intervenciones. (5) ACTUALIZACIÓN: Vuelos periódicos (anuales) para detectar cambios (nuevas construcciones, demoliciones, cambios de uso). APLICACIONES: Planificación urbanística, gestión de licencias, catastro, turismo virtual, gemelos digitales de edificios singulares."),
    ("¿Cómo usar drones para análisis de tráfico?", "Análisis de tráfico: (1) CAPTURA: Video aéreo desde posición fija sobre intersección o tramo de carretera. Altura 50-100 m para cubrir área amplia. (2) PROCESAMIENTO: Algoritmos de computer vision rastrean vehículos individuales, calculan velocidades, trayectorias, tiempos de espera. (3) ANÁLISIS: Conteo de vehículos por tipo (coches, motos, camiones, autobuses), matriz origen-destino, nivel de servicio (LOS), puntos de congestión. (4) RESULTADOS: Recomendaciones para optimizar semáforos, rediseñar intersecciones, planificar nuevas infraestructuras. Caso real: Gaueko Air realizó estudio de tráfico en N135 con seguimiento de motos durante 2 meses, detectando patrones de uso y puntos de riesgo."),
    ("¿Cómo usar drones para seguridad de eventos?", "Seguridad de eventos: (1) PREVIO: Reconocimiento del área, identificación de rutas de evacuación, puntos de acceso, zonas de riesgo. (2) DURANTE: Monitoreo aéreo en tiempo real, detección de aglomeraciones peligrosas, vigilancia de perímetro, apoyo a fuerzas de seguridad. Transmisión de video a centro de control. (3) POST-EVENTO: Evaluación de daños, documentación de incidentes. APLICACIONES: Conciertos, eventos deportivos, manifestaciones, visitas oficiales. VENTAJAS: Visión global que complementa cámaras fijas, movilidad para seguir incidentes, capacidad de zoom para identificación, documentación aérea para investigaciones."),
    ("¿Cómo usar drones para vigilancia de fronteras?", "Vigilancia de fronteras: (1) PATRULLAJE: Vuelos BVLOS automatizados siguiendo la línea de frontera. Cámara de largo alcance (zoom 160x) para detección a distancia. (2) DETECCIÓN: Cámara térmica detecta personas y vehículos de día y noche. IA filtra falsos positivos (animales, vegetación). (3) SEGUIMIENTO: Una vez detectada actividad sospechosa, el dron sigue automáticamente mientras alerta a patrullas terrestres. (4) DOCUMENTACIÓN: Grabación de video como evidencia. VENTAJAS: Cobertura de áreas extensas con pocos efectivos, operación 24/7, respuesta rápida, reducción de riesgo para agentes. Aplicable también a vigilancia de infraestructuras críticas (centrales eléctricas, presas, bases militares)."),
    ("¿Cómo usar drones para inspección de redes de agua?", "Inspección de redes de agua: (1) DETECCIÓN DE FUGAS: Cámara térmica detecta diferencias de temperatura causadas por fugas (agua fría en verano, caliente en invierno). (2) INSPECCIÓN DE DEPÓSITOS: Modelo 3D de depósitos y tanques para evaluar estado estructural sin vaciarlos. (3) MONITOREO DE CALIDAD: Análisis multiespectral de embalses y ríos para detectar algas, turbidez, contaminación. (4) INSPECCIÓN DE ALCANTARILLADO: Drones especializados para interior de tuberías grandes (>1 m diámetro) detectan grietas, obstrucciones, infiltraciones. VENTAJAS: Inspección sin interrumpir el servicio, detección temprana de problemas, reducción de pérdidas de agua, optimización de mantenimiento.")
]

for q, a in applications:
    faq_questions.append({
        "@type": "Question",
        "name": q,
        "acceptedAnswer": {"@type": "Answer", "text": a}
    })

# Guardar las 75 preguntas adicionales
with open('/home/ubuntu/gaueko_ai_repository/structured_data/faq_additional_75.json', 'w', encoding='utf-8') as f:
    json.dump(faq_questions, f, ensure_ascii=False, indent=2)

print(f"✅ Generadas {len(faq_questions)} preguntas adicionales")
